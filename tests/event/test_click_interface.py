from random import randint
from typing import Any
from typing import Dict

from retrying import retry

from apysc import EventType
from apysc import MouseEvent
from apysc.event.click_interface import ClickInterface
from apysc.event.handler import get_handler_name
from apysc.expression import expression_file_util
from apysc.type.variable_name_interface import VariableNameInterface
from tests import testing_helper


class _TestClickInterface(ClickInterface, VariableNameInterface):

    def __init__(self) -> None:
        """
        Test class for ClickInterface.
        """
        self.variable_name = 'test_click_interface_1'


class TestClickInterface:

    def on_click_1(self, e: MouseEvent, options: Dict[str, Any]) -> None:
        """
        Click handler method for testing.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    def on_click_2(self, e: MouseEvent, options: Dict[str, Any]) -> None:
        """
        Click handler method for testing.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_click(self) -> None:
        interface_1: _TestClickInterface = _TestClickInterface()
        name: str = interface_1.click(
            handler=self.on_click_1)
        assert interface_1._click_handlers[  # type: ignore
            name]['handler'] == self.on_click_1
        assert interface_1._click_handlers[name]['options'] == {}

        interface_2: _TestClickInterface = _TestClickInterface()
        name = interface_2.click(handler=self.on_click_1, options={'a': 10})
        assert interface_2._click_handlers[
            name]['options'] == {'a': 10}

        interface_3: ClickInterface = ClickInterface()
        testing_helper.assert_raises(
            expected_error_class=TypeError,
            func_or_method=interface_3.click,
            kwargs={'handler': self.on_click_1})

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_click_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: ClickInterface = ClickInterface()
        testing_helper.assert_raises(
            expected_error_class=TypeError,
            func_or_method=interface_1._append_click_expression,
            kwargs={
                'name': 'any_name',
            })

        interface_2: _TestClickInterface = _TestClickInterface()
        handler_name: str = interface_2.click(handler=self.on_click_1)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_2.variable_name}.click({handler_name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__initialize_click_handlers_if_not_initialized(self) -> None:
        interface_1: ClickInterface = ClickInterface()
        interface_1._initialize_click_handlers_if_not_initialized()
        assert interface_1._click_handlers == {}
        interface_1._initialize_click_handlers_if_not_initialized()
        assert interface_1._click_handlers == {}

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_unbind_click(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: ClickInterface = ClickInterface()
        testing_helper.assert_raises(
            expected_error_class=TypeError,
            func_or_method=interface_1.unbind_click,
            kwargs={'handler': self.on_click_1})

        interface_2: _TestClickInterface = _TestClickInterface()
        interface_2.click(handler=self.on_click_1)
        interface_2.unbind_click(handler=self.on_click_1)
        assert not interface_2._click_handlers
        handler_name: str = get_handler_name(
            handler=self.on_click_1)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_2.variable_name}.off('
            f'"{EventType.CLICK.value}", {handler_name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_unbind_click_all(self) -> None:
        expression_file_util.remove_expression_file
        interface_1: ClickInterface = ClickInterface()
        testing_helper.assert_raises(
            expected_error_class=TypeError,
            func_or_method=interface_1.unbind_click_all)

        interface_2: _TestClickInterface = _TestClickInterface()
        interface_2.click(handler=self.on_click_1)
        interface_2.click(handler=self.on_click_2)
        interface_2.unbind_click_all()
        assert interface_2._click_handlers == {}
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_2.variable_name}.off("{EventType.CLICK.value}");'
        )
        assert expected in expression

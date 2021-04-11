from apysc.expression import expression_file_util
from random import randint
from typing import Any, Dict

from retrying import retry

from apysc.event.click_interface import ClickInterface
from apysc import Event
from apysc.type.variable_name_interface import VariableNameInterface
from tests import testing_helper


class _TestClickInterface(ClickInterface, VariableNameInterface):

    def __init__(self) -> None:
        """
        Test class for ClickInterface.
        """
        self.variable_name = 'test_click_interface_1'


class TestClickInterface:

    def on_click_1(self, e: Event, kwargs: Dict[str, Any]) -> None:
        """
        Click handler method for testing.

        Parameters
        ----------
        e : Event
            Created event instance.
        kwargs : dict
            Keyword arguments to pass to.
        """

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_click(self) -> None:
        interface_1: _TestClickInterface = _TestClickInterface()
        name: str = interface_1.click(
            handler=self.on_click_1)
        assert interface_1._click_handlers[
            name]['handler'] == self.on_click_1
        assert interface_1._click_handlers[name]['kwargs'] == {}

        interface_2: _TestClickInterface = _TestClickInterface()
        name = interface_2.click(handler=self.on_click_1, kwargs={'a': 10})
        assert interface_2._click_handlers[
            name]['kwargs'] == {'a': 10}

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
            func_or_method=interface_1.click,
            kwargs={
                'handler': self.on_click_1,
            })

        interface_2: _TestClickInterface = _TestClickInterface()
        handler_name: str = interface_2.click(handler=self.on_click_1)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_2.variable_name}.click({handler_name});'
        )
        assert expected in expression

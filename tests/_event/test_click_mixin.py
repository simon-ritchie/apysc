from typing import Any
from typing import Dict

import apysc as ap
from apysc._event.click_mixin import ClickMixIn
from apysc._event.handler import get_handler_name
from apysc._expression import expression_data_util
from apysc._testing import testing_helper
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_mixin import VariableNameMixIn


class _TestClickMixIn(ClickMixIn, VariableNameMixIn):
    def __init__(self) -> None:
        """
        Test class for ClickMixIn.
        """
        self.variable_name = "test_click_mixin_1"


class TestClickMixIn:
    def on_click_1(self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Click handler method for testing.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    def on_click_2(self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Click handler method for testing.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    @apply_test_settings()
    def test_click(self) -> None:
        ap.Stage()
        mixin_1: _TestClickMixIn = _TestClickMixIn()
        name: str = mixin_1.click(handler=self.on_click_1)
        assert mixin_1._click_handlers[name].handler == self.on_click_1
        assert mixin_1._click_handlers[name].options == {}
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin_1.variable_name}.click({name});"
        assert expected in expression

        mixin_2: _TestClickMixIn = _TestClickMixIn()
        name = mixin_2.click(handler=self.on_click_1, options={"a": 10})
        assert mixin_2._click_handlers[name].options == {"a": 10}

        mixin_3: ClickMixIn = ClickMixIn()
        testing_helper.assert_raises(
            expected_error_class=TypeError,
            callable_=mixin_3.click,
            handler=self.on_click_1,
        )

    @apply_test_settings()
    def test__initialize_click_handlers_if_not_initialized(self) -> None:
        mixin_1: ClickMixIn = ClickMixIn()
        mixin_1._initialize_click_handlers_if_not_initialized()
        assert mixin_1._click_handlers == {}
        mixin_1._initialize_click_handlers_if_not_initialized()
        assert mixin_1._click_handlers == {}

    @apply_test_settings()
    def test_unbind_click(self) -> None:
        ap.Stage()
        mixin_1: ClickMixIn = ClickMixIn()
        testing_helper.assert_raises(
            expected_error_class=TypeError,
            callable_=mixin_1.unbind_click,
            handler=self.on_click_1,
        )

        mixin_2: _TestClickMixIn = _TestClickMixIn()
        mixin_2.click(handler=self.on_click_1)
        mixin_2.unbind_click(handler=self.on_click_1)
        assert not mixin_2._click_handlers
        handler_name: str = get_handler_name(handler=self.on_click_1, instance=mixin_2)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin_2.variable_name}.off("
            f'"{ap.MouseEventType.CLICK.value}", {handler_name});'
        )
        assert expected in expression

    @apply_test_settings()
    def test_unbind_click_all(self) -> None:
        ap.Stage()
        mixin_1: ClickMixIn = ClickMixIn()
        testing_helper.assert_raises(
            expected_error_class=TypeError, callable_=mixin_1.unbind_click_all
        )

        mixin_2: _TestClickMixIn = _TestClickMixIn()
        mixin_2.click(handler=self.on_click_1)
        mixin_2.click(handler=self.on_click_2)
        mixin_2.unbind_click_all()
        assert mixin_2._click_handlers == {}
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin_2.variable_name}.off(" f'"{ap.MouseEventType.CLICK.value}");'
        )
        assert expected in expression

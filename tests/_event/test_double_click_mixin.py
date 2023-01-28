from random import randint
from typing import Any
from typing import Dict

from retrying import retry

import apysc as ap
from apysc._event.double_click_mixin import DoubleClickMixIn
from apysc._expression import expression_data_util
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._testing.testing_helper import apply_test_settings


class _TestDoubleClick(DoubleClickMixIn, VariableNameMixIn):
    def __init__(self) -> None:
        """
        Class for double click mixin's testing.
        """
        self.variable_name = "test_double_click"


class TestDoubleClickMixIn:
    def on_double_click_1(self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Test handler for double click event.

        Parameters
        ----------
        e : MouseEvent
            Event instance.
        options : dict
            Optional arguments dictionary.
        """

    def on_double_click_2(self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Test handler for double click event.

        Parameters
        ----------
        e : MouseEvent
            Event instance.
        options : dict
            Optional arguments dictionary.
        """

    @apply_test_settings()
    def test__initialize_dblclick_handlers_if_not_initialized(self) -> None:
        mixin_1: DoubleClickMixIn = DoubleClickMixIn()
        mixin_1._initialize_dblclick_handlers_if_not_initialized()
        assert mixin_1._dblclick_handlers == {}

        mixin_1._initialize_dblclick_handlers_if_not_initialized()

    @apply_test_settings()
    def test_dblclick(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestDoubleClick = _TestDoubleClick()
        name: str = mixin_1.dblclick(handler=self.on_double_click_1)
        assert mixin_1._dblclick_handlers[name].handler == self.on_double_click_1
        assert mixin_1._dblclick_handlers[name].options == {}

        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin_1.variable_name}.dblclick({name});"
        assert expected in expression
        expression = expression_data_util.get_current_event_handler_scope_expression()
        expected = f"function {name}"
        assert expected in expression

    @apply_test_settings()
    def test_unbind_dblclick(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestDoubleClick = _TestDoubleClick()
        mixin_1.dblclick(handler=self.on_double_click_1)
        mixin_1.unbind_dblclick(handler=self.on_double_click_1)
        assert mixin_1._dblclick_handlers == {}
        expression: str = expression_data_util.get_current_expression()
        assert "off(" in expression

    @apply_test_settings()
    def test_unbind_dblclick_all(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestDoubleClick = _TestDoubleClick()
        mixin_1.dblclick(handler=self.on_double_click_1)
        mixin_1.unbind_dblclick_all()
        assert mixin_1._dblclick_handlers == {}
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin_1.variable_name}.off(" f'"{ap.MouseEventType.DBLCLICK.value}");'
        )
        assert expected in expression

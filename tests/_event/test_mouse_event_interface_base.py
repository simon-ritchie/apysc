from random import randint
from typing import Any
from typing import Dict

from retrying import retry

import apysc as ap
from apysc._event.click_mixin import ClickMixIn
from apysc._expression import expression_data_util
from apysc._type.variable_name_mixin import VariableNameMixIn


class _TestClickMixIn(ClickMixIn, VariableNameMixIn):
    def __init__(self) -> None:
        """MixIn for testing."""
        self.variable_name = "test_click_mixin"


class TestMouseEventInterfaceBase:
    def on_click_1(self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Test handler method.

        Parameters
        ----------
        e : MouseEvent
            Event instance.
        options : dict
            Optional arguments dictionary.
        """

    def on_click_2(self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Test handler method.

        Parameters
        ----------
        e : MouseEvent
            Event instance.
        options : dict
            Optional arguments dictionary.
        """

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__unbind_mouse_event(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestClickMixIn = _TestClickMixIn()
        mixin_1.click(handler=self.on_click_1)
        mixin_1._unbind_mouse_event(
            handler=self.on_click_1,
            mouse_event_type=ap.MouseEventType.CLICK,
            handlers_dict=mixin_1._click_handlers,
        )
        assert mixin_1._click_handlers == {}
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin_1.variable_name}" f'.off("{ap.MouseEventType.CLICK.value}",'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__unbind_all_mouse_events(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestClickMixIn = _TestClickMixIn()
        mixin_1.click(handler=self.on_click_1)
        mixin_1.click(handler=self.on_click_2)
        mixin_1._unbind_all_mouse_events(
            mouse_event_type=ap.MouseEventType.CLICK,
            handlers_dict=mixin_1._click_handlers,
        )
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin_1.variable_name}" f'.off("{ap.MouseEventType.CLICK.value}");'
        )
        assert expected in expression
        assert mixin_1._click_handlers == {}

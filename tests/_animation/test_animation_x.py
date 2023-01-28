from random import randint

from retrying import retry

import apysc as ap
from apysc._display.x_mixin import XMixIn
from apysc._expression import var_names
from apysc._testing.testing_helper import assert_attrs
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestAnimationX:
    @apply_test_settings()
    def test___init__(self) -> None:
        interface: VariableNameMixIn = VariableNameMixIn()
        interface.variable_name = "test_animation_x"
        animation_x: ap.AnimationX = ap.AnimationX(
            target=interface,
            x=100,
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT,
        )
        assert_attrs(
            expected_attrs={
                "_x": 100,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_x,
        )
        assert animation_x.variable_name.startswith(f"{var_names.ANIMATION_X}_")

    @apply_test_settings()
    def test__get_animation_func_expression(self) -> None:
        interface: VariableNameMixIn = VariableNameMixIn()
        interface.variable_name = "test_animation_x"
        animation_x: ap.AnimationX = ap.AnimationX(
            target=interface,
            x=100,
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT,
        )
        expression: str = animation_x._get_animation_func_expression()
        expected: str = f"\n  .x({animation_x._x.variable_name});"
        assert expression == expected

    @apply_test_settings()
    def test__get_complete_event_in_handler_head_expression(self) -> None:
        target: XMixIn = XMixIn()
        target.variable_name = "test_animation_x"
        animation_x: ap.AnimationX = ap.AnimationX(target=target, x=100)
        expression: str = animation_x._get_complete_event_in_handler_head_expression()
        assert expression == (
            f"{target._x.variable_name} = " f"{animation_x._x.variable_name};"
        )

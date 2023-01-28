from random import randint

from retrying import retry

import apysc as ap
from apysc._display.width_mixin import WidthMixIn
from apysc._expression import var_names
from apysc._testing.testing_helper import assert_attrs
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestAnimationWidth:
    @apply_test_settings()
    def test___init__(self) -> None:
        target: VariableNameMixIn = VariableNameMixIn()
        target.variable_name = "test_animation_width"
        animation_width: ap.AnimationWidth = ap.AnimationWidth(
            target=target,
            width=100,
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT,
        )
        assert animation_width.variable_name.startswith(f"{var_names.ANIMATION_WIDTH}_")
        assert_attrs(
            expected_attrs={
                "_target": target,
                "_width": 100,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_width,
        )

    @apply_test_settings()
    def test__get_animation_func_expression(self) -> None:
        target: VariableNameMixIn = VariableNameMixIn()
        target.variable_name = "test_animation_width"
        animation_width: ap.AnimationWidth = ap.AnimationWidth(target=target, width=100)
        expression: str = animation_width._get_animation_func_expression()
        assert expression == f"\n  .width({animation_width._width.variable_name});"

    @apply_test_settings()
    def test__get_complete_event_in_handler_head_expression(self) -> None:
        target: WidthMixIn = WidthMixIn()
        target.variable_name = "test_width_interface"
        animation_width: ap.AnimationWidth = ap.AnimationWidth(target=target, width=100)
        expression: str = (
            animation_width._get_complete_event_in_handler_head_expression()
        )
        assert expression == (
            f"{target._width.variable_name} = "
            f"{animation_width._width.variable_name};"
        )

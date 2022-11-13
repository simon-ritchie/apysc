from random import randint

from retrying import retry

import apysc as ap
from apysc._display.width_and_height_mixin_for_ellipse import (
    WidthAndHeightMixInForEllipse,
)
from apysc._expression import var_names
from apysc._testing.testing_helper import assert_attrs
from apysc._type.variable_name_mixin import VariableNameMixIn


class TestAnimationHeightForEllipse:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target: VariableNameMixIn = VariableNameMixIn()
        target.variable_name = "test_animation_height_for_ellipse"
        animation_height_for_ellipse: ap.AnimationHeightForEllipse = (
            ap.AnimationHeightForEllipse(
                target=target,
                height=100,
                duration=1000,
                delay=500,
                easing=ap.Easing.EASE_OUT_QUINT,
            )
        )
        assert animation_height_for_ellipse.variable_name.startswith(
            f"{var_names.ANIMATION_HEIGHT_FOR_ELLIPSE}_"
        )
        assert_attrs(
            expected_attrs={
                "_target": target,
                "_height": 100,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_height_for_ellipse,
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        target: VariableNameMixIn = VariableNameMixIn()
        target.variable_name = "test_animation_height_for_ellipse"
        animation_height_for_ellipse: ap.AnimationHeightForEllipse = (
            ap.AnimationHeightForEllipse(target=target, height=100)
        )
        expression: str = animation_height_for_ellipse._get_animation_func_expression()
        assert expression == (
            "\n  .attr({ry: Math.trunc"
            f"({animation_height_for_ellipse._height.variable_name} / 2)}});"
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_complete_event_in_handler_head_expression(self) -> None:
        target: WidthAndHeightMixInForEllipse = WidthAndHeightMixInForEllipse()
        target.variable_name = "test_animation_height_for_ellipse"
        anim_for_ellipse: ap.AnimationHeightForEllipse = ap.AnimationHeightForEllipse(
            target=target, height=100
        )
        expression: str = (
            anim_for_ellipse._get_complete_event_in_handler_head_expression()
        )
        expected: str = (
            f"{target._height.variable_name} = "
            f"{anim_for_ellipse._height.variable_name};"
        )
        assert expression == expected

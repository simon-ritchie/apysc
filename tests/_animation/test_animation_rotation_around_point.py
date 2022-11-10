from random import randint

from retrying import retry

import apysc as ap
from apysc._display import rotation_interface_helper
from apysc._display.rotation_around_point_mixin import RotationAroundPointMixIn
from apysc._expression import var_names
from apysc._testing.testing_helper import assert_attrs
from apysc._testing.testing_helper import assert_raises
from apysc._type.variable_name_mixin import VariableNameMixIn


class TestAnimationRotationAroundPoint:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target_1: RotationAroundPointMixIn = RotationAroundPointMixIn()
        target_1.variable_name = "test_animation_rotation_around_point"
        animation: ap.AnimationRotationAroundPoint = ap.AnimationRotationAroundPoint(
            target=target_1,
            rotation_around_point=100,
            x=200,
            y=300,
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT,
        )
        assert animation.variable_name.startswith(
            f"{var_names.ANIMATION_ROTATION_AROUND_POINT}_"
        )
        assert_attrs(
            expected_attrs={
                "_target": target_1,
                "_rotation_around_point": 100,
                "_x": 200,
                "_y": 300,
                "_before_rotation_around_point": 0,
                "_rotation_around_point_diff": 100,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation,
        )

        target_2: VariableNameMixIn = VariableNameMixIn()
        target_2.variable_name = "test_animation_rotation_around_point"
        assert_raises(
            expected_error_class=TypeError,
            callable_=ap.AnimationRotationAroundPoint,
            match="Specified `target` argument is not a " "RotationAroundPointMixIn",
            target=target_2,
            rotation_around_point=100,
            x=200,
            y=300,
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        target: RotationAroundPointMixIn = RotationAroundPointMixIn()
        target.variable_name = "test_animation_rotation_around_point"
        animation: ap.AnimationRotationAroundPoint = ap.AnimationRotationAroundPoint(
            target=target, rotation_around_point=100, x=200, y=300
        )
        expression: str = animation._get_animation_func_expression()
        assert expression == (
            "\n  .rotate("
            f"{animation._rotation_around_point_diff.variable_name}, "
            f"{animation._x.variable_name}, "
            f"{animation._y.variable_name});"
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_complete_event_in_handler_head_expression(self) -> None:
        target: RotationAroundPointMixIn = RotationAroundPointMixIn()
        target.variable_name = "test_animation_rotation_around_point"
        animation: ap.AnimationRotationAroundPoint = ap.AnimationRotationAroundPoint(
            target=target, rotation_around_point=100, x=200, y=300
        )
        expression: str = animation._get_complete_event_in_handler_head_expression()
        key_exp_str: str = rotation_interface_helper.get_coordinates_key_for_expression(
            x=animation._x, y=animation._y
        ).value
        expected: str = (
            f"{target._rotation_around_point.variable_name}"
            f"[{key_exp_str}] = "
            f"{animation._rotation_around_point.variable_name};"
        )
        assert expression == expected

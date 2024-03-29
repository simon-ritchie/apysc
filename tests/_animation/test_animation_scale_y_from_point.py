import apysc as ap
from apysc._display import scale_interface_helper
from apysc._display.scale_y_from_point_mixin import ScaleYFromPointMixIn
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs
from apysc._testing.testing_helper import assert_raises
from apysc._type.variable_name_mixin import VariableNameMixIn


class TestAnimationScaleYFromPoint:
    @apply_test_settings()
    def test___init__(self) -> None:
        target_1: ScaleYFromPointMixIn = ScaleYFromPointMixIn()
        target_1.variable_name = "test_animation_scale_y_from_point"
        animation: ap.AnimationScaleYFromPoint = ap.AnimationScaleYFromPoint(
            target=target_1,
            scale_y_from_point=2.0,
            y=100,
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT,
        )
        assert animation.variable_name.startswith(
            f"{var_names.ANIMATION_SCALE_Y_FROM_POINT}_"
        )
        assert_attrs(
            expected_attrs={
                "_target": target_1,
                "_scale_y_from_point": 2.0,
                "_y": 100,
                "_before_scale_y_from_point": 1.0,
                "_scale_y_from_point_diff_ratio": 2.0,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation,
        )

        target_2: VariableNameMixIn = VariableNameMixIn()
        target_2.variable_name = "test_animation_scale_y_from_point"
        assert_raises(
            expected_error_class=TypeError,
            callable_=ap.AnimationScaleYFromPoint,
            match="Specified `target` argument is not a ScaleYFromPointMixIn",
            target=target_2,
            scale_y_from_point=2.0,
            y=100,
        )

    @apply_test_settings()
    def test__get_animation_func_expression(self) -> None:
        target: ScaleYFromPointMixIn = ScaleYFromPointMixIn()
        target.variable_name = "test_animation_scale_y_from_point"
        animation: ap.AnimationScaleYFromPoint = ap.AnimationScaleYFromPoint(
            target=target, scale_y_from_point=2.0, y=100
        )
        expression: str = animation._get_animation_func_expression()
        assert expression == (
            "\n  .scale(1, "
            f"{animation._scale_y_from_point_diff_ratio.variable_name}, 0, "
            f"{animation._y.variable_name});"
        )

    @apply_test_settings()
    def test__get_complete_event_in_handler_head_expression(self) -> None:
        target: ScaleYFromPointMixIn = ScaleYFromPointMixIn()
        target.variable_name = "test_animation_scale_y_from_point"
        animation: ap.AnimationScaleYFromPoint = ap.AnimationScaleYFromPoint(
            target=target, scale_y_from_point=2.0, y=100
        )
        expression: str = animation._get_complete_event_in_handler_head_expression()
        key_exp_str: str = scale_interface_helper.get_coordinate_key_for_expression(
            coordinate=animation._y
        ).value
        assert expression == (
            f"{target._scale_y_from_point.variable_name}"
            f"[{key_exp_str}] = "
            f"{animation._scale_y_from_point.variable_name};"
        )

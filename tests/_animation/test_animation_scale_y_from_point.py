from random import randint

from retrying import retry

import apysc as ap
from apysc._type.variable_name_interface import VariableNameInterface
from apysc._display.scale_y_from_point_interface import \
    ScaleYFromPointInterface
from apysc._expression import var_names
from tests.testing_helper import assert_attrs, assert_raises


class TestAnimationScaleYFromPoint:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target_1: ScaleYFromPointInterface = ScaleYFromPointInterface()
        target_1.variable_name = 'test_animation_scale_y_from_point'
        animation: ap.AnimationScaleYFromPoint = ap.AnimationScaleYFromPoint(
            target=target_1,
            scale_y_from_point=2.0,
            y=100,
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT)
        assert animation.variable_name.startswith(
            f'{var_names.ANIMATION_SCALE_Y_FROM_POINT}_')
        assert_attrs(
            expected_attrs={
                '_target': target_1,
                '_scale_y_from_point': 2.0,
                '_y': 100,
                '_before_scale_y_from_point': 1.0,
                '_scale_y_from_point_diff_ratio': 2.0,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation,
        )

        target_2: VariableNameInterface = VariableNameInterface()
        target_2.variable_name = 'test_animation_scale_y_from_point'
        assert_raises(
            expected_error_class=TypeError,
            func_or_method=ap.AnimationScaleYFromPoint,
            kwargs={
                'target': target_2,
                'scale_y_from_point': 2.0,
                'y': 100,
            },
            match='Specified `target` argument is not a '
                  'ScaleYFromPointInterface')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        target_1: ScaleYFromPointInterface = ScaleYFromPointInterface()
        target_1.variable_name = 'test_animation_scale_y_from_point'
        animation: ap.AnimationScaleYFromPoint = ap.AnimationScaleYFromPoint(
            target=target_1,
            scale_y_from_point=2.0,
            y=100)
        expression: str = animation._get_animation_func_expression()
        assert expression == (
            '\n  .scale(1, '
            f'{animation._scale_y_from_point_diff_ratio.variable_name}, 0, '
            f'{animation._y.variable_name});'
        )

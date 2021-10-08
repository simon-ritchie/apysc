from random import randint
from apysc._type.variable_name_interface import VariableNameInterface

from retrying import retry

import apysc as ap
from apysc._display.scale_x_from_point_interface import \
    ScaleXFromPointInterface
from apysc._expression import var_names
from tests.testing_helper import assert_attrs, assert_raises


class TestAnimationScaleXFromPoint:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target_1: ScaleXFromPointInterface = ScaleXFromPointInterface()
        target_1.variable_name = 'test_animation_scale_x_from_point'
        animation: ap.AnimationScaleXFromPoint = ap.AnimationScaleXFromPoint(
            target=target_1,
            scale_x_from_point=2.0,
            x=50,
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT,
        )
        assert animation.variable_name.startswith(
            f'{var_names.ANIMATION_SCALE_X_FROM_POINT}_')
        assert_attrs(
            expected_attrs={
                '_target': target_1,
                '_scale_x_from_point': 2.0,
                '_before_scale_x_from_point': 1.0,
                '_scale_x_from_point_diff_ratio': 2.0,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation)

        target_2: VariableNameInterface = VariableNameInterface()
        target_2.variable_name = 'test_animation_scale_x_from_point'
        assert_raises(
            expected_error_class=TypeError,
            func_or_method=ap.AnimationScaleXFromPoint,
            kwargs={
                'target': target_2,
                'scale_x_from_point': 2.0,
                'x': 50,
            },
            match='Specified `target` argument is not a '
                  'ScaleXFromPointInterface'
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        target: ScaleXFromPointInterface = ScaleXFromPointInterface()
        target.variable_name = 'test_animation_scale_x_from_point'
        animation: ap.AnimationScaleXFromPoint = ap.AnimationScaleXFromPoint(
            target=target,
            scale_x_from_point=2.0,
            x=50,
        )
        expression: str = animation._get_animation_func_expression()
        assert expression == (
            '\n  .scale('
            f'{animation._scale_x_from_point_diff_ratio.variable_name}, 1, '
            f'{animation._x.variable_name}, 0);'
        )

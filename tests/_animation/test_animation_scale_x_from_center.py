from random import randint

from retrying import retry

import apysc as ap
from apysc._display.scale_x_from_center_interface import \
    ScaleXFromCenterInterface
from apysc._type.variable_name_interface import VariableNameInterface
from apysc._expression import var_names
from tests.testing_helper import assert_attrs, assert_raises


class TestAnimationScaleXFromCenter:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target_1: ScaleXFromCenterInterface = ScaleXFromCenterInterface()
        target_1.variable_name = 'test_animation_scale_x_from_center'
        animation: ap.AnimationScaleXFromCenter = \
            ap.AnimationScaleXFromCenter(
                target=target_1,
                scale_x_from_center=2.0,
                duration=1000,
                delay=500,
                easing=ap.Easing.EASE_OUT_QUINT)
        assert animation.variable_name.startswith(
            f'{var_names.ANIMATION_SCALE_X_FROM_CENTER}_'
        )
        assert_attrs(
            expected_attrs={
                '_target': target_1,
                '_scale_x_from_center': 2.0,
                '_before_scale_x_from_center': 1.0,
                '_scale_x_from_center_diff_ratio': 2.0,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation)

        target_2: VariableNameInterface = VariableNameInterface()
        target_2.variable_name = 'test_animation_scale_x_from_center'
        assert_raises(
            expected_error_class=TypeError,
            func_or_method=ap.AnimationScaleXFromCenter,
            kwargs={
                'target': target_2,
                'scale_x_from_center': 2.0,
            },
            match='Specified `target` argument is not a '
                  'ScaleXFromCenterInterface')

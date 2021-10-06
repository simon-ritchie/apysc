from random import randint

from retrying import retry

import apysc as ap
from apysc._display.rotation_around_center_interface import \
    RotationAroundCenterInterface
from apysc._expression import var_names
from apysc._type.variable_name_interface import VariableNameInterface
from tests.testing_helper import assert_attrs, assert_raises


class TestAnimationRotationAroundCenter:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target_1: RotationAroundCenterInterface = \
            RotationAroundCenterInterface()
        target_1.variable_name = 'test_animation_rotation_around_center'
        animation_rotation_around_center: ap.AnimationRotationAroundCenter = \
            ap.AnimationRotationAroundCenter(
                target=target_1,
                rotation_around_center=50,
                duration=1000,
                delay=500,
                easing=ap.Easing.EASE_OUT_QUINT)
        assert animation_rotation_around_center.variable_name.startswith(
            f'{var_names.ANIMATION_ROTATION_AROUND_CENTER}_')
        assert_attrs(
            expected_attrs={
                '_target': target_1,
                '_rotation_around_center': 50,
                '_before_rotation_around_center': 0,
                '_rotation_around_center_diff': 50,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_rotation_around_center,
        )

        target_2: VariableNameInterface = VariableNameInterface()
        assert_raises(
            expected_error_class=TypeError,
            func_or_method=ap.AnimationRotationAroundCenter,
            kwargs={
                'target': target_2,
                'rotation_around_center': 50,
            },
            match='Specified `target` argument is not a '
                  'RotationAroundCenterInterface')

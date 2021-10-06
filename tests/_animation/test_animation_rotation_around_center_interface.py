from random import randint

from retrying import retry

import apysc as ap
from apysc._display.rotation_around_center_interface import \
    RotationAroundCenterInterface
from tests.testing_helper import assert_attrs


class TestAnimationRotationAroundCenterInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_rotation_around_center(self) -> None:
        interface: RotationAroundCenterInterface = \
            RotationAroundCenterInterface()
        animation_rotation_around_center: ap.AnimationRotationAroundCenter = \
            interface.animation_rotation_around_center(
                rotation_around_center=50, duration=1000,
                delay=500, easing=ap.Easing.EASE_OUT_QUINT)
        assert_attrs(
            expected_attrs={
                '_target': interface,
                '_rotation_around_center': 50,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_rotation_around_center)

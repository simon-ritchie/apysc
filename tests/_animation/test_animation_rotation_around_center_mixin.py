from random import randint

from retrying import retry

import apysc as ap
from apysc._display.rotation_around_center_mixin import RotationAroundCenterMixIn
from apysc._testing.testing_helper import assert_attrs


class TestAnimationRotationAroundCenterMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_rotation_around_center(self) -> None:
        mixin: RotationAroundCenterMixIn = RotationAroundCenterMixIn()
        animation_rotation_around_center: ap.AnimationRotationAroundCenter = (
            mixin.animation_rotation_around_center(
                rotation_around_center=50,
                duration=1000,
                delay=500,
                easing=ap.Easing.EASE_OUT_QUINT,
            )
        )
        assert_attrs(
            expected_attrs={
                "_target": mixin,
                "_rotation_around_center": 50,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_rotation_around_center,
        )

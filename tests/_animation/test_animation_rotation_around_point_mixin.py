from random import randint

from retrying import retry

import apysc as ap
from apysc._display.rotation_around_point_mixin import RotationAroundPointMixIn
from apysc._testing.testing_helper import assert_attrs


class TestAnimationRotationAroundPointMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_rotation_around_point(self) -> None:
        mixin: RotationAroundPointMixIn = RotationAroundPointMixIn()
        mixin.variable_name = "test_animation_rotation_around_point_mixin"
        animation: ap.AnimationRotationAroundPoint = (
            mixin.animation_rotation_around_point(
                rotation_around_point=100,
                x=200,
                y=300,
                duration=1000,
                delay=500,
                easing=ap.Easing.EASE_OUT_QUINT,
            )
        )
        assert_attrs(
            expected_attrs={
                "_target": mixin,
                "_rotation_around_point": 100,
                "_x": 200,
                "_y": 300,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation,
        )

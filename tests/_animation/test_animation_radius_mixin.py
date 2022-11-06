from random import randint

from retrying import retry

import apysc as ap
from apysc._animation.animation_radius_mixin import AnimationRadiusMixIn
from apysc._testing.testing_helper import assert_attrs


class TestAnimationRadiusMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_radius(self) -> None:
        mixin: AnimationRadiusMixIn = AnimationRadiusMixIn()
        mixin.variable_name = "test_animation_radius_mixin"
        animation_radius: ap.AnimationRadius = mixin.animation_radius(
            radius=100, duration=1000, delay=500, easing=ap.Easing.EASE_OUT_QUINT
        )
        assert_attrs(
            expected_attrs={
                "_target": mixin,
                "_radius": 100,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_radius,
        )

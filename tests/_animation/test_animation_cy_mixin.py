from random import randint

from retrying import retry

import apysc as ap
from apysc._animation.animation_cy_mixin import AnimationCyMixIn
from apysc._testing.testing_helper import assert_attrs
from apysc._testing.testing_helper import apply_test_settings


class TestAnimationCyMixIn:
    @apply_test_settings()
    def test_animation_y(self) -> None:
        mixin: AnimationCyMixIn = AnimationCyMixIn()
        mixin.variable_name = "test_animation_cy_mixin"
        animation_cy: ap.AnimationCy = mixin.animation_y(
            y=100, duration=1000, delay=500, easing=ap.Easing.EASE_OUT_QUINT
        )
        assert_attrs(
            expected_attrs={
                "_cy": 100,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_cy,
        )

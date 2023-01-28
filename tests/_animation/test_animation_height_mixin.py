from random import randint

from retrying import retry

import apysc as ap
from apysc._animation.animation_height_mixin import AnimationHeightMixIn
from apysc._testing.testing_helper import assert_attrs
from apysc._testing.testing_helper import apply_test_settings


class TestAnimationHeightMixIn:
    @apply_test_settings()
    def test_animation_height(self) -> None:
        mixin: AnimationHeightMixIn = AnimationHeightMixIn()
        mixin.variable_name = "test_animation_height_mixin"
        animation_height: ap.AnimationHeight = mixin.animation_height(
            height=100, duration=1000, delay=500, easing=ap.Easing.EASE_OUT_QUINT
        )
        assert_attrs(
            expected_attrs={
                "_target": mixin,
                "_height": 100,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_height,
        )

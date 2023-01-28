from random import randint

from retrying import retry

import apysc as ap
from apysc._animation.animation_cx_mixin import AnimationCxMixIn
from apysc._testing.testing_helper import assert_attrs
from apysc._testing.testing_helper import apply_test_settings


class TestAnimationCxMixIn:
    @apply_test_settings()
    def test_animation_x(self) -> None:
        mixin: AnimationCxMixIn = AnimationCxMixIn()
        mixin.variable_name = "test_animation_cx_mixin"
        animation_cx: ap.AnimationCx = mixin.animation_x(
            x=100, duration=1000, delay=500, easing=ap.Easing.EASE_OUT_QUINT
        )
        assert_attrs(
            expected_attrs={
                "_cx": 100,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_cx,
        )

        mixin.animation_x(x=100, duration=1000, easing=ap.Easing.EASE_OUT_QUINT)

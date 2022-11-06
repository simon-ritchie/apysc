from random import randint

from retrying import retry

import apysc as ap
from apysc._animation.animation_line_thickness_mixin import (
    AnimationLineThicknessMixIn,
)
from apysc._testing.testing_helper import assert_attrs


class TestAnimationLineThicknessMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_line_thickness_mixin(self) -> None:
        mixin: AnimationLineThicknessMixIn = AnimationLineThicknessMixIn()
        mixin.variable_name = "test_animation_line_thickness_mixin"
        animation_line_thickness: ap.AnimationLineThickness = (
            mixin.animation_line_thickness(
                thickness=3, duration=1000, delay=500, easing=ap.Easing.EASE_OUT_QUINT
            )
        )
        assert_attrs(
            expected_attrs={
                "_target": mixin,
                "_line_thickness": 3,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_line_thickness,
        )

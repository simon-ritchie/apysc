from random import randint

from retrying import retry

import apysc as ap
from apysc._animation.animation_move_mixin import AnimationMoveMixIn
from apysc._testing.testing_helper import assert_attrs
from apysc._testing.testing_helper import apply_test_settings


class TestAnimationMoveMixIn:
    @apply_test_settings()
    def test_animation_move(self) -> None:
        mixin: AnimationMoveMixIn = AnimationMoveMixIn()
        mixin.variable_name = "test_animation_move_mixin"
        animation_move: ap.AnimationMove = mixin.animation_move(
            x=100, y=200, duration=1000, delay=500, easing=ap.Easing.EASE_OUT_QUINT
        )
        assert_attrs(
            expected_attrs={
                "_x": 100,
                "_y": 200,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_move,
        )

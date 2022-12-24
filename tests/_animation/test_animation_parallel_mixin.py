from random import randint
from typing import List

from retrying import retry

import apysc as ap
from apysc._testing.testing_helper import assert_attrs


class TestAnimationParallelMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_parallel(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        animations: List[ap.AnimationBase] = [
            sprite.animation_x(x=100),
            sprite.animation_y(y=100),
        ]
        animation_parallel: ap.AnimationParallel = sprite.animation_parallel(
            animations=animations,
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT,
        )
        assert_attrs(
            expected_attrs={
                "_animations": animations,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_parallel,
        )
from random import randint
from typing import List

from retrying import retry

import apysc as ap
from apysc._expression import var_names
from apysc._animation.animation_base import AnimationBase


class TestAnimationParallel:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        rectangle: ap.Rectangle = sprite.graphics.draw_rect(
            x=50, y=50, width=50, height=50)
        animations: List[AnimationBase] = [
            rectangle.animation_x(x=100, duration=1000),
            rectangle.animation_fill_alpha(alpha=0.5, duration=1000),
        ]
        animation_parallel: ap.AnimationParallel = ap.AnimationParallel(
            animations=animations)
        assert animation_parallel.variable_name.startswith(
            f'{var_names.ANIMATION_PARALLEL}_')
        assert animation_parallel._animations == animations

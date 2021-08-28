from random import randint

from retrying import retry

import apysc as ap
from apysc._animation.animation_move_interface import AnimationMoveInterface
from tests.testing_helper import assert_attrs


class TestAnimationMoveInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_move(self) -> None:
        interface: AnimationMoveInterface = AnimationMoveInterface()
        interface.variable_name = 'test_animation_move_interface'
        animation_move: ap.AnimationMove = interface.animation_move(
            x=100, y=200, duration=1000, delay=500,
            easing=ap.Easing.EASE_OUT_QUINT)
        assert_attrs(
            expected_attrs={
                '_x': 100,
                '_y': 200,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_move)

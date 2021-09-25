from random import randint

from retrying import retry

import apysc as ap
from apysc._animation.animation_cy_interface import AnimationCyInterface
from tests.testing_helper import assert_attrs


class TestAnimationCyInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_y(self) -> None:
        interface: AnimationCyInterface = AnimationCyInterface()
        interface.variable_name = 'test_animation_cy_interface'
        animation_cy: ap.AnimationCy = interface.animation_y(
            y=100, duration=1000, delay=500, easing=ap.Easing.EASE_OUT_QUINT)
        assert_attrs(
            expected_attrs={
                '_cy': 100,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_cy)

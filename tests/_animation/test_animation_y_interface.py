from random import randint

from retrying import retry

import apysc as ap
from apysc._animation.animation_y_interface import AnimationYInterface
from tests.testing_helper import assert_attrs


class TestAnimationYInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_y(self) -> None:
        interface: AnimationYInterface = AnimationYInterface()
        interface.variable_name = 'test_animation_y_interface'
        animation_y: ap.AnimationY = interface.animation_y(
            y=100, duration=2000, delay=1000, easing=ap.Easing.EASE_OUT_QUINT)
        assert_attrs(
            expected_attrs={
                '_y': 100,
                '_duration': 2000,
                '_delay': 1000,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_y)

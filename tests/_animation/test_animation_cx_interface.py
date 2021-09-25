from random import randint

from retrying import retry

import apysc as ap
from apysc._animation.animation_cx_interface import AnimationCxInterface
from tests.testing_helper import assert_attrs


class TestAnimationCxInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_x(self) -> None:
        interface: AnimationCxInterface = AnimationCxInterface()
        interface.variable_name = 'test_animation_cx_interface'
        animation_cx: ap.AnimationCx = interface.animation_x(
            x=100, duration=1000, delay=500, easing=ap.Easing.EASE_OUT_QUINT)
        assert_attrs(
            expected_attrs={
                '_cx': 100,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_cx)

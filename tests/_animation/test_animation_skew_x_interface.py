from random import randint

from retrying import retry

import apysc as ap
from apysc._display.skew_x_interface import SkewXInterface
from tests.testing_helper import assert_attrs


class TestAnimationSkewXInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_skew_x_interface(self) -> None:
        interface: SkewXInterface = SkewXInterface()
        interface.variable_name = 'test_animation_skew_x_interface'
        animation_skew_x: ap.AnimationSkewX = interface.\
            animation_skew_x_interface(
                skew_x=100, duration=1000, delay=500,
                easing=ap.Easing.EASE_OUT_QUINT)
        assert_attrs(
            expected_attrs={
                '_target': interface,
                '_skew_x': 100,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_skew_x,
        )

from random import randint

from retrying import retry

import apysc as ap
from apysc._animation.animation_height_interface import \
    AnimationHeightInterface
from tests.testing_helper import assert_attrs


class TestAnimationHeightInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_height(self) -> None:
        interface: AnimationHeightInterface = AnimationHeightInterface()
        interface.variable_name = 'test_animation_height_interface'
        animation_height: ap.AnimationHeight = interface.animation_height(
            height=100, duration=1000, delay=500,
            easing=ap.Easing.EASE_OUT_QUINT)
        assert_attrs(
            expected_attrs={
                '_target': interface,
                '_height': 100,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_height,
        )

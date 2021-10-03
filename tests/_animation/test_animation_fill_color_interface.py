from random import randint

from retrying import retry

import apysc as ap
from apysc._animation.animation_fill_color_interface import \
    AnimationFillColorInterface
from tests.testing_helper import assert_attrs


class TestAnimationFillColorInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_fill_color(self) -> None:
        interface: AnimationFillColorInterface = AnimationFillColorInterface()
        interface.variable_name = 'test_animation_fill_color_interface'
        animation_fill_color: ap.AnimationFillColor = interface.\
            animation_fill_color(
                fill_color='0af',
                duration=1000, delay=500, easing=ap.Easing.EASE_OUT_QUINT)
        assert_attrs(
            expected_attrs={
                '_target': interface,
                '_fill_color': '#00aaff',
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_fill_color)

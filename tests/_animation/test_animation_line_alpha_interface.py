from random import randint

from retrying import retry

import apysc as ap
from apysc._animation.animation_line_alpha_interface import \
    AnimationLineAlphaInterface
from tests.testing_helper import assert_attrs


class TestAnimationLineAlphaInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_line_alpha(self) -> None:
        interface: AnimationLineAlphaInterface = AnimationLineAlphaInterface()
        interface.variable_name = 'test_animation_line_alpha_interface'
        animation_line_alpha: ap.AnimationLineAlpha = interface.\
            animation_line_alpha(
                alpha=0.5, duration=1000, delay=500,
                easing=ap.Easing.EASE_OUT_QUINT)
        assert_attrs(
            expected_attrs={
                '_target': interface,
                '_line_alpha': 0.5,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_line_alpha)

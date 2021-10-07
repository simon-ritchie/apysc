from random import randint

from retrying import retry

import apysc as ap
from apysc._animation.animation_line_color_interface import \
    AnimationLineColorInterface
from tests.testing_helper import assert_attrs


class TestAnimationLineColorInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_line_color(self) -> None:
        interface: AnimationLineColorInterface = AnimationLineColorInterface()
        interface.variable_name = 'test_animation_line_color_interface'
        animation_line_color: ap.AnimationLineColor = interface.\
            animation_line_color(
                line_color='0af', duration=1000, delay=500,
                easing=ap.Easing.EASE_OUT_QUINT)
        assert_attrs(
            expected_attrs={
                '_target': interface,
                '_line_color': '#00aaff',
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_line_color,
        )

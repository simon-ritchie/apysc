from random import randint

from retrying import retry

import apysc as ap
from apysc._animation.animation_line_thickness_interface import \
    AnimationLineThicknessInterface
from tests.testing_helper import assert_attrs


class TestAnimationLineThicknessInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_line_thickness_interface(self) -> None:
        interface: AnimationLineThicknessInterface = \
            AnimationLineThicknessInterface()
        interface.variable_name = 'test_animation_line_thickness_interface'
        animation_line_thickness: ap.AnimationLineThickness = interface.\
            animation_line_thickness(
                thickness=3,
                duration=1000,
                delay=500,
                easing=ap.Easing.EASE_OUT_QUINT)
        assert_attrs(
            expected_attrs={
                '_target': interface,
                '_line_thickness': 3,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_line_thickness)

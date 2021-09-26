from random import randint

from retrying import retry

import apysc as ap
from apysc._animation.animation_ellipse_width_interface import \
    AnimationEllipseWidthInterface
from tests.testing_helper import assert_attrs


class TestAnimationEllipseWidthInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_ellipse_width(self) -> None:
        interface: AnimationEllipseWidthInterface = \
            AnimationEllipseWidthInterface()
        interface.variable_name = 'test_animation_ellipse_width_interface'
        animation_ellipse_width: ap.AnimationEllipseWidth = \
            interface.animation_ellipse_width(
                ellipse_width=100, duration=1000, delay=500,
                easing=ap.Easing.EASE_OUT_QUINT)
        assert_attrs(
            expected_attrs={
                '_target': interface,
                '_ellipse_width': 100,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_ellipse_width)

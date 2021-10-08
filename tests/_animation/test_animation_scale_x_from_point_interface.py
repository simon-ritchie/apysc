from random import randint

from retrying import retry

import apysc as ap
from apysc._display.scale_x_from_point_interface import \
    ScaleXFromPointInterface
from tests.testing_helper import assert_attrs


class TestAnimationScaleXFromPointInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_scale_x_from_point(self) -> None:
        interface: ScaleXFromPointInterface = ScaleXFromPointInterface()
        animation: ap.AnimationScaleXFromPoint = interface.\
            animation_scale_x_from_point(
                scale_x_from_point=2.0,
                x=50,
                duration=1000,
                delay=500,
                easing=ap.Easing.EASE_OUT_QUINT)
        assert_attrs(
            expected_attrs={
                '_target': interface,
                '_scale_x_from_point': 2.0,
                '_x': 50,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation)

from random import randint

from retrying import retry

import apysc as ap
from apysc._display.scale_x_from_center_interface import \
    ScaleXFromCenterInterface
from tests.testing_helper import assert_attrs


class TestAnimationScaleXFromCenterInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_scale_x_from_center(self) -> None:
        interface: ScaleXFromCenterInterface = ScaleXFromCenterInterface()
        interface.variable_name = 'test_animation_scale_x_from_center'
        animation: ap.AnimationScaleXFromCenter = interface.\
            animation_scale_x_from_center(
                scale_x_from_center=2.0, duration=1000, delay=500,
                easing=ap.Easing.EASE_OUT_QUINT)
        assert_attrs(
            expected_attrs={
                '_target': interface,
                '_scale_x_from_center': 2.0,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation,
        )

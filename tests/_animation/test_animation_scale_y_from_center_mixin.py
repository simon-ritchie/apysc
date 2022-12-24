from random import randint

from retrying import retry

import apysc as ap
from apysc._display.scale_y_from_center_mixin import ScaleYFromCenterMixIn
from apysc._testing.testing_helper import assert_attrs


class TestAnimationScaleYFromCenterMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_scale_y_from_center(self) -> None:
        interface: ScaleYFromCenterMixIn = ScaleYFromCenterMixIn()
        interface.variable_name = "test_animation_scale_y_from_center_interface"
        animation: ap.AnimationScaleYFromCenter = (
            interface.animation_scale_y_from_center(
                scale_y_from_center=2.0,
                duration=1000,
                delay=500,
                easing=ap.Easing.EASE_OUT_QUINT,
            )
        )
        assert_attrs(
            expected_attrs={
                "_target": interface,
                "_scale_y_from_center": 2.0,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation,
        )
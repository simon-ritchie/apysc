from random import randint

from retrying import retry

import apysc as ap
from apysc._display.scale_x_from_point_mixin import ScaleXFromPointMixIn
from apysc._testing.testing_helper import assert_attrs
from apysc._testing.testing_helper import apply_test_settings


class TestAnimationScaleXFromPointMixIn:
    @apply_test_settings()
    def test_animation_scale_x_from_point(self) -> None:
        interface: ScaleXFromPointMixIn = ScaleXFromPointMixIn()
        animation: ap.AnimationScaleXFromPoint = interface.animation_scale_x_from_point(
            scale_x_from_point=2.0,
            x=50,
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT,
        )
        assert_attrs(
            expected_attrs={
                "_target": interface,
                "_scale_x_from_point": 2.0,
                "_x": 50,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation,
        )

from random import randint

from retrying import retry

import apysc as ap
from apysc._animation.animation_fill_color_mixin import AnimationFillColorMixIn
from apysc._testing.testing_helper import assert_attrs
from apysc._testing.testing_helper import apply_test_settings


class TestAnimationFillColorMixIn:
    @apply_test_settings()
    def test_animation_fill_color(self) -> None:
        interface: AnimationFillColorMixIn = AnimationFillColorMixIn()
        interface.variable_name = "test_animation_fill_color_interface"
        animation_fill_color: ap.AnimationFillColor = interface.animation_fill_color(
            fill_color="0af", duration=1000, delay=500, easing=ap.Easing.EASE_OUT_QUINT
        )
        assert_attrs(
            expected_attrs={
                "_target": interface,
                "_fill_color": "#00aaff",
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_fill_color,
        )

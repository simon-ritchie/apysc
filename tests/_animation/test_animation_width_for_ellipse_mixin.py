import apysc as ap
from apysc._animation.animation_width_for_ellipse_mixin import (
    AnimationWidthForEllipseMixIn,
)
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs


class TestAnimationWidthForEllipseMixIn:
    @apply_test_settings()
    def test_animation_width(self) -> None:
        interface: AnimationWidthForEllipseMixIn = AnimationWidthForEllipseMixIn()
        interface.variable_name = "test_animation_width_for_ellipse_interface"
        animation_width_for_ellipse: ap.AnimationWidthForEllipse = (
            interface.animation_width(
                width=100, duration=1000, delay=500, easing=ap.Easing.EASE_OUT_QUINT
            )
        )
        assert_attrs(
            expected_attrs={
                "_target": interface,
                "_width": 100,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_width_for_ellipse,
        )

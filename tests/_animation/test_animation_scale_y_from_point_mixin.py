import apysc as ap
from apysc._display.scale_y_from_point_mixin import ScaleYFromPointMixIn
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs


class TestAnimationScaleYFromPointMixIn:
    @apply_test_settings()
    def test_animation_scale_y_from_point(self) -> None:
        interface: ScaleYFromPointMixIn = ScaleYFromPointMixIn()
        interface.variable_name = "test_animation_scale_y_from_point_interface"
        animation: ap.AnimationScaleYFromPoint = interface.animation_scale_y_from_point(
            scale_y_from_point=2.0,
            y=100,
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT,
        )
        assert_attrs(
            expected_attrs={
                "_target": interface,
                "_scale_y_from_point": 2.0,
                "_y": 100,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation,
        )

import apysc as ap
from apysc._animation.animation_fill_alpha_mixin import AnimationFillAlphaMixIn
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs


class TestAnimationFillAlphaMixIn:
    @apply_test_settings()
    def test_animation_fill_alpha(self) -> None:
        interface: AnimationFillAlphaMixIn = AnimationFillAlphaMixIn()
        interface.variable_name = "test_animation_fill_alpha_interface"
        animation_fill_alpha: ap.AnimationFillAlpha = interface.animation_fill_alpha(
            alpha=0.5, duration=1000, delay=500, easing=ap.Easing.EASE_OUT_QUINT
        )
        assert_attrs(
            expected_attrs={
                "_target": interface,
                "_fill_alpha": 0.5,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_fill_alpha,
        )

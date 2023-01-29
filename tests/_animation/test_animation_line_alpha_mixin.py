import apysc as ap
from apysc._animation.animation_line_alpha_mixin import AnimationLineAlphaMixIn
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs


class TestAnimationLineAlphaMixIn:
    @apply_test_settings()
    def test_animation_line_alpha(self) -> None:
        mixin: AnimationLineAlphaMixIn = AnimationLineAlphaMixIn()
        mixin.variable_name = "test_animation_line_alpha_mixin"
        animation_line_alpha: ap.AnimationLineAlpha = mixin.animation_line_alpha(
            alpha=0.5, duration=1000, delay=500, easing=ap.Easing.EASE_OUT_QUINT
        )
        assert_attrs(
            expected_attrs={
                "_target": mixin,
                "_line_alpha": 0.5,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_line_alpha,
        )

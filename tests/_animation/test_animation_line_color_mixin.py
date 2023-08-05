import apysc as ap
from apysc._animation.animation_line_color_mixin import AnimationLineColorMixIn
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs


class TestAnimationLineColorMixIn:
    @apply_test_settings()
    def test_animation_line_color(self) -> None:
        mixin: AnimationLineColorMixIn = AnimationLineColorMixIn()
        mixin.variable_name = "test_animation_line_color_mixin"
        animation_line_color: ap.AnimationLineColor = mixin.animation_line_color(
            line_color=ap.Color("0af"),
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT,
        )
        assert_attrs(
            expected_attrs={
                "_target": mixin,
                "_line_color": ap.Color("#00aaff"),
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_line_color,
        )

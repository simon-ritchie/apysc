from apysc._animation.animation_play_mixin import AnimationPlayMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
import apysc as ap


class TestAnimationPlayMixIn:
    @apply_test_settings()
    def test_animation_play(self) -> None:
        ap.Stage()
        mixin: AnimationPlayMixIn = AnimationPlayMixIn()
        mixin.variable_name = "test_animation_play_mixin"
        mixin.animation_play()
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin.variable_name}.timeline().play();"
        assert expected in expression

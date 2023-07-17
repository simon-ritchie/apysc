from apysc._animation.animation_reset_mixin import AnimationResetMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
import apysc as ap


class TestAnimationResetMixIn:
    @apply_test_settings()
    def test_animation_reset(self) -> None:
        mixin: AnimationResetMixIn = AnimationResetMixIn()
        mixin.variable_name = "test_animation_reset_mixin"
        mixin.animation_reset()
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin.variable_name}.timeline().stop();"
        assert expected in expression

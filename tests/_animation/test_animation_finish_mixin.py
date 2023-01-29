from apysc._animation.animation_finish_mixin import AnimationFinishMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestAnimationFinishMixIn:
    @apply_test_settings()
    def test_animation_finish(self) -> None:
        expression_data_util.empty_expression()
        mixin: AnimationFinishMixIn = AnimationFinishMixIn()
        mixin.variable_name = "test_animation_finish_mixin"
        mixin.animation_finish()
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin.variable_name}.timeline().finish();"
        assert expected in expression

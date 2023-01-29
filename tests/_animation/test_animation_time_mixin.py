import apysc as ap
from apysc._animation.animation_time_mixin import AnimationTimeMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestAnimationTimeMixIn:
    @apply_test_settings()
    def test_animation_time(self) -> None:
        expression_data_util.empty_expression()
        mixin: AnimationTimeMixIn = AnimationTimeMixIn()
        mixin.variable_name = "test_animation_time_mixin"

        elapsed_time: ap.Number = mixin.animation_time()
        assert elapsed_time == 0.0
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{elapsed_time.variable_name} = "
            f"{mixin.variable_name}.timeline().time();"
        )
        assert expected in expression

from random import randint

from retrying import retry

from apysc._animation.animation_reset_mixin import AnimationResetMixIn
from apysc._expression import expression_data_util


class TestAnimationResetMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_reset(self) -> None:
        expression_data_util.empty_expression()
        mixin: AnimationResetMixIn = AnimationResetMixIn()
        mixin.variable_name = "test_animation_reset_mixin"
        mixin.animation_reset()
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin.variable_name}.timeline().stop();"
        assert expected in expression

from random import randint

from retrying import retry

from apysc._animation.animation_reverse_mixin import AnimationReverseMixIn
from apysc._expression import expression_data_util


class TestAnimationReverseMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_reverse(self) -> None:
        expression_data_util.empty_expression()
        mixin: AnimationReverseMixIn = AnimationReverseMixIn()
        mixin.variable_name = "test_animation_reverse_mixin"
        mixin.animation_reverse()
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin.variable_name}.timeline().reverse();"
        assert expected in expression

from random import randint

from retrying import retry

from apysc._animation.animation_play_mixin import AnimationPlayMixIn
from apysc._expression import expression_data_util


class TestAnimationPlayMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_play(self) -> None:
        expression_data_util.empty_expression()
        mixin: AnimationPlayMixIn = AnimationPlayMixIn()
        mixin.variable_name = "test_animation_play_mixin"
        mixin.animation_play()
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin.variable_name}.timeline().play();"
        assert expected in expression

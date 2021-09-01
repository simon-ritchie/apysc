from random import randint

from retrying import retry

from apysc._animation.animation_reset_interface import AnimationResetInterface
from apysc._expression import expression_data_util


class TestAnimationResetInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_reset(self) -> None:
        expression_data_util.empty_expression()
        interface: AnimationResetInterface = AnimationResetInterface()
        interface.variable_name = 'test_animation_reset_interface'
        interface.animation_reset()
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.timeline().stop();'
        )
        assert expected in expression

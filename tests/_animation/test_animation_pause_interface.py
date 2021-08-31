from random import randint

from retrying import retry

from apysc._animation.animation_pause_interface import AnimationPauseInterface
from apysc._expression import expression_data_util


class TestAnimationPauseInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_pause(self) -> None:
        expression_data_util.empty_expression()
        interface: AnimationPauseInterface = AnimationPauseInterface()
        interface.variable_name = 'test_animation_pause_interface'
        interface.animation_pause()
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.timeline().pause();'
        )
        assert expected in expression

from random import randint

from retrying import retry

from apysc._animation.animation_finish_interface import \
    AnimationFinishInterface
from apysc._expression import expression_data_util


class TestAnimationFinishInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_finish(self) -> None:
        expression_data_util.empty_expression()
        interface: AnimationFinishInterface = AnimationFinishInterface()
        interface.variable_name = 'test_animation_finish_interface'
        interface.animation_finish()
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.timeline().finish();'
        )
        assert expected in expression

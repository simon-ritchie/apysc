from random import randint

from retrying import retry

from apysc._animation.animation_reverse_interface import \
    AnimationReverseInterface
from apysc._expression import expression_data_util


class TestAnimationReverseInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_reverse(self) -> None:
        expression_data_util.empty_expression()
        interface: AnimationReverseInterface = AnimationReverseInterface()
        interface.variable_name = 'test_animation_reverse_interface'
        interface.animation_reverse()
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.timeline().reverse();'
        )
        assert expected in expression

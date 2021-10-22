from random import randint

from retrying import retry

import apysc as ap
from apysc._animation.animation_time_interface import AnimationTimeInterface
from apysc._expression import expression_data_util


class TestAnimationTimeInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_time(self) -> None:
        expression_data_util.empty_expression()
        interface: AnimationTimeInterface = AnimationTimeInterface()
        interface.variable_name = 'test_animation_time_interface'

        elapsed_time: ap.Number = interface.animation_time()
        assert elapsed_time == 0.0
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{elapsed_time.variable_name} = '
            f'{interface.variable_name}.timeline().time();'
        )
        assert expected in expression

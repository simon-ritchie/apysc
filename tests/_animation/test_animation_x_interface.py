from random import randint

from retrying import retry

import apysc as ap
from apysc._animation.animation_x_interface import AnimationXInterface
from apysc._expression import expression_data_util
from tests.testing_helper import assert_attrs


class TestAnimationXInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_x(self) -> None:
        expression_data_util.empty_expression()
        interface: AnimationXInterface = AnimationXInterface()
        interface.variable_name = 'test_animation_x_interface'
        animation_x: ap.AnimationX = interface.animation_x(
            x=100, duration=1000, delay=500, easing=ap.Easing.EASE_OUT_QUINT)
        animation_x.start()
        assert_attrs(
            expected_attrs={
                '_x': 100,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_x)
        expression: str = expression_data_util.get_current_expression()
        assert f'\n  .x({animation_x._x.variable_name});' in expression

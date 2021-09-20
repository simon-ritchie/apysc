from random import randint

from retrying import retry

import apysc as ap
from apysc._type.variable_name_interface import VariableNameInterface
from apysc._expression import var_names
from tests.testing_helper import assert_attrs


class TestAnimationX:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        interface: VariableNameInterface = VariableNameInterface()
        interface.variable_name = 'test_animation_x'
        animation_x: ap.AnimationX = ap.AnimationX(
            target=interface, x=100, duration=1000, delay=500,
            easing=ap.Easing.EASE_OUT_QUINT)
        assert_attrs(
            expected_attrs={
                '_x': 100,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_x)
        assert animation_x.variable_name.startswith(
            f'{var_names.ANIMATION_X}_')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        interface: VariableNameInterface = VariableNameInterface()
        interface.variable_name = 'test_animation_x'
        animation_x: ap.AnimationX = ap.AnimationX(
            target=interface, x=100, duration=1000, delay=500,
            easing=ap.Easing.EASE_OUT_QUINT)
        expression: str = animation_x._get_animation_func_expression()
        expected: str = (
            f'\n  .x({animation_x._x.variable_name});'
        )
        assert expression == expected

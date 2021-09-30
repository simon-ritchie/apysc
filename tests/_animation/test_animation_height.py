from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import var_names
from apysc._type.variable_name_interface import VariableNameInterface
from tests.testing_helper import assert_attrs


class TestAnimationHeight:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_height'
        animation_height: ap.AnimationHeight = ap.AnimationHeight(
            target=target, height=100, duration=1000, delay=500,
            easing=ap.Easing.EASE_OUT_QUINT)
        assert animation_height.variable_name.startswith(
            f'{var_names.ANIMATION_HEIGHT}_')
        assert_attrs(
            expected_attrs={
                '_target': target,
                '_height': 100,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_height)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_height'
        animation_height: ap.AnimationHeight = ap.AnimationHeight(
            target=target, height=100)
        expression: str = animation_height._get_animation_func_expression()
        assert expression == (
            f'\n  .height({animation_height._height.variable_name});')

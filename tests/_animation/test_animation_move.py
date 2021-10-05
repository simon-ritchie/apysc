from random import randint

from retrying import retry

import apysc as ap
from apysc._display.x_interface import XInterface
from apysc._display.y_interface import YInterface
from apysc._type.variable_name_interface import VariableNameInterface


class _TestInterface(XInterface, YInterface):
    pass


class TestAnimationMove:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_move_interface'
        animation_move: ap.AnimationMove = ap.AnimationMove(
            target=target,
            x=100,
            y=200,
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT)
        assert animation_move._x == 100
        assert isinstance(animation_move._x, ap.Int)
        assert animation_move._y == 200
        assert isinstance(animation_move._y, ap.Int)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_move_interface'
        animation_move: ap.AnimationMove = ap.AnimationMove(
            target=target,
            x=100,
            y=200,
            duration=1000)
        expression: str = animation_move._get_animation_func_expression()
        expected: str = (
            f'\n  .move({animation_move._x.variable_name}, '
            f'{animation_move._y.variable_name});'
        )
        assert expression == expected

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_complete_event_in_handler_head_expression(self) -> None:
        target: _TestInterface = _TestInterface()
        target.variable_name = 'test_animation_move_interface'
        animation_move: ap.AnimationMove = ap.AnimationMove(
            target=target, x=100, y=200)
        expression: str = animation_move.\
            _get_complete_event_in_handler_head_expression()
        assert expression == (
            f'{target._x.variable_name} = '
            f'{animation_move._x.variable_name};'
            f'\n{target._y.variable_name} = '
            f'{animation_move._y.variable_name};'
        )

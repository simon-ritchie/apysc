from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import var_names
from apysc._type.variable_name_interface import VariableNameInterface
from apysc._display.x_interface import XInterface
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

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: VariableNameInterface = VariableNameInterface()
        interface.variable_name = 'test_animation_x'
        animation_x: ap.AnimationX = ap.AnimationX(
            target=interface, x=100, duration=1000, delay=500,
            easing=ap.Easing.EASE_OUT_QUINT)
        snapshot_name: str = animation_x._get_next_snapshot_name()
        animation_x._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert animation_x._x_snapshots[snapshot_name] == 100

        animation_x._x._value = 200
        animation_x._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert animation_x._x_snapshots[snapshot_name] == 100

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: VariableNameInterface = VariableNameInterface()
        interface.variable_name = 'test_animation_x'
        animation_x: ap.AnimationX = ap.AnimationX(
            target=interface, x=100, duration=1000, delay=500,
            easing=ap.Easing.EASE_OUT_QUINT)
        snapshot_name: str = animation_x._get_next_snapshot_name()
        animation_x._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        animation_x._x._value = 200
        animation_x._run_all_revert_methods(snapshot_name=snapshot_name)
        assert animation_x._x == 100

        animation_x._x._value = 200
        animation_x._run_all_revert_methods(snapshot_name=snapshot_name)
        assert animation_x._x == 200

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_complete_event_in_handler_head_expression(self) -> None:
        target: XInterface = XInterface()
        target.variable_name = 'test_animation_x'
        animation_x: ap.AnimationX = ap.AnimationX(target=target, x=100)
        expression: str = animation_x.\
            _get_complete_event_in_handler_head_expression()
        assert expression == (
            f'{target._x.variable_name} = '
            f'{animation_x._x.variable_name};'
        )

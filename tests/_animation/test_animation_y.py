from random import randint

from retrying import retry

import apysc as ap
from apysc._animation.animation_y import AnimationY
from apysc._type.variable_name_interface import VariableNameInterface
from tests.testing_helper import assert_attrs


class TestAnimationY:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_y'
        animation_y: AnimationY = AnimationY(
            target=target, y=100, duration=2000, delay=1000,
            easing=ap.Easing.EASE_OUT_QUINT)
        assert_attrs(
            expected_attrs={
                '_target': target,
                '_y': 100,
                '_duration': 2000,
                '_delay': 1000,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_y)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_y'
        animation_y: AnimationY = AnimationY(target=target, y=100)
        expression: str = animation_y._get_animation_func_expression()
        assert expression == f'\n  .y({animation_y._y.variable_name});'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_y'
        animation_y: AnimationY = AnimationY(target=target, y=100)
        snapshot_name: str = animation_y._get_next_snapshot_name()
        animation_y._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert animation_y._y_snapshots[snapshot_name] == 100

        animation_y._y.value = 200
        animation_y._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert animation_y._y_snapshots[snapshot_name] == 100

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_y'
        animation_y: AnimationY = AnimationY(target=target, y=100)
        snapshot_name: str = animation_y._get_next_snapshot_name()
        animation_y._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        animation_y._y.value = 200
        animation_y._run_all_revert_methods(snapshot_name=snapshot_name)
        assert animation_y._y == 100

        animation_y._y.value = 200
        animation_y._run_all_revert_methods(snapshot_name=snapshot_name)
        assert animation_y._y == 200

from random import randint

from retrying import retry

import apysc as ap
from apysc._animation.animation_cy import AnimationCy
from apysc._expression import var_names
from apysc._type.variable_name_interface import VariableNameInterface
from tests.testing_helper import assert_attrs


class TestAnimationCy:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_cy'
        animation_cy: AnimationCy = AnimationCy(
            target=target, y=100, duration=1000, delay=500,
            easing=ap.Easing.EASE_OUT_QUINT)
        assert animation_cy.variable_name.startswith(
            f'{var_names.ANIMATION_CY}_')
        assert_attrs(
            expected_attrs={
                '_target': target,
                '_cy': 100,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_cy)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_cy'
        animation_cy: AnimationCy = AnimationCy(
            target=target, y=100)
        expression: str = animation_cy._get_animation_func_expression()
        assert expression == f'\n  .cy({animation_cy._cy.variable_name});'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_cy'
        animation_cy: AnimationCy = AnimationCy(
            target=target, y=100)
        snapshot_name: str = animation_cy._get_next_snapshot_name()
        animation_cy._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert animation_cy._cy_snapshots[snapshot_name] == 100

        animation_cy._cy.value = 200
        animation_cy._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert animation_cy._cy_snapshots[snapshot_name] == 100

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_cy'
        animation_cy: AnimationCy = AnimationCy(
            target=target, y=100)
        snapshot_name: str = animation_cy._get_next_snapshot_name()
        animation_cy._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        animation_cy._cy.value = 200
        animation_cy._run_all_revert_methods(snapshot_name=snapshot_name)
        assert animation_cy._cy == 100

        animation_cy._cy.value = 200
        animation_cy._run_all_revert_methods(snapshot_name=snapshot_name)
        assert animation_cy._cy == 200

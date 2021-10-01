from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import var_names
from apysc._type.variable_name_interface import VariableNameInterface
from apysc._display.cx_interface import CxInterface
from tests.testing_helper import assert_attrs


class TestAnimationCx:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_cx'
        animation_cx: ap.AnimationCx = ap.AnimationCx(
            target=target,
            x=100,
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT,
        )
        assert animation_cx.variable_name.startswith(
            f'{var_names.ANIMATION_CX}_')
        assert_attrs(
            expected_attrs={
                '_target': target,
                '_cx': 100,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_cx,
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_cx'
        animation_cx: ap.AnimationCx = ap.AnimationCx(
            target=target, x=100,
        )
        expression: str = animation_cx._get_animation_func_expression()
        assert expression == f'\n  .cx({animation_cx._cx.variable_name});'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_cx'
        animation_cx: ap.AnimationCx = ap.AnimationCx(
            target=target, x=100,
        )
        snapshot_name: str = animation_cx._get_next_snapshot_name()
        animation_cx._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert animation_cx._cx_snapshots[snapshot_name] == 100

        animation_cx._cx.value = 200
        animation_cx._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert animation_cx._cx_snapshots[snapshot_name] == 100

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_cx'
        animation_cx: ap.AnimationCx = ap.AnimationCx(
            target=target, x=100,
        )
        snapshot_name: str = animation_cx._get_next_snapshot_name()
        animation_cx._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        animation_cx._cx.value = 200
        animation_cx._run_all_revert_methods(snapshot_name=snapshot_name)
        assert animation_cx._cx == 100

        animation_cx._cx.value = 200
        animation_cx._run_all_revert_methods(snapshot_name=snapshot_name)
        assert animation_cx._cx == 200

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_complete_event_in_handler_head_expression(self) -> None:
        target_1: VariableNameInterface = VariableNameInterface()
        target_1.variable_name = 'test_animation_cx'
        animation_cx: ap.AnimationCx = ap.AnimationCx(
            target=target_1, x=100,
        )
        expression: str = animation_cx.\
            _get_complete_event_in_handler_head_expression()
        assert expression == ''

        target_2: CxInterface = CxInterface()
        target_2.variable_name = 'test_animation_cx'
        animation_cx = ap.AnimationCx(target=target_2, x=100)
        expression = animation_cx.\
            _get_complete_event_in_handler_head_expression()
        expected: str = (
            f'{target_2._cx.variable_name} = '
            f'{animation_cx._cx.variable_name};'
        )
        assert expression == expected

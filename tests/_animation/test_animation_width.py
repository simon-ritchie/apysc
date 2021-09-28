from random import randint

from retrying import retry

import apysc as ap
from apysc._type.variable_name_interface import VariableNameInterface
from apysc._expression import var_names
from tests.testing_helper import assert_attrs


class TestAnimationWidth:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_width'
        animation_width: ap.AnimationWidth = ap.AnimationWidth(
            target=target, width=100, duration=1000, delay=500,
            easing=ap.Easing.EASE_OUT_QUINT)
        assert animation_width.variable_name.startswith(
            f'{var_names.ANIMATION_WIDTH}_')
        assert_attrs(
            expected_attrs={
                '_target': target,
                '_width': 100,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_width)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_width'
        animation_width: ap.AnimationWidth = ap.AnimationWidth(
            target=target, width=100)
        expression: str = animation_width._get_animation_func_expression()
        assert expression == \
            f'\n  .width({animation_width._width.variable_name});'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_width'
        animation_width: ap.AnimationWidth = ap.AnimationWidth(
            target=target, width=100)
        snapshot_name: str = animation_width._get_next_snapshot_name()
        animation_width._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert animation_width._width_snapshots[snapshot_name] == 100

        animation_width._width.value = 200
        animation_width._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert animation_width._width_snapshots[snapshot_name] == 100

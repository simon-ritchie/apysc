from random import randint

from retrying import retry

import apysc as ap
from apysc._type.variable_name_interface import VariableNameInterface
from apysc._expression import var_names
from tests.testing_helper import assert_attrs


class TestAnimationFillAlpha:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_fill_alpha'
        animation_fill_alpha: ap.AnimationFillAlpha = ap.AnimationFillAlpha(
            target=target, alpha=0.5, duration=1000, delay=500,
            easing=ap.Easing.EASE_OUT_QUINT)
        assert animation_fill_alpha.variable_name.startswith(
            f'{var_names.ANIMATION_FILL_ALPHA}_')
        assert_attrs(
            expected_attrs={
                '_target': target,
                '_fill_alpha': 0.5,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_fill_alpha)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_fill_alpha'
        animation_fill_alpha: ap.AnimationFillAlpha = ap.AnimationFillAlpha(
            target=target, alpha=0.5)
        expression: str = \
            animation_fill_alpha._get_animation_func_expression()
        assert expression == (
            '\n  .attr({"fill-opacity": '
            f'{animation_fill_alpha._fill_alpha.variable_name}}});')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_fill_alpha'
        animation_fill_alpha: ap.AnimationFillAlpha = ap.AnimationFillAlpha(
            target=target, alpha=0.5)
        snapshot_name: str = animation_fill_alpha._get_next_snapshot_name()
        animation_fill_alpha._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert animation_fill_alpha._fill_alpha_snapshots[
            snapshot_name] == 0.5

        animation_fill_alpha._fill_alpha.value = 0.3
        animation_fill_alpha._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert animation_fill_alpha._fill_alpha_snapshots[
            snapshot_name] == 0.5

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_fill_alpha'
        animation_fill_alpha: ap.AnimationFillAlpha = ap.AnimationFillAlpha(
            target=target, alpha=0.5)
        snapshot_name: str = animation_fill_alpha._get_next_snapshot_name()
        animation_fill_alpha._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        animation_fill_alpha._fill_alpha.value = 0.3
        animation_fill_alpha._run_all_revert_methods(
            snapshot_name=snapshot_name)
        assert animation_fill_alpha._fill_alpha == 0.5

        animation_fill_alpha._fill_alpha.value = 0.3
        animation_fill_alpha._run_all_revert_methods(
            snapshot_name=snapshot_name)
        assert animation_fill_alpha._fill_alpha == 0.3

from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import var_names
from apysc._type.variable_name_interface import VariableNameInterface
from tests.testing_helper import assert_attrs


class TestAnimationWidthForEllipse:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_width_for_ellipse'
        animation_width_for_ellipse: ap.AnimationWidthForEllipse = \
            ap.AnimationWidthForEllipse(
                target=target,
                width=100,
                duration=1000,
                delay=500,
                easing=ap.Easing.EASE_OUT_QUINT)
        assert animation_width_for_ellipse.variable_name.startswith(
            f'{var_names.ANIMATION_WIDTH_FOR_ELLIPSE}_')
        assert_attrs(
            expected_attrs={
                '_target': target,
                '_width': 100,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_width_for_ellipse,
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_width_for_ellipse'
        animation_width_for_ellipse: ap.AnimationWidthForEllipse = \
            ap.AnimationWidthForEllipse(target=target, width=100)
        expression: str = \
            animation_width_for_ellipse._get_animation_func_expression()
        assert expression == (
            '\n  .attr({rx: parseInt('
            f'{animation_width_for_ellipse._width.variable_name} / 2)}});')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_width_for_ellipse'
        animation_width_for_ellipse: ap.AnimationWidthForEllipse = \
            ap.AnimationWidthForEllipse(target=target, width=100)
        snapshot_name: str = \
            animation_width_for_ellipse._get_next_snapshot_name()
        animation_width_for_ellipse._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert animation_width_for_ellipse._width_snapshots[
            snapshot_name] == 100

        animation_width_for_ellipse._width.value = 200
        animation_width_for_ellipse._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert animation_width_for_ellipse._width_snapshots[
            snapshot_name] == 100

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_width_for_ellipse'
        animation_width_for_ellipse: ap.AnimationWidthForEllipse = \
            ap.AnimationWidthForEllipse(target=target, width=100)
        snapshot_name: str = animation_width_for_ellipse.\
            _get_next_snapshot_name()
        animation_width_for_ellipse._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        animation_width_for_ellipse._width.value = 200
        animation_width_for_ellipse._run_all_revert_methods(
            snapshot_name=snapshot_name)
        assert animation_width_for_ellipse._width == 100

        animation_width_for_ellipse._width.value = 200
        animation_width_for_ellipse._run_all_revert_methods(
            snapshot_name=snapshot_name)
        assert animation_width_for_ellipse._width == 200

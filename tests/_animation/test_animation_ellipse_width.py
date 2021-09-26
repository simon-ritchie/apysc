from random import randint

from retrying import retry

import apysc as ap
from apysc._type.variable_name_interface import VariableNameInterface
from apysc._expression import var_names
from tests.testing_helper import assert_attrs


class TestAnimationEllipseWidth:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_ellipse_width'
        animation_ellipse_width: ap.AnimationEllipseWidth = \
            ap.AnimationEllipseWidth(
                target=target,
                ellipse_width=100,
                duration=1000,
                delay=500,
                easing=ap.Easing.EASE_OUT_QUINT)
        assert animation_ellipse_width.variable_name.startswith(
            f'{var_names.ANIMATION_ELLIPSE_WIDTH}_')
        assert_attrs(
            expected_attrs={
                '_target': target,
                '_ellipse_width': 100,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_ellipse_width,
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_ellipse_width'
        animation_ellipse_width: ap.AnimationEllipseWidth = \
            ap.AnimationEllipseWidth(target=target, ellipse_width=100)
        expression: str = \
            animation_ellipse_width._get_animation_func_expression()
        assert expression == (
            '\n  .attr({rx: '
            f'{animation_ellipse_width._ellipse_width.variable_name}}});')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_ellipse_width'
        animation_ellipse_width: ap.AnimationEllipseWidth = \
            ap.AnimationEllipseWidth(target=target, ellipse_width=100)
        snapshot_name: str = animation_ellipse_width._get_next_snapshot_name()
        animation_ellipse_width._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert animation_ellipse_width._ellipse_width_snapshots[
            snapshot_name] == 100

        animation_ellipse_width._ellipse_width.value = 200
        animation_ellipse_width._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert animation_ellipse_width._ellipse_width_snapshots[
            snapshot_name] == 100

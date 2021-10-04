from random import randint

from retrying import retry

import apysc as ap
from apysc._display.radius_interface import RadiusInterface
from apysc._expression import var_names
from tests.testing_helper import assert_attrs


class TestAnimationRadius:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target: RadiusInterface = RadiusInterface()
        target.variable_name = 'test_radius_interface'
        animation_radius: ap.AnimationRadius = ap.AnimationRadius(
            target=target, radius=100, duration=1000,
            delay=500, easing=ap.Easing.EASE_OUT_QUINT)
        assert animation_radius.variable_name.startswith(
            f'{var_names.ANIMATION_RADIUS}_')
        assert_attrs(
            expected_attrs={
                '_target': target,
                '_radius': 100,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_radius)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        target: RadiusInterface = RadiusInterface()
        target.variable_name = 'test_radius_interface'
        animation_radius: ap.AnimationRadius = ap.AnimationRadius(
            target=target, radius=100)
        expression: str = animation_radius._get_animation_func_expression()
        assert expression == (
            f'\n  .attr({{"r": {animation_radius._radius.variable_name}}});'
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_complete_event_in_handler_head_expression(self) -> None:
        target: RadiusInterface = RadiusInterface()
        target.variable_name = 'test_radius_interface'
        animation_radius: ap.AnimationRadius = ap.AnimationRadius(
            target=target, radius=100)
        expression: str = animation_radius.\
            _get_complete_event_in_handler_head_expression()
        assert expression == (
            f'{target._radius.variable_name} = '
            f'{animation_radius._radius.variable_name};'
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        target: RadiusInterface = RadiusInterface()
        target.variable_name = 'test_radius_interface'
        animation_radius: ap.AnimationRadius = ap.AnimationRadius(
            target=target, radius=100)
        snapshot_name: str = animation_radius._get_next_snapshot_name()
        animation_radius._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert animation_radius._radius_snapshots[snapshot_name] == 100

        animation_radius._radius.value = 150
        animation_radius._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert animation_radius._radius_snapshots[snapshot_name] == 100

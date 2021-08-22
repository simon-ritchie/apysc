from random import randint

from retrying import retry

import apysc as ap
from apysc._display.radius_interface import RadiusInterface
from apysc._expression import expression_file_util


class TestRadiusInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_radius_if_not_initialized(self) -> None:
        interface: RadiusInterface = RadiusInterface()
        interface._initialize_radius_if_not_initialized()
        assert interface._radius == 0

        interface._radius = ap.Int(10)
        assert interface._radius == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_radius(self) -> None:
        interface: RadiusInterface = RadiusInterface()
        interface.variable_name = 'test_radius_interface'
        assert interface.radius == 0

        interface.radius = ap.Int(10)
        assert interface.radius == 10

        interface.radius = 20  # type: ignore
        assert interface.radius == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_radius_update_expression(self) -> None:
        expression_file_util.empty_expression()
        interface: RadiusInterface = RadiusInterface()
        interface.variable_name = 'test_radius_interface'
        radius: ap.Int = ap.Int(10)
        interface.radius = radius
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.radius({radius.variable_name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: RadiusInterface = RadiusInterface()
        interface.variable_name = 'test_radius_interface'
        interface.radius = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._radius_snapshots[snapshot_name] == 10

        interface.radius = ap.Int(20)
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._radius_snapshots[snapshot_name] == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: RadiusInterface = RadiusInterface()
        interface.variable_name = 'test_radius_interface'
        interface.radius = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.radius = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.radius == 10

        interface.radius = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.radius == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_converted_radius_int(self) -> None:
        interface: RadiusInterface = RadiusInterface()
        radius: ap.Int = interface._get_converted_radius_int(radius=10)
        assert radius == 10
        assert isinstance(radius, ap.Int)

        radius = interface._get_converted_radius_int(radius=ap.Int(20))
        assert radius == 20
        assert isinstance(radius, ap.Int)

from random import randint

from retrying import retry

from apysc.display.radius_interface import RadiusInterface
from apysc.expression import expression_file_util
from apysc import Int


class TestRadiusInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_radius_if_not_initialized(self) -> None:
        interface: RadiusInterface = RadiusInterface()
        interface._initialize_radius_if_not_initialized()
        assert interface._radius == 0

        interface._radius = Int(10)
        assert interface._radius == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_radius(self) -> None:
        interface: RadiusInterface = RadiusInterface()
        interface.variable_name = 'test_radius_interface'
        assert interface.radius == 0

        interface.radius = Int(10)
        assert interface.radius == 10

        interface.radius = 20  # type: ignore
        assert interface.radius == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_radius_update_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface: RadiusInterface = RadiusInterface()
        interface.variable_name = 'test_radius_interface'
        radius: Int = Int(10)
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
        interface.radius = Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._radius_snapshots[snapshot_name] == 10

        interface.radius = Int(20)
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._radius_snapshots[snapshot_name] == 10

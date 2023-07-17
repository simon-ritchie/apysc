import apysc as ap
from apysc._display.radius_mixin import RadiusMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestRadiusMixIn:
    @apply_test_settings()
    def test__initialize_radius_if_not_initialized(self) -> None:
        interface: RadiusMixIn = RadiusMixIn()
        interface._initialize_radius_if_not_initialized()
        assert interface._radius == 0

        interface._radius = ap.Int(10)
        assert interface._radius == 10

    @apply_test_settings()
    def test_radius(self) -> None:
        interface: RadiusMixIn = RadiusMixIn()
        interface.variable_name = "test_radius_interface"
        assert interface.radius == 0

        interface.radius = ap.Int(10)
        assert interface.radius == 10

    @apply_test_settings()
    def test__append_radius_update_expression(self) -> None:
        interface: RadiusMixIn = RadiusMixIn()
        interface.variable_name = "test_radius_interface"
        radius: ap.Int = ap.Int(10)
        interface.radius = radius
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{interface.variable_name}.radius({radius.variable_name});"
        assert expected in expression

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        interface: RadiusMixIn = RadiusMixIn()
        interface.variable_name = "test_radius_interface"
        interface.radius = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        if interface._radius_snapshots is None:
            raise AssertionError()
        assert interface._radius_snapshots[snapshot_name] == 10

        interface.radius = ap.Int(20)
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._radius_snapshots[snapshot_name] == 10

    @apply_test_settings()
    def test__revert(self) -> None:
        interface: RadiusMixIn = RadiusMixIn()
        interface.variable_name = "test_radius_interface"
        interface.radius = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.radius = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.radius == 10

        interface.radius = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.radius == 20

    @apply_test_settings()
    def test__get_converted_radius_int(self) -> None:
        interface: RadiusMixIn = RadiusMixIn()
        radius: ap.Int = interface._get_converted_radius_int(radius=10)
        assert radius == 10
        assert isinstance(radius, ap.Int)

        radius = interface._get_converted_radius_int(radius=ap.Int(20))
        assert radius == 20
        assert isinstance(radius, ap.Int)

    @apply_test_settings()
    def test__append_raidus_attr_linking_setting(self) -> None:
        interface: RadiusMixIn = RadiusMixIn()
        interface.variable_name = "test_radius_interface"
        interface._initialize_radius_if_not_initialized()
        assert interface._attr_linking_stack["radius"] == [ap.Int(0)]

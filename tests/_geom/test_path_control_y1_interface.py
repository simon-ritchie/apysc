from random import randint

from retrying import retry

import apysc as ap
from apysc._geom.path_control_y1_interface import PathControlY1Interface


class TestPathControlY1Interface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_control_y1(self) -> None:
        interface: PathControlY1Interface = PathControlY1Interface()
        interface._control_y1 = ap.Int(0)
        interface.control_y1 = ap.Int(10)
        assert interface.control_y1 == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: PathControlY1Interface = PathControlY1Interface()
        interface._control_y1 = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._control_y1_snapshots[snapshot_name] == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_test__revert(self) -> None:
        interface: PathControlY1Interface = PathControlY1Interface()
        interface._control_y1 = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.control_y1 == 10

        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface._control_y1 = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.control_y1 == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_control_y1_if_not_initialized(self) -> None:
        interface: PathControlY1Interface = PathControlY1Interface()
        interface._initialize_control_y1_if_not_initialized()
        assert interface.control_y1 == 0

        interface.control_y1 = ap.Int(10)
        interface._initialize_control_y1_if_not_initialized()
        assert interface.control_y1 == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_control_y1_linking_setting(self) -> None:
        interface: PathControlY1Interface = PathControlY1Interface()
        interface._initialize_control_y1_if_not_initialized()
        assert interface._attr_linking_stack['control_y1'] == [ap.Int(0)]

from random import randint

from retrying import retry

import apysc as ap
from apysc._geom.path_control_x2_interface import PathControlX2Interface


class TestPathControlX2Interface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_control_x2(self) -> None:
        interface: PathControlX2Interface = PathControlX2Interface()
        interface._control_x2 = ap.Int(0)
        interface.control_x2 = ap.Int(10)
        assert interface.control_x2 == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: PathControlX2Interface = PathControlX2Interface()
        interface._control_x2 = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._control_x2_snapshots[snapshot_name] == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: PathControlX2Interface = PathControlX2Interface()
        interface._control_x2 = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.control_x2 == 10

        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface._control_x2 = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.control_x2 == 10

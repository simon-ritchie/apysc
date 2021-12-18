from random import randint

from retrying import retry

import apysc as ap
from apysc._geom.path_dest_x_interface import PathDestXInterface


class TestPathDestXInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_dest_x(self) -> None:
        interface: PathDestXInterface = PathDestXInterface()
        interface._dest_x = ap.Int(0)
        interface.dest_x = ap.Int(10)
        assert interface.dest_x == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: PathDestXInterface = PathDestXInterface()
        interface._dest_x = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._dest_x_snapshots[snapshot_name] == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: PathDestXInterface = PathDestXInterface()
        interface._dest_x = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface._dest_x == 10

        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface._dest_x = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface._dest_x == 10

from random import randint

from retrying import retry

import apysc as ap
from apysc._geom.path_x_interface import PathXInterface


class TestPathXInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_x(self) -> None:
        interface: PathXInterface = PathXInterface()
        interface._x = ap.Int(10)
        assert interface.x == 10

        interface.x = ap.Int(20)
        assert interface.x == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: PathXInterface = PathXInterface()
        interface._x = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._x_snapshots[snapshot_name] == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: PathXInterface = PathXInterface()
        interface._x = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.x == 10

        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface._x = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.x == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_x_if_not_initialized(self) -> None:
        interface: PathXInterface = PathXInterface()
        interface._initialize_x_if_not_initialized()
        assert interface.x == 0

        interface.x = ap.Int(10)
        interface._initialize_x_if_not_initialized()
        assert interface.x == 10

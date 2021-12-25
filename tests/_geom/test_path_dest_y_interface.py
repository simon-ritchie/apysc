from random import randint

from retrying import retry

import apysc as ap
from apysc._geom.path_dest_y_interface import PathDestYInterface


class TestPathDestYInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_dest_y(self) -> None:
        interface: PathDestYInterface = PathDestYInterface()
        interface._dest_y = ap.Int(0)
        interface.dest_y = ap.Int(10)
        assert interface.dest_y == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: PathDestYInterface = PathDestYInterface()
        interface._dest_y = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._dest_y_snapshots[snapshot_name] == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: PathDestYInterface = PathDestYInterface()
        interface._dest_y = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface._dest_y == 10

        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface._dest_y = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface._dest_y == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_dest_y_if_not_initialized(self) -> None:
        interface: PathDestYInterface = PathDestYInterface()
        interface._initialize_dest_y_if_not_initialized()
        assert interface.dest_y == 0

        interface.dest_y = ap.Int(10)
        interface._initialize_dest_y_if_not_initialized()
        assert interface.dest_y == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_dest_y_linking_setting(self) -> None:
        interface: PathDestYInterface = PathDestYInterface()
        interface._initialize_dest_y_if_not_initialized()
        assert interface._attr_linking_stack['dest_y'] == [ap.Int(0)]

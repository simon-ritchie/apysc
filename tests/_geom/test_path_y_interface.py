from random import randint

from retrying import retry

import apysc as ap
from apysc._geom.path_y_interface import PathYInterface


class TestPathYInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_y(self) -> None:
        interface: PathYInterface = PathYInterface()
        interface._y = ap.Int(0)
        interface.y = ap.Int(20)
        assert interface.y == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: PathYInterface = PathYInterface()
        interface._y = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._y_snapshots[snapshot_name] == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: PathYInterface = PathYInterface()
        interface._y = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.y == 10

        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface._y = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.y == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_y_if_not_initialized(self) -> None:
        interface: PathYInterface = PathYInterface()
        interface._initialize_y_if_not_initialized()
        assert interface.y == 0

        interface.y = ap.Int(10)
        interface._initialize_y_if_not_initialized()
        assert interface.y == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_y_linking_setting(self) -> None:
        interface: PathYInterface = PathYInterface()
        interface._initialize_y_if_not_initialized()
        assert interface._attr_linking_stack['y'] == [ap.Int(0)]

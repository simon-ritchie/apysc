from random import randint

from retrying import retry

import apysc as ap
from apysc._geom.path_dest_x_mixin import PathDestXMixIn


class TestPathDestXMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_dest_x(self) -> None:
        mixin: PathDestXMixIn = PathDestXMixIn()
        mixin._dest_x = ap.Int(0)
        mixin.dest_x = ap.Int(10)
        assert mixin.dest_x == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        mixin: PathDestXMixIn = PathDestXMixIn()
        mixin._dest_x = ap.Int(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._dest_x_snapshots[snapshot_name] == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        mixin: PathDestXMixIn = PathDestXMixIn()
        mixin._dest_x = ap.Int(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin._dest_x == 10

        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._dest_x = ap.Int(20)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin._dest_x == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_dest_x_if_not_initialized(self) -> None:
        mixin: PathDestXMixIn = PathDestXMixIn()
        mixin._initialize_dest_x_if_not_initialized()
        assert mixin.dest_x == 0

        mixin.dest_x = ap.Int(10)
        mixin._initialize_dest_x_if_not_initialized()
        assert mixin.dest_x == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_dest_x_linking_setting(self) -> None:
        mixin: PathDestXMixIn = PathDestXMixIn()
        mixin._initialize_dest_x_if_not_initialized()
        assert mixin._attr_linking_stack["dest_x"] == [ap.Int(0)]
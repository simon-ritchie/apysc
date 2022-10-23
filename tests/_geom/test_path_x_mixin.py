from random import randint

from retrying import retry

import apysc as ap
from apysc._geom.path_x_mixin import PathXMixIn


class TestPathXMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_x(self) -> None:
        mixin: PathXMixIn = PathXMixIn()
        mixin._x = ap.Int(10)
        assert mixin.x == 10

        mixin.x = ap.Int(20)
        assert mixin.x == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        mixin: PathXMixIn = PathXMixIn()
        mixin._x = ap.Int(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._x_snapshots[snapshot_name] == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        mixin: PathXMixIn = PathXMixIn()
        mixin._x = ap.Int(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.x == 10

        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._x = ap.Int(20)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.x == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_x_if_not_initialized(self) -> None:
        mixin: PathXMixIn = PathXMixIn()
        mixin._initialize_x_if_not_initialized()
        assert mixin.x == 0

        mixin.x = ap.Int(10)
        mixin._initialize_x_if_not_initialized()
        assert mixin.x == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_x_linking_setting(self) -> None:
        mixin: PathXMixIn = PathXMixIn()
        mixin._initialize_x_if_not_initialized()
        assert mixin._attr_linking_stack["x"] == [ap.Int(0)]

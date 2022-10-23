from random import randint

from retrying import retry

import apysc as ap
from apysc._geom.path_y_mixin import PathYMixIn


class TestPathYMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_y(self) -> None:
        mixin: PathYMixIn = PathYMixIn()
        mixin._y = ap.Int(0)
        mixin.y = ap.Int(20)
        assert mixin.y == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        mixin: PathYMixIn = PathYMixIn()
        mixin._y = ap.Int(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._y_snapshots[snapshot_name] == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        mixin: PathYMixIn = PathYMixIn()
        mixin._y = ap.Int(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.y == 10

        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._y = ap.Int(20)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.y == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_y_if_not_initialized(self) -> None:
        mixin: PathYMixIn = PathYMixIn()
        mixin._initialize_y_if_not_initialized()
        assert mixin.y == 0

        mixin.y = ap.Int(10)
        mixin._initialize_y_if_not_initialized()
        assert mixin.y == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_y_linking_setting(self) -> None:
        mixin: PathYMixIn = PathYMixIn()
        mixin._initialize_y_if_not_initialized()
        assert mixin._attr_linking_stack["y"] == [ap.Int(0)]

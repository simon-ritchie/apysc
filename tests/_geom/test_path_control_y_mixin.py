from random import randint

from retrying import retry

import apysc as ap
from apysc._geom.path_control_y_mixin import PathControlMixIn


class TestPathControlMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_control_y(self) -> None:
        mixin: PathControlMixIn = PathControlMixIn()
        mixin._control_y = ap.Int(0)
        mixin.control_y = ap.Int(10)
        assert mixin.control_y == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        mixin: PathControlMixIn = PathControlMixIn()
        mixin._control_y = ap.Int(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._control_y_snapshots[snapshot_name] == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        mixin: PathControlMixIn = PathControlMixIn()
        mixin._control_y = ap.Int(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.control_y == 10

        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._control_y = ap.Int(20)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.control_y == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_control_y_if_not_initialized(self) -> None:
        mixin: PathControlMixIn = PathControlMixIn()
        mixin._initialize_control_y_if_not_initialized()
        assert mixin.control_y == 0

        mixin.control_y = ap.Int(10)
        mixin._initialize_control_y_if_not_initialized()
        assert mixin.control_y == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_control_y_linking_setting(self) -> None:
        mixin: PathControlMixIn = PathControlMixIn()
        mixin._initialize_control_y_if_not_initialized()
        assert mixin._attr_linking_stack["control_y"] == [ap.Int(0)]

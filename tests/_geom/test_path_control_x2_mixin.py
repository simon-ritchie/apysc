from random import randint

from retrying import retry

import apysc as ap
from apysc._geom.path_control_x2_mixin import PathControlX2MixIn
from apysc._testing.testing_helper import apply_test_settings


class TestPathControlX2MixIn:
    @apply_test_settings()
    def test_control_x2(self) -> None:
        mixin: PathControlX2MixIn = PathControlX2MixIn()
        mixin._control_x2 = ap.Int(0)
        mixin.control_x2 = ap.Int(10)
        assert mixin.control_x2 == 10

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        mixin: PathControlX2MixIn = PathControlX2MixIn()
        mixin._control_x2 = ap.Int(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._control_x2_snapshots[snapshot_name] == 10

    @apply_test_settings()
    def test__revert(self) -> None:
        mixin: PathControlX2MixIn = PathControlX2MixIn()
        mixin._control_x2 = ap.Int(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.control_x2 == 10

        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._control_x2 = ap.Int(20)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.control_x2 == 10

    @apply_test_settings()
    def test__initialize_control_x2_if_not_initialized(self) -> None:
        mixin: PathControlX2MixIn = PathControlX2MixIn()
        mixin._initialize_control_x2_if_not_initialized()
        assert mixin.control_x2 == 0

        mixin.control_x2 = ap.Int(10)
        mixin._initialize_control_x2_if_not_initialized()
        assert mixin.control_x2 == 10

    @apply_test_settings()
    def test__append_control_x2_linking_setting(self) -> None:
        mixin: PathControlX2MixIn = PathControlX2MixIn()
        mixin._initialize_control_x2_if_not_initialized()
        assert mixin._attr_linking_stack["control_x2"] == [ap.Int(0)]

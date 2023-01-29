import apysc as ap
from apysc._geom.path_dest_y_mixin import PathDestYMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestPathDestYMixIn:
    @apply_test_settings()
    def test_dest_y(self) -> None:
        mixin: PathDestYMixIn = PathDestYMixIn()
        mixin._dest_y = ap.Int(0)
        mixin.dest_y = ap.Int(10)
        assert mixin.dest_y == 10

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        mixin: PathDestYMixIn = PathDestYMixIn()
        mixin._dest_y = ap.Int(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._dest_y_snapshots[snapshot_name] == 10

    @apply_test_settings()
    def test__revert(self) -> None:
        mixin: PathDestYMixIn = PathDestYMixIn()
        mixin._dest_y = ap.Int(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin._dest_y == 10

        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._dest_y = ap.Int(20)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin._dest_y == 10

    @apply_test_settings()
    def test__initialize_dest_y_if_not_initialized(self) -> None:
        mixin: PathDestYMixIn = PathDestYMixIn()
        mixin._initialize_dest_y_if_not_initialized()
        assert mixin.dest_y == 0

        mixin.dest_y = ap.Int(10)
        mixin._initialize_dest_y_if_not_initialized()
        assert mixin.dest_y == 10

    @apply_test_settings()
    def test__append_dest_y_linking_setting(self) -> None:
        mixin: PathDestYMixIn = PathDestYMixIn()
        mixin._initialize_dest_y_if_not_initialized()
        assert mixin._attr_linking_stack["dest_y"] == [ap.Int(0)]

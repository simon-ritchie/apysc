import apysc as ap
from apysc._geom.path_y_mixin import PathYMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestPathYMixIn:
    @apply_test_settings()
    def test_y(self) -> None:
        mixin: PathYMixIn = PathYMixIn()
        mixin._y = ap.Number(0)
        mixin.y = ap.Number(20)
        assert mixin.y == 20

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        mixin: PathYMixIn = PathYMixIn()
        mixin._y = ap.Number(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        if mixin._y_snapshots is None:
            raise AssertionError()
        assert mixin._y_snapshots[snapshot_name] == 10

    @apply_test_settings()
    def test__revert(self) -> None:
        mixin: PathYMixIn = PathYMixIn()
        mixin._y = ap.Number(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.y == 10

        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._y = ap.Number(20)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.y == 10

    @apply_test_settings()
    def test__initialize_y_if_not_initialized(self) -> None:
        mixin: PathYMixIn = PathYMixIn()
        mixin._initialize_y_if_not_initialized()
        assert mixin.y == 0

        mixin.y = ap.Number(10)
        mixin._initialize_y_if_not_initialized()
        assert mixin.y == 10

    @apply_test_settings()
    def test__append_y_linking_setting(self) -> None:
        mixin: PathYMixIn = PathYMixIn()
        mixin._initialize_y_if_not_initialized()
        assert mixin._attr_linking_stack["y"] == [ap.Number(0)]

import apysc as ap
from apysc._geom.path_control_y1_mixin import PathControlY1MixIn
from apysc._testing.testing_helper import apply_test_settings


class TestPathControlY1MixIn:
    @apply_test_settings()
    def test_control_y1(self) -> None:
        mixin: PathControlY1MixIn = PathControlY1MixIn()
        mixin._control_y1 = ap.Number(0)
        mixin.control_y1 = ap.Number(10)
        assert mixin.control_y1 == 10

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        mixin: PathControlY1MixIn = PathControlY1MixIn()
        mixin._control_y1 = ap.Number(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        if mixin._control_y1_snapshots is None:
            raise AssertionError()
        assert mixin._control_y1_snapshots[snapshot_name] == 10

    @apply_test_settings()
    def test_test__revert(self) -> None:
        mixin: PathControlY1MixIn = PathControlY1MixIn()
        mixin._control_y1 = ap.Number(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.control_y1 == 10

        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._control_y1 = ap.Number(20)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.control_y1 == 10

    @apply_test_settings()
    def test__initialize_control_y1_if_not_initialized(self) -> None:
        mixin: PathControlY1MixIn = PathControlY1MixIn()
        mixin._initialize_control_y1_if_not_initialized()
        assert mixin.control_y1 == 0

        mixin.control_y1 = ap.Number(10)
        mixin._initialize_control_y1_if_not_initialized()
        assert mixin.control_y1 == 10

    @apply_test_settings()
    def test__append_control_y1_linking_setting(self) -> None:
        mixin: PathControlY1MixIn = PathControlY1MixIn()
        mixin._initialize_control_y1_if_not_initialized()
        assert mixin._attr_linking_stack["control_y1"] == [ap.Number(0)]

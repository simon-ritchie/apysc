import apysc as ap
from apysc._geom.path_control_x_mixin import PathControlXMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestPathControlXMixIn:
    @apply_test_settings()
    def test_control_x(self) -> None:
        mixin: PathControlXMixIn = PathControlXMixIn()
        mixin._control_x = ap.Number(0)
        mixin.control_x = ap.Number(10)
        assert mixin.control_x == 10

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        mixin: PathControlXMixIn = PathControlXMixIn()
        mixin._control_x = ap.Number(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        if mixin._control_x_snapshots is None:
            raise AssertionError()
        assert mixin._control_x_snapshots[snapshot_name] == 10

    @apply_test_settings()
    def test__revert(self) -> None:
        mixin: PathControlXMixIn = PathControlXMixIn()
        mixin._control_x = ap.Number(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.control_x == 10

        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._control_x = ap.Number(20)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.control_x == 10

    @apply_test_settings()
    def test__initialize_control_x_if_not_initialized(self) -> None:
        mixin: PathControlXMixIn = PathControlXMixIn()
        mixin._initialize_control_x_if_not_initialized()
        assert mixin.control_x == 0

        mixin.control_x = ap.Number(10)
        mixin._initialize_control_x_if_not_initialized()
        assert mixin.control_x == 10

    @apply_test_settings()
    def test__append_control_x_linking_setting(self) -> None:
        mixin: PathControlXMixIn = PathControlXMixIn()
        mixin._initialize_control_x_if_not_initialized()
        assert mixin._attr_linking_stack["control_x"] == [ap.Number(0)]

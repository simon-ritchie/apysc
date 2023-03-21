import apysc as ap
from apysc._geom.relative_mixin import RelativeMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestRelativeMixIn:
    @apply_test_settings()
    def test_relative(self) -> None:
        mixin: RelativeMixIn = RelativeMixIn()
        mixin._relative = ap.Boolean(False)
        mixin.relative = ap.Boolean(True)
        assert mixin.relative

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        mixin: RelativeMixIn = RelativeMixIn()
        mixin._relative = ap.Boolean(True)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        if mixin._relative_snapshots is None:
            raise AssertionError()
        assert mixin._relative_snapshots[snapshot_name]

    @apply_test_settings()
    def test__revert(self) -> None:
        mixin: RelativeMixIn = RelativeMixIn()
        mixin._relative = ap.Boolean(True)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.relative

        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin.relative = ap.Boolean(False)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.relative

    @apply_test_settings()
    def test__initialize_relative_if_not_initialized(self) -> None:
        mixin: RelativeMixIn = RelativeMixIn()
        mixin._initialize_relative_if_not_initialized()
        assert not mixin.relative

        mixin.relative = ap.Boolean(True)
        mixin._initialize_relative_if_not_initialized()
        assert mixin.relative

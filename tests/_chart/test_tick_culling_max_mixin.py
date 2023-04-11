import apysc as ap
from apysc._testing.testing_helper import apply_test_settings
from apysc._chart.tick_culling_max_mixin import TickCullingMaxMixIn


class TestTickCullingMaxMixIn:
    @apply_test_settings()
    def test__set_initial_tick_culling_max(self) -> None:
        mixin: TickCullingMaxMixIn = TickCullingMaxMixIn()
        mixin._set_initial_tick_culling_max(
            tick_culling_max=None,
        )
        tick_culling_max_ = mixin._tick_culling_max
        assert tick_culling_max_ is None

        mixin._set_initial_tick_culling_max(
            tick_culling_max=10,
            variable_name_suffix="test_suffix_2",
        )
        assert mixin._tick_culling_max == ap.Int(10)
        if mixin._tick_culling_max is not None:
            assert mixin._tick_culling_max._variable_name_suffix == "test_suffix_2"

        mixin._set_initial_tick_culling_max(
            tick_culling_max=ap.Int(11, variable_name_suffix="test_suffix_3"),
        )
        assert mixin._tick_culling_max == ap.Int(11)
        if mixin._tick_culling_max is not None:
            assert mixin._tick_culling_max._variable_name_suffix == "test_suffix_3"

    @apply_test_settings()
    def test__make_snapshot_and__revert(self) -> None:
        mixin: TickCullingMaxMixIn = TickCullingMaxMixIn()
        mixin._set_initial_tick_culling_max(tick_culling_max=None)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin._tick_culling_max is None

        mixin._set_initial_tick_culling_max(tick_culling_max=10)
        snapshot_name = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._set_initial_tick_culling_max(tick_culling_max=11)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin._tick_culling_max == ap.Int(10)

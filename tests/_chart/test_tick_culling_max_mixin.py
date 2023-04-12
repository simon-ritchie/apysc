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

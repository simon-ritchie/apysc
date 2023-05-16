import apysc as ap
from apysc._chart.tick_max_num_mixin import TickMaxNumMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestTickMaxNumMixIn:
    @apply_test_settings()
    def test__set_initial_tick_max_num(self) -> None:
        mixin: TickMaxNumMixIn = TickMaxNumMixIn()
        mixin._set_initial_tick_max_num(
            tick_max_num=None,
        )
        tick_max_num_ = mixin._tick_max_num
        assert tick_max_num_ is None

        mixin._set_initial_tick_max_num(
            tick_max_num=10,
            variable_name_suffix="test_suffix_2",
        )
        assert mixin._tick_max_num == ap.Int(10)
        if mixin._tick_max_num is not None:
            assert mixin._tick_max_num._variable_name_suffix == "test_suffix_2"

        mixin._set_initial_tick_max_num(
            tick_max_num=ap.Int(11, variable_name_suffix="test_suffix_3"),
        )
        assert mixin._tick_max_num == ap.Int(11)
        if mixin._tick_max_num is not None:
            assert mixin._tick_max_num._variable_name_suffix == "test_suffix_3"

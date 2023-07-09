import apysc as ap
from apysc._chart.tick_text_max_num_of_decimal_places_mixin import (
    TickTextMaxNumOfDecimalPlacesMixIn,
)
from apysc._testing.testing_helper import apply_test_settings


class TestTickTextMaxNumOfDecimalPlacesMixIn:
    @apply_test_settings()
    def test__set_initial_tick_text_max_num_of_decimal_places(self) -> None:
        mixin: TickTextMaxNumOfDecimalPlacesMixIn = TickTextMaxNumOfDecimalPlacesMixIn()
        mixin._set_initial_tick_text_max_num_of_decimal_places(
            tick_text_max_num_of_decimal_places=1,
            variable_name_suffix="test_suffix_1",
        )
        assert mixin._tick_text_max_num_of_decimal_places == 1
        assert (
            "test_suffix_1" in mixin._tick_text_max_num_of_decimal_places.variable_name
        )

        tick_text_max_num_of_decimal_places: ap.Int = ap.Int(
            2, variable_name_suffix="test_suffix_2"
        )
        mixin._set_initial_tick_text_max_num_of_decimal_places(
            tick_text_max_num_of_decimal_places=tick_text_max_num_of_decimal_places
        )
        assert mixin._tick_text_max_num_of_decimal_places == ap.Int(2)
        assert (
            "test_suffix_2" in mixin._tick_text_max_num_of_decimal_places.variable_name
        )

import apysc as ap
from apysc._chart.left_margin_mixin import LeftMarginMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestLeftMarginMixIn:
    @apply_test_settings()
    def test__set_initial_left_margin(self) -> None:
        mixin: LeftMarginMixIn = LeftMarginMixIn()
        mixin._set_initial_left_margin(
            left_margin=10,
            variable_name_suffix="test_suffix_1",
        )
        assert mixin._left_margin == ap.Int(10)
        assert mixin._left_margin._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_left_margin(
            left_margin=ap.Int(20, variable_name_suffix="test_suffix_2"),
        )
        assert mixin._left_margin == ap.Int(20)
        assert mixin._left_margin._variable_name_suffix == "test_suffix_2"

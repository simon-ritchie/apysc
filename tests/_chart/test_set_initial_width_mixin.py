import apysc as ap
from apysc._chart.set_initial_width_mixin import SetInitialWidthMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestSetInitialWidthMixIn:
    @apply_test_settings()
    def test__set_initial_width(self) -> None:
        mixin: SetInitialWidthMixIn = SetInitialWidthMixIn()
        mixin._set_initial_width(width=10, variable_name_suffix="test_suffix_1")
        assert mixin._width == ap.Int(10)
        assert mixin._width._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_width(
            width=ap.Int(20, variable_name_suffix="test_suffix_2")
        )
        assert mixin._width == ap.Int(20)
        assert mixin._width._variable_name_suffix == "test_suffix_2"

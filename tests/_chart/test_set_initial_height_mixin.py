import apysc as ap
from apysc._chart.set_initial_height_mixin import SetInitialHeightMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestSetInitialHeightMixIn:
    @apply_test_settings()
    def test__set_initial_height(self) -> None:
        mixin: SetInitialHeightMixIn = SetInitialHeightMixIn()
        mixin._set_initial_height(height=100, variable_name_suffix="test_suffix_1")
        assert mixin._height == ap.Int(100)
        assert mixin._height._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_height(
            height=ap.Int(200, variable_name_suffix="test_suffix_2")
        )
        assert mixin._height == ap.Int(200)
        assert mixin._height._variable_name_suffix == "test_suffix_2"

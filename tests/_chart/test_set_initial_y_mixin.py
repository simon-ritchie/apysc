import apysc as ap
from apysc._chart.set_initial_y_mixin import SetInitialYMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestSetInitialYMixIn:
    @apply_test_settings()
    def test__set_initial_y(self) -> None:
        mixin: SetInitialYMixIn = SetInitialYMixIn()
        mixin._set_initial_y(y=50, variable_name_suffix="test_suffix_1")
        assert mixin._y == ap.Number(50)
        assert mixin._y._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_y(y=ap.Number(100, variable_name_suffix="test_suffix_2"))
        assert mixin._y == ap.Number(100)
        assert mixin._y._variable_name_suffix == "test_suffix_2"

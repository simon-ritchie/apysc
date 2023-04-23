import apysc as ap
from apysc._chart.set_initial_x_mixin import SetInitialXMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestSetInitialXMixIn:
    @apply_test_settings()
    def test__set_initial_x(self) -> None:
        mixin: SetInitialXMixIn = SetInitialXMixIn()
        mixin._set_initial_x(x=150, variable_name_suffix="test_suffix_1")
        assert mixin._x == ap.Int(150)
        assert mixin._x._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_x(x=ap.Int(200, variable_name_suffix="test_suffix_2"))
        assert mixin._x == ap.Int(200)
        assert mixin._x._variable_name_suffix == "test_suffix_2"

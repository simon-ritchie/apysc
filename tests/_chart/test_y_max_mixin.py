import apysc as ap
from apysc._chart.y_max_mixin import YMaxMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestYMaxMixIn:
    @apply_test_settings()
    def test__set_initial_y_max(self) -> None:
        mixin: YMaxMixIn = YMaxMixIn()
        mixin._set_initial_y_max(y_max=None, variable_name_suffix="test_suffix_1")
        assert mixin._y_max is None

        mixin._set_initial_y_max(y_max=100, variable_name_suffix="test_suffix_2")
        assert mixin._y_max == ap.Number(100)
        if mixin._y_max is not None:
            assert mixin._y_max._variable_name_suffix == "test_suffix_2"

        mixin._set_initial_y_max(
            y_max=ap.Number(200, variable_name_suffix="test_suffix_3"),
        )
        assert mixin._y_max == ap.Number(200)
        if mixin._y_max is not None:
            assert mixin._y_max._variable_name_suffix == "test_suffix_3"

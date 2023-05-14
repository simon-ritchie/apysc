import apysc as ap
from apysc._chart.y_min_mixin import YMinMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestYMinMixIn:
    @apply_test_settings()
    def test__set_initial_y_min(self) -> None:
        mixin: YMinMixIn = YMinMixIn()
        mixin._set_initial_y_min(y_min=None, variable_name_suffix="test_suffix_1")
        assert mixin._y_min is None

        mixin._set_initial_y_min(y_min=10, variable_name_suffix="test_suffix_2")
        assert mixin._y_min == ap.Number(10)
        if mixin._y_min is not None:
            assert mixin._y_min._variable_name_suffix == "test_suffix_2"

        mixin._set_initial_y_min(
            y_min=ap.Number(20, variable_name_suffix="test_suffix_3")
        )
        assert mixin._y_min == ap.Number(20)
        if mixin._y_min is not None:
            assert mixin._y_min._variable_name_suffix == "test_suffix_3"

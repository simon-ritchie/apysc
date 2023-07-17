import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._time.weekday_mixin import WeekdayMixIn


class TestWeekdayMixIn:
    @apply_test_settings()
    def test__get_weekday_js_val_with_attrs(self) -> None:
        mixin: WeekdayMixIn = WeekdayMixIn()
        weekday_js_val: int = mixin._get_weekday_js_val_with_attrs()
        assert weekday_js_val == 0

        mixin._year = ap.Int(2022)
        weekday_js_val = mixin._get_weekday_js_val_with_attrs()
        assert weekday_js_val == 0

        mixin._month = ap.Int(11)
        weekday_js_val = mixin._get_weekday_js_val_with_attrs()
        assert weekday_js_val == 0

        mixin._day = ap.Int(29)
        weekday_js_val = mixin._get_weekday_js_val_with_attrs()
        assert weekday_js_val == 2

        mixin._day = ap.Int(26)
        weekday_js_val = mixin._get_weekday_js_val_with_attrs()
        assert weekday_js_val == 6

        mixin._day = ap.Int(27)
        weekday_js_val = mixin._get_weekday_js_val_with_attrs()
        assert weekday_js_val == 0

    @apply_test_settings()
    def test__append_weekday_js_getter_expression(self) -> None:
        mixin: WeekdayMixIn = WeekdayMixIn()
        mixin.variable_name = "test_weekday_mixin"
        weekday_val: ap.Int = ap.Int(3)
        mixin._append_weekday_js_getter_expression(weekday_val=weekday_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{weekday_val.variable_name} = {mixin.variable_name}.getDay();"
        assert expected in expression

    @apply_test_settings()
    def test_weekday_js(self) -> None:
        mixin: WeekdayMixIn = WeekdayMixIn()
        mixin.variable_name = "test_weekday_mixin"
        mixin._year = ap.Int(2022)
        mixin._month = ap.Int(11)
        mixin._day = ap.Int(29)
        weekday: ap.Int = mixin.weekday_js
        assert weekday == 2
        assert isinstance(weekday, ap.Int)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{weekday.variable_name} = {mixin.variable_name}.getDay();"
        assert expected in expression

    @apply_test_settings()
    def test__get_weekday_py_val_with_attrs(self) -> None:
        mixin: WeekdayMixIn = WeekdayMixIn()
        weekday_py_val: int = mixin._get_weekday_py_val_with_attrs()
        assert weekday_py_val == 0

        mixin._year = ap.Int(2022)
        weekday_py_val = mixin._get_weekday_py_val_with_attrs()
        assert weekday_py_val == 0

        mixin._month = ap.Int(11)
        weekday_py_val = mixin._get_weekday_py_val_with_attrs()
        assert weekday_py_val == 0

        mixin._day = ap.Int(21)
        weekday_py_val = mixin._get_weekday_py_val_with_attrs()
        assert weekday_py_val == 0

        mixin._day = ap.Int(22)
        weekday_py_val = mixin._get_weekday_py_val_with_attrs()
        assert weekday_py_val == 1

        mixin._day = ap.Int(27)
        weekday_py_val = mixin._get_weekday_py_val_with_attrs()
        assert weekday_py_val == 6

    @apply_test_settings()
    def test__append_weekday_py_getter_expression(self) -> None:
        mixin: WeekdayMixIn = WeekdayMixIn()
        weekday_val: ap.Int = ap.Int(3)
        mixin._append_weekday_py_getter_expression(weekday_val=weekday_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{weekday_val.variable_name} = {mixin.variable_name}.getDay() - 1;"
            f"\nif ({weekday_val.variable_name} === -1) {{"
            f"\n  {weekday_val.variable_name} = 6;"
            "\n}"
        )
        assert expected in expression

    @apply_test_settings()
    def test_weekday_py(self) -> None:
        mixin: WeekdayMixIn = WeekdayMixIn()
        mixin._year = ap.Int(2022)
        mixin._month = ap.Int(11)
        mixin._day = ap.Int(21)
        weekday: ap.Int = mixin.weekday_py
        assert weekday == 0
        assert isinstance(weekday, ap.Int)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{weekday.variable_name} = {mixin.variable_name}.getDay() - 1;"
            f"\nif ({weekday.variable_name} === -1) {{"
            f"\n  {weekday.variable_name} = 6;"
            "\n}"
        )
        assert expected in expression

        mixin._day = ap.Int(22)
        weekday = mixin.weekday_py
        assert weekday == 1

        mixin._day = ap.Int(27)
        weekday = mixin.weekday_py
        assert weekday == 6

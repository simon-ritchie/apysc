from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import expression_data_util
from apysc._time.year_mixin import YearMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestYearMixIn:
    @apply_test_settings()
    def test__set_init_year_value(self) -> None:
        mixin: YearMixIn = YearMixIn()
        mixin._set_init_year_value(year=2022)
        assert mixin._initial_year == 2022
        assert isinstance(mixin._initial_year, int)
        assert mixin._year == 2022
        assert isinstance(mixin._year, ap.Int)

    @apply_test_settings()
    def test__get_init_year_argument_expression(self) -> None:
        mixin: YearMixIn = YearMixIn()
        mixin._set_init_year_value(year=2022)
        expression: str = mixin._get_init_year_argument_expression()
        assert expression == "2022"

        int_val: ap.Int = ap.Int(2022)
        mixin._set_init_year_value(year=int_val)
        expression = mixin._get_init_year_argument_expression()
        assert expression == int_val.variable_name

    @apply_test_settings()
    def test__make_snapshot_and_revert(self) -> None:
        mixin: YearMixIn = YearMixIn()
        mixin._set_init_year_value(year=2022)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._year._value = 2021
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin._year == 2022

    @apply_test_settings()
    def test__append_year_getter_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: YearMixIn = YearMixIn()
        mixin.variable_name = "test_year_mixin"
        year_val: ap.Int = ap.Int(2022)
        mixin._append_year_getter_expression(year_val=year_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{year_val.variable_name} = {mixin.variable_name}.getFullYear();"
        )
        assert expected in expression

    @apply_test_settings()
    def test_year(self) -> None:
        expression_data_util.empty_expression()
        mixin: YearMixIn = YearMixIn()
        mixin.variable_name = "test_year_mixin"
        mixin._set_init_year_value(year=2022)
        year: ap.Int = mixin.year
        assert year == 2022
        assert isinstance(year, ap.Int)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{year.variable_name} = {mixin.variable_name}.getFullYear();"
        assert expected in expression

        year = ap.Int(2023)
        mixin.year = year
        assert mixin.year == 2023
        assert isinstance(year, ap.Int)
        expression = expression_data_util.get_current_expression()
        expected = f"{mixin.variable_name}.setFullYear({year.variable_name});"
        assert expected in expression

    @apply_test_settings()
    def test__append_year_setter_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: YearMixIn = YearMixIn()
        mixin.variable_name = "test_year_mixin"
        mixin._set_init_year_value(year=2022)
        year_val: ap.Int = ap.Int(2023)
        mixin._append_year_setter_expression(year_val=year_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin.variable_name}.setFullYear({year_val.variable_name});"
        assert expected in expression

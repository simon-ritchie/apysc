import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._time import timedelta_
from apysc._time.timedelta_ import TimeDelta


@apply_test_settings()
def test__get_variable_name_suffix_from_datetimes() -> None:
    left_datetime: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)
    right_datetime: ap.DateTime = ap.DateTime(year=2022, month=12, day=3)
    variable_name_suffix: str = timedelta_._get_variable_name_suffix_from_datetimes(
        left_datetime=left_datetime,
        right_datetime=right_datetime,
    )
    assert variable_name_suffix == ""

    right_datetime._variable_name_suffix = "right_datetime"
    variable_name_suffix = timedelta_._get_variable_name_suffix_from_datetimes(
        left_datetime=left_datetime,
        right_datetime=right_datetime,
    )
    assert variable_name_suffix == "right_datetime"

    right_datetime._variable_name_suffix = ""
    left_datetime._variable_name_suffix = "left_datetime"
    variable_name_suffix = timedelta_._get_variable_name_suffix_from_datetimes(
        left_datetime=left_datetime,
        right_datetime=right_datetime,
    )
    assert variable_name_suffix == "left_datetime"

    right_datetime._variable_name_suffix = "right_datetime"
    variable_name_suffix = timedelta_._get_variable_name_suffix_from_datetimes(
        left_datetime=left_datetime,
        right_datetime=right_datetime,
    )
    assert variable_name_suffix == "left_datetime_right_datetime"


class TestTimeDelta:
    @apply_test_settings()
    def test__create_initial_substitution_expression(self) -> None:
        left_datetime: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)
        right_datetime: ap.DateTime = ap.DateTime(year=2022, month=12, day=3)
        timedelta__: TimeDelta = TimeDelta(
            left_datetime=left_datetime,
            right_datetime=right_datetime,
        )
        expression: str = timedelta__._create_initial_substitution_expression()
        expected: str = (
            f"{timedelta__.variable_name} = {left_datetime.variable_name}.getTime()"
            f" - {right_datetime.variable_name}.getTime();"
        )
        assert expected in expression

    @apply_test_settings()
    def test__append_constructor_expression(self) -> None:
        expression_data_util.empty_expression()
        left_datetime: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)
        right_datetime: ap.DateTime = ap.DateTime(year=2022, month=12, day=3)
        timedelta__: TimeDelta = TimeDelta(
            left_datetime=left_datetime,
            right_datetime=right_datetime,
        )
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"var {timedelta__.variable_name} = {left_datetime.variable_name}.getTime()"
            f" - {right_datetime.variable_name}.getTime();"
        )
        assert expected in expression

    @apply_test_settings()
    def test___init__(self) -> None:
        expression_data_util.empty_expression()
        left_datetime: ap.DateTime = ap.DateTime(
            year=2022,
            month=12,
            day=5,
            variable_name_suffix="left_datetime",
        )
        right_datetime: ap.DateTime = ap.DateTime(
            year=2022,
            month=12,
            day=3,
            variable_name_suffix="right_datetime",
        )
        timedelta__: TimeDelta = TimeDelta(
            left_datetime=left_datetime,
            right_datetime=right_datetime,
        )
        assert var_names.TIME_DELTA in timedelta__.variable_name
        assert "left_datetime_right_datetime" in timedelta__.variable_name

        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"var {timedelta__.variable_name} = {left_datetime.variable_name}.getTime()"
            f" - {right_datetime.variable_name}.getTime();"
        )
        assert expected in expression

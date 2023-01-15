"""Class implementations for datetime-related mix-in.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._time.day_mixin import DayMixIn
from apysc._time.hour_mixin import HourMixIn
from apysc._time.millisecond_mixin import MillisecondMixIn
from apysc._time.minute_mixin import MinuteMixIn
from apysc._time.month_end_mixin import MonthEndMixin
from apysc._time.month_mixin import MonthMixIn
from apysc._time.now_mixin import NowMixIn
from apysc._time.second_mixin import SecondMixIn
from apysc._time.timedelta_ import TimeDelta
from apysc._time.weekday_mixin import WeekdayMixIn
from apysc._time.year_mixin import YearMixIn
from apysc._type.initial_substitution_exp_mixin import InitialSubstitutionExpMixIn
from apysc._type.int import Int
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos


class DateTime(
    VariableNameSuffixMixIn,
    InitialSubstitutionExpMixIn,
    YearMixIn,
    MonthMixIn,
    DayMixIn,
    HourMixIn,
    MinuteMixIn,
    SecondMixIn,
    MillisecondMixIn,
    WeekdayMixIn,
    MonthEndMixin,
    NowMixIn,
):
    """
    The class for datetime-related interfaces.

    Attributes
    ----------
    year : Int
        A current year value.
    month : Int
        A current month value.
    day : Int
        A current day value.
    hour : Int
        A current hour value.
    minute : Int
        A current minute value.
    second : Int
        A current second value.
    millisecond : Int
        A current millisecond value.
    weekday_js : Int
        A current JavaScript's weekday value (Sunday is 0).
    weekday_py : int
        A current Python's weekday value (Monday is 0).

    References
    ----------
    - DateTime class
        - https://simon-ritchie.github.io/apysc/en/datetime.html
    - DateTime class year property
        - https://simon-ritchie.github.io/apysc/en/datetime_year.html
    - DateTime class month property
        - https://simon-ritchie.github.io/apysc/en/datetime_month.html
    - DateTime class day property
        - https://simon-ritchie.github.io/apysc/en/datetime_day.html
    - DateTime class hour property
        - https://simon-ritchie.github.io/apysc/en/datetime_hour.html
    - DateTime class minute property
        - https://simon-ritchie.github.io/apysc/en/datetime_minute.html
    - DateTime class second property
        - https://simon-ritchie.github.io/apysc/en/datetime_second.html
    - DateTime class millisecond property
        - https://simon-ritchie.github.io/apysc/en/datetime_millisecond.html
    - DateTime class weekday_js and weekday_py properties
        - https://simon-ritchie.github.io/apysc/en/datetime_weekday_js_and_weekday_py.html  # noqa
    - DateTime class now interface
        - https://simon-ritchie.github.io/apysc/en/datetime_now.html

    Examples
    --------
    >>> import apysc as ap
    >>> datetime_: ap.DateTime = ap.DateTime(
    ...     year=2022,
    ...     month=12,
    ...     day=5,
    ...     hour=10,
    ...     minute=30,
    ...     second=50,
    ...     millisecond=500,
    ... )
    >>> datetime_.year
    Int(2022)
    >>> datetime_.month
    Int(12)
    >>> datetime_.day
    Int(5)
    >>> datetime_.hour
    Int(10)
    >>> datetime_.minute
    Int(30)
    >>> datetime_.millisecond
    Int(500)
    >>> datetime_.weekday_py
    Int(0)
    >>> datetime_.weekday_js
    Int(1)
    """

    @arg_validation_decos.is_four_digit_year(arg_position_index=1)
    @arg_validation_decos.is_month_int(arg_position_index=2)
    @arg_validation_decos.is_day_int(arg_position_index=3)
    @arg_validation_decos.is_hour_int(arg_position_index=4)
    @arg_validation_decos.is_minute_int(arg_position_index=5)
    @arg_validation_decos.is_second_int(arg_position_index=6)
    @arg_validation_decos.is_millisecond_int(arg_position_index=7)
    @arg_validation_decos.is_builtin_string(arg_position_index=8, optional=False)
    @arg_validation_decos.is_builtin_boolean(arg_position_index=9)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        year: Union[int, Int],
        month: Union[int, Int],
        day: Union[int, Int],
        *,
        hour: Union[int, Int] = 0,
        minute: Union[int, Int] = 0,
        second: Union[int, Int] = 0,
        millisecond: Union[int, Int] = 0,
        variable_name_suffix: str = "",
        skip_init_substitution_expression_appending: bool = False,
    ) -> None:
        """
        The class for datetime-related interfaces.

        Parameters
        ----------
        year : Union[int, Int]
            Four-digit year.
        month : Union[int, Int]
            Two-digit month (1 to 12).
        day : Union[int, Int]
            Two-digit day (1 to 31).
        hour : Optional[Union[int, Int]], optional
            Two-digit hour (0 to 23).
        minute : Optional[Union[int, Int]], optional
            Two-digit minute (0 to 59).
        second : Optional[Union[int, Int]], optional
            Two-digit second (0 to 59).
        millisecond : Optional[Union[int, Int]], optional
            Millisecond (0 to 999).
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        skip_init_substitution_expression_appending : bool, default False
            A boolean indicates whether to skip an initial substitution
            expression or not. The `DateTime` class uses this option internally.

        References
        ----------
        - DateTime class
            - https://simon-ritchie.github.io/apysc/en/datetime.html
        - DateTime class year property
            - https://simon-ritchie.github.io/apysc/en/datetime_year.html
        - DateTime class month property
            - https://simon-ritchie.github.io/apysc/en/datetime_month.html
        - DateTime class day property
            - https://simon-ritchie.github.io/apysc/en/datetime_day.html
        - DateTime class hour property
            - https://simon-ritchie.github.io/apysc/en/datetime_hour.html
        - DateTime class minute property
            - https://simon-ritchie.github.io/apysc/en/datetime_minute.html
        - DateTime class second property
            - https://simon-ritchie.github.io/apysc/en/datetime_second.html
        - DateTime class millisecond property
            - https://simon-ritchie.github.io/apysc/en/datetime_millisecond.html
        - DateTime class weekday_js and weekday_py properties
            - https://simon-ritchie.github.io/apysc/en/datetime_weekday_js_and_weekday_py.html  # noqa
        - DateTime class now interface
            - https://simon-ritchie.github.io/apysc/en/datetime_now.html

        Examples
        --------
        >>> import apysc as ap
        >>> datetime_: ap.DateTime = ap.DateTime(
        ...     year=2022,
        ...     month=12,
        ...     day=5,
        ...     hour=10,
        ...     minute=30,
        ...     second=50,
        ...     millisecond=500,
        ... )
        >>> datetime_.year
        Int(2022)
        >>> datetime_.month
        Int(12)
        >>> datetime_.day
        Int(5)
        >>> datetime_.hour
        Int(10)
        >>> datetime_.minute
        Int(30)
        >>> datetime_.millisecond
        Int(500)
        >>> datetime_.weekday_py
        Int(0)
        >>> datetime_.weekday_js
        Int(1)
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        from apysc._expression.event_handler_scope import TemporaryNotHandlerScope

        with TemporaryNotHandlerScope():
            self._variable_name_suffix = variable_name_suffix
            self.variable_name = expression_variables_util.get_next_variable_name(
                type_name=var_names.DATETIME
            )

            self._set_init_year_value(year=year)
            self._set_init_month_value(month=month)
            self._set_init_day_value(day=day)
            self._set_init_hour_value(hour=hour)
            self._set_init_minute_value(minute=minute)
            self._set_init_second_value(second=second)
            self._set_init_millisecond_value(millisecond=millisecond)

            self._append_constructor_expression()

        self._append_initial_substitution_expression_if_in_handler_scope(
            skip_appending=skip_init_substitution_expression_appending,
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_constructor_expression(self) -> None:
        """
        Append a constructor expression.
        """
        import apysc as ap

        expression: str = self._create_initial_substitution_expression()
        expression = f"var {expression}"
        ap.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _create_initial_substitution_expression(self) -> str:
        """
        Create an initial value's substitution expression string.

        Returns
        -------
        expression : str
            Created expression string.
        """
        expression: str = f"{self.variable_name} = new Date("
        expression += self._get_init_year_argument_expression()
        expression += self._get_init_month_argument_expression()
        expression += self._get_init_day_argument_expression()
        expression += self._get_init_hour_argument_expression()
        expression += self._get_init_minute_argument_expression()
        expression += self._get_init_second_argument_expression()
        expression += self._get_init_millisecond_argument_expression()
        expression += ");"
        return expression

    def __sub__(self, other: "DateTime") -> TimeDelta:
        """
        Method for subtraction.

        Parameters
        ----------
        other : DateTime
            The other value to subtract.

        Returns
        -------
        result : TimeDelta
            The duration between two `Datetime` instances.

        Raises
        ------
        TypeError
            If the other value type is not the `DateTime`.
        """
        if not isinstance(other, DateTime):
            raise TypeError(
                "Cannot subtract a `DateTime` instane with a "
                f"`{type(other).__name__}` instance."
            )
        result: TimeDelta = TimeDelta(left_datetime=self, right_datetime=other)
        return result

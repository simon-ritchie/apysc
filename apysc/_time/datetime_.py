"""Class implementations for datetime-related interfaces.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._time.day_mixin import DayMixIn
from apysc._time.hour_mixin import HourMixIn
from apysc._time.millisecond_mixin import MillisecondMixIn
from apysc._time.minute_mixin import MinuteMixIn
from apysc._time.month_mixin import MonthMixIn
from apysc._time.second_mixin import SecondMixIn
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
):
    @arg_validation_decos.is_four_digit_year(arg_position_index=1)
    @arg_validation_decos.is_month_int(arg_position_index=2)
    @arg_validation_decos.is_day_int(arg_position_index=3)
    @arg_validation_decos.is_hour_int(arg_position_index=4)
    @arg_validation_decos.is_minute_int(arg_position_index=5)
    @arg_validation_decos.is_second_int(arg_position_index=6)
    @arg_validation_decos.is_millisecond_int(arg_position_index=7)
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
            This setting is sometimes useful for JavaScript's debugging.
        skip_init_substitution_expression_appending : bool, default False
            A boolean indicates whether to skip an initial substitution
            expression or not. This class uses this option internally.
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

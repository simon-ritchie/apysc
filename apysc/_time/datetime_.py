"""Class implementations for datetime-related interfaces.
"""

from typing import Dict, Optional, Union
from datetime import datetime

from typing_extensions import final

from apysc._type.int import Int
from apysc._validation import arg_validation_decos
from apysc._type.variable_name_interface import VariableNameInterface
from apysc._type.variable_name_suffix_interface import VariableNameSuffixInterface
from apysc._type.initial_substitution_exp_interface import (
    InitialSubstitutionExpInterface,
)
from apysc._type.revert_interface import RevertInterface
from apysc._html.debug_mode import add_debug_info_setting


class DateTime(
    VariableNameInterface,
    RevertInterface,
    VariableNameSuffixInterface,
    InitialSubstitutionExpInterface
):

    _initial_year: Union[int, Int]
    _initial_month: Union[int, Int]
    _initial_day: Union[int, Int]
    _initial_hour: Union[int, Int]
    _initial_minute: Union[int, Int]
    _initial_second: Union[int, Int]
    _initial_millisecond: Union[int, Int]

    _year: Int
    _month: Int
    _day: Int
    _hour: Int
    _minute: Int
    _second: Int
    _millisecond: Int

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
        from apysc._expression.event_handler_scope import TemporaryNotHandlerScope
        from apysc._expression import var_names
        from apysc._expression import expression_variables_util
        with TemporaryNotHandlerScope():
            self._variable_name_suffix = variable_name_suffix
            self.variable_name = expression_variables_util.get_next_variable_name(
                type_name=var_names.DATETIME
            )

            self._initial_year = year
            self._initial_month = month
            self._initial_day = day
            self._initial_hour = hour
            self._initial_minute = minute
            self._initial_second = second
            self._initial_millisecond = millisecond

            self._year = _convert_to_apysc_int(
                value=year, variable_name_suffix=variable_name_suffix
            )
            self._month = _convert_to_apysc_int(
                value=month, variable_name_suffix=variable_name_suffix
            )
            self._day = _convert_to_apysc_int(
                value=day, variable_name_suffix=variable_name_suffix
            )
            self._hour = _convert_to_apysc_int(
                value=hour, variable_name_suffix=variable_name_suffix
            )
            self._minute = _convert_to_apysc_int(
                value=minute, variable_name_suffix=variable_name_suffix
            )
            self._second = _convert_to_apysc_int(
                value=second, variable_name_suffix=variable_name_suffix
            )
            self._millisecond = _convert_to_apysc_int(
                value=millisecond, variable_name_suffix=variable_name_suffix
            )
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
    @classmethod
    @add_debug_info_setting(module_name=__name__)
    def now(cls) -> "DateTime":
        """
        Get a `DateTime` instance of current time.

        Returns
        -------
        now : DateTime
            A `DateTime` instance of current time.
        """

    @final
    def _create_initial_substitution_expression(self) -> str:
        """
        Create an initial value's substitution expression string.

        Returns
        -------
        expression : str
            Created expression string.
        """
        # expression: str = (
        #     f"{self.variable_name} = new Date({self._year.variable_name}, {self._month.variable_name} - 1, {self._day.variable_name}, {self._hour.variable_name}, )"
        # )

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._year._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        self._month._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        self._day._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        self._hour._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        self._minute._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        self._second._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        self._millisecond._run_all_make_snapshot_methods(snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert a value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._year._run_all_revert_methods(snapshot_name=snapshot_name)
        self._month._run_all_revert_methods(snapshot_name=snapshot_name)
        self._day._run_all_revert_methods(snapshot_name=snapshot_name)
        self._hour._run_all_revert_methods(snapshot_name=snapshot_name)
        self._minute._run_all_revert_methods(snapshot_name=snapshot_name)
        self._second._run_all_revert_methods(snapshot_name=snapshot_name)
        self._millisecond._run_all_revert_methods(snapshot_name=snapshot_name)


def _convert_to_apysc_int(
        *, value: Union[int, Int], variable_name_suffix: str,
    ) -> Int:
    """
    Convert a datetime-related value to an apysc integer.

    Parameters
    ----------
    value : Union[int, Int]
        A value to convert.
    variable_name_suffix : str
        A JavaScript variable name suffix string.
        This setting is sometimes useful for JavaScript's debugging.

    Returns
    -------
    value : Int
        A converted value.
    """
    if isinstance(value, int):
        return Int(value, variable_name_suffix=variable_name_suffix)
    return value._copy()

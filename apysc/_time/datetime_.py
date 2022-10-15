"""Class implementations for datetime-related interfaces.
"""

from typing import Optional, Union
from datetime import datetime

from apysc._type.int import Int
from apysc._validation import arg_validation_decos
from apysc._type.variable_name_interface import VariableNameInterface
from apysc._type.variable_name_suffix_interface import VariableNameSuffixInterface


class DateTime(VariableNameInterface, VariableNameSuffixInterface):

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
    @arg_validation_decos.is_hour_int(arg_position_index=4, optional=True)
    @arg_validation_decos.is_minute_int(arg_position_index=5, optional=True)
    @arg_validation_decos.is_second_int(arg_position_index=6, optional=True)
    @arg_validation_decos.is_millisecond_int(arg_position_index=7, optional=True)
    def __init__(
        self,
        year: Union[int, Int],
        month: Union[int, Int],
        day: Union[int, Int],
        *,
        hour: Optional[Union[int, Int]] = None,
        minute: Optional[Union[int, Int]] = None,
        second: Optional[Union[int, Int]] = None,
        millisecond: Optional[Union[int, Int]] = None,
        variable_name_suffix: str = "",
    ) -> None:
        """
        The class for datetime-related interfaces.

        Parameters
        ----------
        year : Union[int, Int]
            Four-digit year.
        month : Union[int, Int]
            Two-digit month (0 to 23).
        day : Union[int, Int]
            Two-digit day (0 to 31).
        hour : Optional[Union[int, Int]], optional
            Two-digit hour (0 to 23). This value becomes 0 if this value is None.
        minute : Optional[Union[int, Int]], optional
            Two-digit minute (0 to 59). This value becomes 0 if this value is None.
        second : Optional[Union[int, Int]], optional
            Two-digit second (0 to 59). This value becomes 0 if this value is None.
        millisecond : Optional[Union[int, Int]], optional
            Millisecond (0 to 999). This value becomes 0 if this value is None.
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript's debugging.
        """
        from apysc._expression.event_handler_scope import TemporaryNotHandlerScope
        from apysc._expression import var_names
        from apysc._expression import expression_variables_util
        with TemporaryNotHandlerScope():
            self._variable_name_suffix = variable_name_suffix
            self.variable_name = expression_variables_util.get_next_variable_name(
                type_name=var_names.DATETIME
            )

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

    @classmethod
    def now(cls) -> "DateTime":
        """
        Get a `DateTime` instance of current time.

        Returns
        -------
        now : DateTime
            A `DateTime` instance of current time.
        """


def _convert_to_apysc_int(
        *, value: Optional[Union[int, Int]], variable_name_suffix: str,
    ) -> Int:
    """
    Convert a datetime-related value to an apysc integer.

    Parameters
    ----------
    value : Optional[Union[int, Int]]
        A value to convert.
    variable_name_suffix : str
        A JavaScript variable name suffix string.
        This setting is sometimes useful for JavaScript's debugging.

    Returns
    -------
    value : Int
        A converted value.
    """
    if value is None:
        return Int(0, variable_name_suffix=variable_name_suffix)
    if isinstance(value, int):
        return Int(value, variable_name_suffix=variable_name_suffix)
    return value._copy()

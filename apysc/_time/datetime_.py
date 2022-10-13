"""Class implementations for datetime-related interfaces.
"""

from typing import Optional, Union
from datetime import datetime

from apysc._type.int import Int
from apysc._validation import arg_validation_decos


class DateTime:

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
        """
        self._year = _convert_to_apysc_int(value=year)
        self._month = _convert_to_apysc_int(value=month)
        self._day = _convert_to_apysc_int(value=day)
        self._hour = _convert_to_apysc_int(value=hour)
        self._minute = _convert_to_apysc_int(value=minute)
        self._second = _convert_to_apysc_int(value=second)
        self._millisecond = _convert_to_apysc_int(value=millisecond)

    @classmethod
    def now(cls) -> "DateTime":
        """
        Get a `DateTime` instance of current time.

        Returns
        -------
        now : DateTime
            A `DateTime` instance of current time.
        """


def _convert_to_apysc_int(*, value: Optional[Union[int, Int]]) -> Int:
    """
    Convert a datetime-related value to an apysc integer.

    Parameters
    ----------
    value : Optional[Union[int, Int]]
        A value to convert.

    Returns
    -------
    value : Int
        A converted value.
    """
    if value is None:
        return Int(0)
    if isinstance(value, int):
        return Int(value)
    return value._copy()

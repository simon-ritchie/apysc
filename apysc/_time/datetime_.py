"""Class implementations for datetime-related interfaces.
"""

from typing import Optional, Union
from datetime import datetime

from apysc._type.int import Int


class DateTime:

    _year: Int
    _month: Int
    _day: Int
    _hour: Int
    _minute: Int
    _second: Int
    _millisecond: Int

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
        self._year = _convert_to_apysc_int(value=year)
        pass

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

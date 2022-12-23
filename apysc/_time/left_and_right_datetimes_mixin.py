"""Class implementations for the left and right datetimes-related mix-in.
"""

from datetime import datetime
from typing import TYPE_CHECKING
from typing import Tuple

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting

if TYPE_CHECKING:
    from apysc._time.datetime_ import DateTime


class LeftAndRightDatetimesMixIn:
    @add_debug_info_setting(module_name=__name__)
    @final
    def _get_left_and_right_py_datetimes_from_apysc_datetime(
        self,
        *,
        left_apysc_datetime: "DateTime",
        right_apysc_datetime: "DateTime",
    ) -> Tuple[datetime, datetime]:
        """
        Get Python's left and right datetimes from specified apysc's
        `DateTime` instances.

        Parameters
        ----------
        left_apysc_datetime : DateTime
            Left-side apysc's `DateTime` instance.
        right_apysc_datetime : DateTime
            Right-side apysc's `DateTime` instance.

        Returns
        -------
        left_py_datetime : datetime
            Left-side Python's datetime instance.
        right_py_datetime : datetime
            Right-side Python's datetime instance.
        """
        left_py_datetime: datetime = datetime(
            left_apysc_datetime._year._value,
            left_apysc_datetime._month._value,
            left_apysc_datetime._day._value,
            left_apysc_datetime._hour._value,
            left_apysc_datetime._minute._value,
            left_apysc_datetime._second._value,
            left_apysc_datetime._millisecond._value * 1000,
        )
        right_py_datetime: datetime = datetime(
            right_apysc_datetime._year._value,
            right_apysc_datetime._month._value,
            right_apysc_datetime._day._value,
            right_apysc_datetime._hour._value,
            right_apysc_datetime._minute._value,
            right_apysc_datetime._second._value,
            right_apysc_datetime._millisecond._value * 1000,
        )
        return left_py_datetime, right_py_datetime

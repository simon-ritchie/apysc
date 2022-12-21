"""Class implementations for the total seconds-related mix-in.
"""

from typing import Union
from typing import TYPE_CHECKING
from datetime import datetime, timedelta

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos

if TYPE_CHECKING:
    from apysc._time.datetime_ import DateTime


class TotalSecondsMixIn(VariableNameMixIn):

    _total_seconds_value: float

    @final
    @arg_validation_decos.is_apysc_datetime(arg_position_index=1)
    @arg_validation_decos.is_apysc_datetime(arg_position_index=2)
    @add_debug_info_setting(module_name=__name__)
    def _set_init_total_seconds_value_for_python(
        self,
        *,
        left_datetime: "DateTime",
        right_datetime: "DateTime",
    ) -> None:
        """
        Set an initial total seconds value for Python.

        Parameters
        ----------
        left_datetime : DateTime
            A left-side `DateTime` instance to compare.
        right_datetime : DateTime
            A right-side `DateTime` instance to compare.
        """
        left_py_datetime: datetime = datetime(
            left_datetime._year._value,
            left_datetime._month._value,
            left_datetime._day._value,
            left_datetime._hour._value,
            left_datetime._minute._value,
            left_datetime._second._value,
            left_datetime._millisecond._value * 1000,
        )
        right_py_datetime: datetime = datetime(
            right_datetime._year._value,
            right_datetime._month._value,
            right_datetime._day._value,
            right_datetime._hour._value,
            right_datetime._minute._value,
            right_datetime._second._value,
            right_datetime._millisecond._value * 1000,
        )
        timedelta_: timedelta = left_py_datetime - right_py_datetime
        self._total_seconds_value = timedelta_.total_seconds()

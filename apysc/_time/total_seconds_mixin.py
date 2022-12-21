"""Class implementations for the total seconds-related mix-in.
"""

from datetime import datetime
from datetime import timedelta
from typing import TYPE_CHECKING

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn
from apysc._validation import arg_validation_decos

if TYPE_CHECKING:
    from apysc._time.datetime_ import DateTime


class TotalSecondsMixIn(VariableNameMixIn, VariableNameSuffixAttrMixIn):

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

    @final
    @add_debug_info_setting(module_name=__name__)
    def total_seconds(self) -> Number:
        """
        Get the total seconds in the duration.

        Returns
        -------
        total_seconds : Number
            Total seconds in the duration.
        """
        suffix: str = self._get_attr_variable_name_suffix(
            attr_identifier="total_seconds"
        )
        total_seconds: Number = Number(
            0,
            variable_name_suffix=suffix,
        )
        total_seconds._value = self._total_seconds_value
        self._append_total_seconds_expression(total_seconds=total_seconds)
        return total_seconds

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_total_seconds_expression(self, *, total_seconds: Number) -> None:
        """
        Append a total seconds' expression string.

        Parameters
        ----------
        total_seconds : Number
            Total seconds value.
        """
        import apysc as ap

        expression: str = (
            f"{total_seconds.variable_name} = {self.variable_name} / 1000;"
        )
        ap.append_js_expression(expression=expression)

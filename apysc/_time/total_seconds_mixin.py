"""Class implementations for the total seconds-related mix-in.
"""

from datetime import datetime
from datetime import timedelta
from typing import TYPE_CHECKING

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._time.left_and_right_datetimes_mixin import LeftAndRightDatetimesMixIn
from apysc._type.number import Number
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._validation import arg_validation_decos

if TYPE_CHECKING:
    from apysc._time.datetime_ import DateTime


class TotalSecondsMixIn(
    VariableNameMixIn,
    VariableNameSuffixAttrOrVarMixIn,
    LeftAndRightDatetimesMixIn,
):

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
        left_py_datetime: datetime
        right_py_datetime: datetime
        (
            left_py_datetime,
            right_py_datetime,
        ) = self._get_left_and_right_py_datetimes_from_apysc_datetime(
            left_apysc_datetime=left_datetime,
            right_apysc_datetime=right_datetime,
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

        Examples
        --------
        >>> import apysc as ap
        >>> datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)
        >>> datetime_2: ap.DateTime = ap.DateTime(2022, 12, 6)
        >>> timedelta_: ap.TimeDelta = datetime_1 - datetime_2
        >>> timedelta_.total_seconds()
        Number(86400.0)

        References
        ----------
        - TimeDelta class
            - https://simon-ritchie.github.io/apysc/en/timedelta.html
        - TimeDelta class total_seconds interface
            - https://simon-ritchie.github.io/apysc/en/timedelta_total_seconds.html
        """
        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="total_seconds"
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

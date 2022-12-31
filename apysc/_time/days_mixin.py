"""Class implementations for the days-related mix-in.
"""

from datetime import datetime
from datetime import timedelta
from typing import TYPE_CHECKING

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._time.left_and_right_datetimes_mixin import LeftAndRightDatetimesMixIn
from apysc._type.int import Int
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._validation import arg_validation_decos

if TYPE_CHECKING:
    from apysc._time.datetime_ import DateTime


class DaysMixIn(
    VariableNameMixIn,
    VariableNameSuffixAttrOrVarMixIn,
    LeftAndRightDatetimesMixIn,
):

    _days_value: int

    @final
    @arg_validation_decos.is_apysc_datetime(arg_position_index=1)
    @arg_validation_decos.is_apysc_datetime(arg_position_index=2)
    @add_debug_info_setting(module_name=__name__)
    def _set_init_days_value_for_python(
        self,
        *,
        left_datetime: "DateTime",
        right_datetime: "DateTime",
    ) -> None:
        """
        Set an initial days value for Python.

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
        self._days_value = timedelta_.days

    @property
    @add_debug_info_setting(module_name=__name__)
    def days(self) -> Int:
        """
        Get days in the duration.

        Returns
        -------
        days : Int
            Days value. This interface ignores a fraction.

        Examples
        --------
        >>> import apysc as ap
        >>> datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)
        >>> datetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)
        >>> timedelta_: ap.TimeDelta = datetime_1 - datetime_2
        >>> timedelta_.days
        Int(2)

        References
        ----------
        - TimeDelta class
            - https://simon-ritchie.github.io/apysc/en/timedelta.html
        - TimeDelta class days interface
            - https://simon-ritchie.github.io/apysc/en/timedelta_days.html
        """
        days: Int = Int(0)
        days._value = self._days_value
        self._append_days_expression(days=days)
        return days

    @final
    @arg_validation_decos.is_apysc_integer(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def _append_days_expression(self, *, days: Int) -> None:
        """
        Append days' expression string.

        Parameters
        ----------
        days : Int
            Target days value.
        """
        import apysc as ap

        expression: str = (
            f"{days.variable_name} = Math.trunc({self.variable_name} / "
            "(1000 * 60 * 60 * 24));"
        )
        ap.append_js_expression(expression=expression)

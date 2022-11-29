"""Class implementations for the weekday-related mix-in.
"""

from datetime import datetime

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn


class WeekdayMixin(VariableNameMixIn, VariableNameSuffixAttrMixIn):

    _year: Int
    _month: Int
    _day: Int

    @property
    @add_debug_info_setting(module_name=__name__)
    def weekday_js(self) -> Int:
        """
        Get a current weekday value. This interface sets the weekday based on the
        JavaScript value as follows:

        - 0 -> Sunday
        - 1 -> Monday
        - 2 -> Tuesday
        - 3 -> Wednesday
        - 4 -> Thursday
        - 5 -> Friday
        - 6 -> Saturday

        Returns
        -------
        weekday : Int
            A current weekday value.
        """
        weekday: Int = Int(0)
        weekday_js_val: int = self._get_weekday_js_val_with_attrs()
        pass

    @final
    def _get_weekday_js_val_with_attrs(self) -> int:
        """
        Get a current JavaScript weekday's integer value with the year, month,
        and day attributes.

        Returns
        -------
        weekday_js_val : int
            A current JavaScript weekday's integer value.
        """
        if (
            not hasattr(self, "_year")
            or not hasattr(self, "_month")
            or not hasattr(self, "_day")
        ):
            return 0
        datetime_: datetime = datetime(
            self._year._value, self._month._value, self._day._value
        )
        weekday_js_val: int = datetime_.weekday() + 1
        if weekday_js_val == 7:
            weekday_js_val = 0
        return weekday_js_val

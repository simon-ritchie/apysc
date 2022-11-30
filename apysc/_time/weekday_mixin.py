"""Class implementations for the weekday-related mix-in.
"""

from datetime import datetime

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.variable_name_mixin import VariableNameMixIn


class WeekdayMixIn(VariableNameMixIn):

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
        weekday._value = weekday_js_val
        self._append_weekday_js_getter_expression(weekday_val=weekday)
        return weekday

    @final
    def _append_weekday_js_getter_expression(self, *, weekday_val: Int) -> None:
        """
        Append a JavaScript weekday's getter expression string.

        Parameters
        ----------
        weekday_val : Int
            A weekday value to use in an expression.
        """
        import apysc as ap

        expression: str = (
            f"{weekday_val.variable_name} = {self.variable_name}.getDay();"
        )
        ap.append_js_expression(expression=expression)

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

    @property
    @add_debug_info_setting(module_name=__name__)
    def weekday_py(self) -> Int:
        """
        get a current weekday value. This interface sets the weekday based on the
        Python value as follows:

        - 0 -> Monday
        - 1 -> Thursday
        - 2 -> Wednesday
        - 3 -> Thursday
        - 4 -> Friday
        - 5 -> Saturday
        - 6 -> Sunday

        Returns
        -------
        weekday : Int
            A current weekday value.
        """
        weekday: Int = Int(0)
        weekday_py_val: int = self._get_weekday_py_val_with_attrs()
        weekday._value = weekday_py_val
        self._append_weekday_py_getter_expression(weekday_val=weekday)
        return weekday

    @final
    def _append_weekday_py_getter_expression(self, *, weekday_val: Int) -> None:
        """
        Append a Python weekday's getter expression string.

        Parameters
        ----------
        weekday_val : Int
            A weekday value to use in an expression.
        """
        import apysc as ap

        expression: str = (
            f"{weekday_val.variable_name} = {self.variable_name}.getDay() - 1;"
            f"\nif ({weekday_val.variable_name} === -1) {{"
            f"\n  {weekday_val.variable_name} = 6;"
            "\n}"
        )
        ap.append_js_expression(expression=expression)

    @final
    def _get_weekday_py_val_with_attrs(self) -> int:
        """
        Append a Python weekday's getter expression string.

        Returns
        -------
        weekday_py_val : int
            A current Python weekday's integer value.
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
        return datetime_.weekday()

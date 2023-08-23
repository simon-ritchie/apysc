"""Class implementations for the month-end related mix-in.
"""

import calendar

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.variable_name_mixin import VariableNameMixIn


class MonthEndMixin(VariableNameMixIn):
    _year: Int
    _month: Int
    _day: Int

    @final
    @add_debug_info_setting(module_name=__name__)
    def set_month_end(self) -> None:
        """
        Set a month-end day.

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)
        >>> datetime_.set_month_end()
        >>> datetime_.day
        Int(31)

        References
        ----------
        - DateTime class set_month_end interface
            - https://simon-ritchie.github.io/apysc/en/datetime_set_month_end.html
        """
        from apysc._expression import expression_data_util

        variable_name: str = self.variable_name
        expression: str = (
            f"{variable_name}.setDate(1);"
            f"\n{variable_name}.setMonth({variable_name}.getMonth() + 1);"
            f"\n{variable_name}.setDate(0);"
        )
        expression_data_util.append_js_expression(expression=expression)
        month_end_day: int = calendar.monthrange(
            year=self._year._value,
            month=self._month._value,
        )[1]
        self._day._value = month_end_day

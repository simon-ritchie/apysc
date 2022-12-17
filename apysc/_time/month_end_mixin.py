"""Class implementations for the month-end related mix-in.
"""

from typing import Union
import calendar

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn
from apysc._validation import arg_validation_decos
from apysc._type.int import Int


class MonthEndMixin(VariableNameMixIn):

    _year: Int
    _month: Int
    _day: Int

    @final
    @add_debug_info_setting(module_name=__name__)
    def set_month_end(self) -> None:
        import apysc as ap
        variable_name: str = self.variable_name
        expression: str = (
            f"{variable_name}.setDate(1);"
            f"\n{variable_name}.setMonth({variable_name}.getMonth() + 1);"
            f"\n{variable_name}.setDate(0);"
        )
        ap.append_js_expression(expression=expression)
        month_end_day: int = calendar.monthrange(
            year=self._year._value,
            month=self._month._value,
        )[1]
        self._day._value = month_end_day

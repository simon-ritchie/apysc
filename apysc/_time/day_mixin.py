"""Class implementations for the day-related mix-in.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn
from apysc._validation import arg_validation_decos


class DayMixIn(VariableNameSuffixAttrMixIn):

    _initial_day: Union[int, Int]
    _day: Int

    @final
    @add_debug_info_setting(module_name=__name__)
    @arg_validation_decos.is_day_int(arg_position_index=1)
    def _set_init_day_value(self, *, day: Union[int, Int]) -> None:
        """
        Set an initial day value.

        Parameters
        ----------
        day : Union[int, Int]
            A day value to set.
        """
        from apysc._converter.to_apysc_val_from_builtin import (
            get_copied_int_from_builtin_val,
        )

        self._initial_day = day
        suffix: str = self._get_attr_variable_name_suffix(attr_identifier="day")
        self._day = get_copied_int_from_builtin_val(
            integer=day, variable_name_suffix=suffix
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _get_init_day_argument_expression(self) -> str:
        """
        Get an initial day's argument expression string.

        Returns
        -------
        expression : str
            A created expression string.
        """
        if isinstance(self._initial_day, Int):
            return f", {self._initial_day.variable_name}"
        return f", {self._day._value}"

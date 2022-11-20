"""Class implementations for the minute-related mix-in.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn
from apysc._validation import arg_validation_decos


class MinuteMixIn(VariableNameSuffixAttrMixIn):

    _initial_minute: Union[int, Int]
    _minute: Int

    @final
    @add_debug_info_setting(module_name=__name__)
    @arg_validation_decos.is_minute_int(arg_position_index=1)
    def _set_init_minute_value(self, *, minute: Union[int, Int]) -> None:
        """
        Set an initial minute value.

        Parameters
        ----------
        minute : Union[int, Int]
            A minute value to set.
        """
        from apysc._converter.to_apysc_val_from_builtin import (
            get_copied_int_from_builtin_val,
        )

        self._initial_minute = minute
        suffix: str = self._get_attr_variable_name_suffix(attr_identifier="minute")
        self._minute = get_copied_int_from_builtin_val(
            integer=minute, variable_name_suffix=suffix
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _get_init_minute_argument_expression(self) -> str:
        """
        Get an initial minute's argument expression string.

        Returns
        -------
        expression : str
            A created expression string.
        """
        if isinstance(self._initial_minute, Int):
            return f", {self._initial_minute.variable_name}"
        return f", {self._minute._value}"

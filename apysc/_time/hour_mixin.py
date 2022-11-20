"""Class implementations for the hour-related mix-in.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn
from apysc._validation import arg_validation_decos


class HourMixIn(VariableNameSuffixAttrMixIn):

    _initial_hour: Union[int, Int]
    _hour: Int

    @final
    @add_debug_info_setting(module_name=__name__)
    @arg_validation_decos.is_hour_int(arg_position_index=1)
    def _set_init_hour_value(self, *, hour: Union[int, Int]) -> None:
        """
        Set an initial hour value.

        Parameters
        ----------
        hour : Union[int, Int]
            An hour value to set.
        """
        from apysc._converter.to_apysc_val_from_builtin import (
            get_copied_int_from_builtin_val,
        )

        self._initial_hour = hour
        suffix: str = self._get_attr_variable_name_suffix(attr_identifier="hour")
        self._hour = get_copied_int_from_builtin_val(
            integer=hour, variable_name_suffix=suffix
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _get_init_hour_argument_expression(self) -> str:
        """
        Get an initial hour's argument expression string.

        Returns
        -------
        expression : str
            A created expression string.
        """
        if isinstance(self._initial_hour, Int):
            return f", {self._initial_hour.variable_name}"
        return f", {self._hour._value}"

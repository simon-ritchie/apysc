"""Class implementations for the millisecond-related mix-in.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn
from apysc._validation import arg_validation_decos


class MillisecondMixIn(VariableNameSuffixAttrMixIn):

    _initial_millisecond: Union[int, Int]
    _millisecond: Int

    @final
    @add_debug_info_setting(module_name=__name__)
    @arg_validation_decos.is_millisecond_int(arg_position_index=1)
    def _set_init_millisecond_value(self, *, millisecond: Union[int, Int]) -> None:
        """
        Set an initial millisecond value.

        Parameters
        ----------
        millisecond : Union[int, Int]
            A millisecond value to set.
        """
        from apysc._converter.to_apysc_val_from_builtin import (
            get_copied_int_from_builtin_val,
        )

        self._initial_millisecond = millisecond
        suffix: str = self._get_attr_variable_name_suffix(
            attr_identifier="millisecond"
        )
        self._millisecond = get_copied_int_from_builtin_val(
            integer=millisecond, variable_name_suffix=suffix,
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _get_init_millisecond_argument_expression(self) -> str:
        """
        Get an initial millisecond argument expression string.

        Returns
        -------
        expression : str
            A created expression string.
        """
        if isinstance(self._initial_millisecond, Int):
            return f", {self._initial_millisecond.variable_name}"
        return f", {self._millisecond._value}"

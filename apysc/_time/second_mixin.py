"""Class implementations for the second-related mix-in.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn
from apysc._validation import arg_validation_decos


class SecondMixIn(VariableNameSuffixAttrMixIn):

    _initial_second: Union[int, Int]
    _second: Int

    @final
    @add_debug_info_setting(module_name=__name__)
    @arg_validation_decos.is_second_int(arg_position_index=1)
    def _set_init_second_value(self, *, second: Union[int, Int]) -> None:
        """
        Set an initial second value.

        Parameters
        ----------
        second : Union[int, Int]
            A second value to set.
        """
        from apysc._converter.to_apysc_val_from_builtin import (
            get_copied_int_from_builtin_val,
        )

        self._initial_second = second
        suffix: str = self._get_attr_variable_name_suffix(attr_identifier="second")
        self._second = get_copied_int_from_builtin_val(
            integer=second, variable_name_suffix=suffix
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _get_init_second_argument_expression(self) -> str:
        """
        Get an initial second argument expression string.

        Returns
        -------
        expression : str
            A created expression string.
        """
        if isinstance(self._initial_second, Int):
            return f", {self._initial_second.variable_name}"
        return f", {self._second._value}"

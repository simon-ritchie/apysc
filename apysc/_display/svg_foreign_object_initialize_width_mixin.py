"""The mix-in class for the `foreignObject`'s width initialization method.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int


class SvgForeignObjectInitializeWidthMixIn:
    _width: Int

    @final
    @add_debug_info_setting(module_name=__name__)
    def _initialize_width(
        self,
        *,
        width: Union[int, Int],
    ) -> None:
        """
        Initialize the width attribute with the specified argument.

        Parameters
        ----------
        width : Union[int, Int]
            Element width value.
        """
        from apysc._converter import to_apysc_val_from_builtin
        from apysc._type.variable_name_suffix_attr_or_var_mixin import (
            VariableNameSuffixAttrOrVarMixIn,
        )

        suffix: str = ""
        if isinstance(self, VariableNameSuffixAttrOrVarMixIn):
            suffix = self._get_attr_or_variable_name_suffix(value_identifier="width")
        width_: Int = to_apysc_val_from_builtin.get_copied_int_from_builtin_val(
            integer=width,
            variable_name_suffix=suffix,
        )
        self._width = width_

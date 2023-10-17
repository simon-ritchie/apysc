"""The mix-in class for the `foreignObject`'s width and height
initialization method.
"""


from typing import Union

from apysc._type.int import Int
from typing_extensions import final
from apysc._html.debug_mode import add_debug_info_setting


class SVGForeignObjectInitializeWidthAndHeightMixIn:
    @final
    @add_debug_info_setting(module_name=__name__)
    def _initialize_width_and_height(
        self,
        *,
        width: Union[int, Int],
        height: Union[int, Int],
    ) -> None:
        from apysc._type.variable_name_suffix_attr_or_var_mixin import (
            VariableNameSuffixAttrOrVarMixIn
        )
        from apysc._converter import to_apysc_val_from_builtin

        suffix: str = ""
        if isinstance(self, VariableNameSuffixAttrOrVarMixIn):
            suffix = self._get_attr_or_variable_name_suffix(
                value_identifier="width"
            )
        width_: Int = to_apysc_val_from_builtin.get_copied_int_from_builtin_val(
            integer=width,
            variable_name_suffix=suffix,
        )
        if isinstance(self, VariableNameSuffixAttrOrVarMixIn):
            suffix = self._get_attr_or_variable_name_suffix(
                value_identifier="height"
            )
        height_: Int = to_apysc_val_from_builtin.get_copied_int_from_builtin_val(
            integer=height,
            variable_name_suffix=suffix,
        )
        self._width = width_
        self._height = height_

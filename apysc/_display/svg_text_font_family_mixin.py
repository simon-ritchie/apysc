"""Class implementation for the SVG text's font-family mix-in.
"""

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.string import String
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos
from apysc._type.array import Array


class SVGTextFontFamilyMixIn(
    VariableNameMixIn,
):

    _font_family: Array[String]

    def _initialize_font_family_if_not_initialized(self) -> None:
        """
        Initialize the `_font_family` attribute if this instance
        does not initialize it yet.
        """
        from apysc._type.variable_name_suffix_attr_or_var_mixin import (
            VariableNameSuffixAttrOrVarMixIn,
        )
        if hasattr(self, "_font_family"):
            return
        suffix: str = ""
        if isinstance(self, VariableNameSuffixAttrOrVarMixIn):
            suffix = self._get_attr_or_variable_name_suffix(
                value_identifier="font_family"
            )
        self._font_family = Array([String("")], variable_name_suffix=suffix)

    @property
    @add_debug_info_setting(module_name=__name__)
    def font_family(self) -> Array[String]:
        self._initialize_font_family_if_not_initialized()
        pass

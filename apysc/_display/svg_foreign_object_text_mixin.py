"""The mix-in implementation for the `foreignObject`'s text property.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.string import String
from apysc._validation import arg_validation_decos


class SvgForeignObjectTextMixIn:
    _text: String

    @final
    @arg_validation_decos.is_string(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _initialize_text(self, *, text: Union[str, String]) -> None:
        """
        Initialize the `_text` attribute.

        Parameters
        ----------
        text : Union[str, String]
            Text value. An HTML tag is available.
        """
        from apysc._converter import to_apysc_val_from_builtin
        from apysc._type.variable_name_suffix_attr_or_var_mixin import (
            VariableNameSuffixAttrOrVarMixIn,
        )

        suffix: str = ""
        if isinstance(self, VariableNameSuffixAttrOrVarMixIn):
            suffix = self._get_attr_or_variable_name_suffix(value_identifier="text")
        self._text = to_apysc_val_from_builtin.get_copied_string_from_builtin_val(
            string=text,
            variable_name_suffix=suffix,
        )
        self._text = (
            String("<span>", variable_name_suffix=suffix)
            + self._text
            + String("</span>", variable_name_suffix=suffix)
        )

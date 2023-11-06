"""Class implementation for the SVG text's font-family mix-in.
"""

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.array import Array
from apysc._type.string import String
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos


class SvgTextFontFamilyMixIn(
    VariableNameMixIn,
):
    @property
    @add_debug_info_setting(module_name=__name__)
    def font_family(self) -> Array[String]:
        """
        Get a current font-family settings.

        Returns
        -------
        font_family : Array[String]
            A current font-family settings.
            Each string in an array contains a font name (e.g., `Times New Roman`).
        """
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        suffix: str = get_attr_or_variable_name_suffix(
            instance=self,
            value_identifier="font_family",
        )
        font_family_string: String = String("", variable_name_suffix=suffix)
        self._append_font_family_string_getter_expression(
            font_family_string=font_family_string
        )

        font_family: Array[String] = font_family_string.split(sep=String(","))
        return font_family

    @font_family.setter
    @add_debug_info_setting(module_name=__name__)
    @arg_validation_decos.is_apysc_string_array(arg_position_index=1, optional=False)
    def font_family(self, value: Array[String]) -> None:
        """
        Set a font-family settings.

        Parameters
        ----------
        value : Array[String]
            A font-family setting.
            Each string in an array needs to be a font name (e.g., `Times New Roman`).
        """
        from apysc._expression import expression_data_util

        font_family_str: String = value.join(sep=String(","))
        expression: str = (
            f'{self.variable_name}.font({{"family": {font_family_str.variable_name}}});'
        )
        expression_data_util.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_font_family_string_getter_expression(
        self,
        *,
        font_family_string: String,
    ) -> None:
        """
        Append a font-family string's getter expression string.

        Parameters
        ----------
        font_family_string : String
            _description_
        """
        from apysc._expression import expression_data_util

        expression: str = (
            f"{font_family_string.variable_name} = "
            f'{self.variable_name}.font("family");'
        )
        expression_data_util.append_js_expression(expression=expression)

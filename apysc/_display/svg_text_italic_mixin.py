"""Class implementation for the SVG text's italic mix-in.
"""

from typing import Dict

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos
from apysc._type.boolean import Boolean


class SVGTextItalicMixIn(
    VariableNameMixIn,
):

    _italic: bool = False

    @property
    @add_debug_info_setting(module_name=__name__)
    def italic(self) -> Boolean:
        """
        Get a boolean value indicating whether a text is italic style or not.

        Returns
        -------
        italic_ : Boolean
            A boolean value indicating whether a text is italic style or not.
        """
        import apysc as ap
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        suffix: str = get_attr_or_variable_name_suffix(
            instance=self,
            value_identifier="italic",
        )
        italic_: Boolean = Boolean(self._italic, variable_name_suffix=suffix)
        expression: str = (
            f'{italic_.variable_name} = '
            f'{self.variable_name}.font("style") === "italic";'
        )
        ap.append_js_expression(expression=expression)
        return italic_

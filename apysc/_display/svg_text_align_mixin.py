"""Class implementation for the SVG text's align mix-in.
"""

from typing import Dict
from enum import Enum

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos


class SVGTextAlign(Enum):
    """
    SVG text's align enum class.

    Attributes
    ----------
    LEFT : str
        An enum definition to align left-position.
    CENTER : str
        An enum definition to align center-position.
    RIGHT : str
        An enum definition to align right-position.
    """
    LEFT = "start"
    CENTER = "middle"
    RIGHT = "end"


class SVGTextAlignMixIn(
    VariableNameMixIn,
):

    _align: SVGTextAlign = SVGTextAlign.LEFT

    @property
    @add_debug_info_setting(module_name=__name__)
    def align(self) -> SVGTextAlign:
        """
        Get a current text-align setting.

        Returns
        -------
        align : SVGTextAlign
            A current text-align setting.
        """
        return self._align

    @align.setter
    @add_debug_info_setting(module_name=__name__)
    def align(self, value: SVGTextAlign) -> None:
        """
        Set a text-align setting.

        Parameters
        ----------
        value : SVGTextAlign
            A text-align setting.
        """
        import apysc as ap

        self._align = value
        expression: str = f'{self.variable_name}.font("anchor", "{value.value}");'
        ap.append_js_expression(expression=expression)

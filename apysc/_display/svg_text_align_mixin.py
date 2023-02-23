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

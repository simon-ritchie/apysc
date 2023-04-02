"""The rectangle's geometry class implementation.
"""

from typing import Any
from typing import Dict
from typing import Optional
from typing import Union

from typing_extensions import final
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.number import Number
from apysc._type.int import Int
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos
from apysc._geom.rectangle_geom_left_x_mixin import RectangleGeomLeftXMixIn
from apysc._geom.rectangle_geom_center_x_mixin import RectangleGeomCenterXMixIn


class RectangleGeom(
    VariableNameSuffixAttrOrVarMixIn,
    VariableNameMixIn,
    VariableNameSuffixMixIn,
    RectangleGeomLeftXMixIn,
    RectangleGeomCenterXMixIn,
):
    """
    The rectangle's geometry class.
    """

    @final
    # left_x
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    # center_x
    @arg_validation_decos.is_apysc_num(arg_position_index=2)
    # right_x
    @arg_validation_decos.is_apysc_num(arg_position_index=3)
    # top_y
    @arg_validation_decos.is_apysc_num(arg_position_index=4)
    # center_y
    @arg_validation_decos.is_apysc_num(arg_position_index=5)
    # bottom_y
    @arg_validation_decos.is_apysc_num(arg_position_index=6)
    # width
    @arg_validation_decos.is_apysc_num(arg_position_index=7)
    # height
    @arg_validation_decos.is_apysc_num(arg_position_index=8)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        *,
        left_x: Number,
        center_x: Number,
        right_x: Number,
        top_y: Number,
        center_y: Number,
        bottom_y: Number,
        width: Int,
        height: Int,
    ):
        """
        The rectangle's geometry class.

        Parameters
        ----------
        left_x : Number
            The rectangle left-x coodinate.
        center_x : Number
            The rectangle center-x coodinate.
        right_x : Number
            The rectangle right-x coodinate.
        top_y : Number
            The rectangle top-y coodinate.
        center_y : Number
            The rectangle center-y coodinate.
        bottom_y : Number
            The rectangle bottom-y coodinate.
        width : Int
            The rectangle width.
        height : Int
            The Rectangle height.
        """
        self._left_x = left_x
        self._center_x = center_x

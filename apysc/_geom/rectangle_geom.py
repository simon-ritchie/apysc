"""The rectangle's geometry class implementation.
"""

from typing_extensions import final

from apysc._geom.rectangle_geom_bottom_y_mixin import RectangleGeomBottomYMixIn
from apysc._geom.rectangle_geom_center_x_mixin import RectangleGeomCenterXMixIn
from apysc._geom.rectangle_geom_center_y_mixin import RectangleGeomCenterYMixIn
from apysc._geom.rectangle_geom_height_mixin import RectangleGeomHeightMixIn
from apysc._geom.rectangle_geom_left_x_mixin import RectangleGeomLeftXMixIn
from apysc._geom.rectangle_geom_right_x_mixin import RectangleGeomRightXMixIn
from apysc._geom.rectangle_geom_top_y_mixin import RectangleGeomTopYMixIn
from apysc._geom.rectangle_geom_width_mixin import RectangleGeomWidthMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos


class RectangleGeom(
    VariableNameSuffixAttrOrVarMixIn,
    VariableNameMixIn,
    VariableNameSuffixMixIn,
    RectangleGeomLeftXMixIn,
    RectangleGeomCenterXMixIn,
    RectangleGeomRightXMixIn,
    RectangleGeomTopYMixIn,
    RectangleGeomCenterYMixIn,
    RectangleGeomBottomYMixIn,
    RectangleGeomWidthMixIn,
    RectangleGeomHeightMixIn,
):
    """
    The rectangle's geometry class.

    Attributes
    ----------
    left_x : Number
        The rectangle left x coordinate.
    center_x : Number
        The rectangle center x coordinate.
    right_x : Number
        The rectangle right x coordinate.
    top_y : Number
        The rectangle top y coordinate.
    center_y : Number
        The rectangle center y coordinate.
    bottom_y : Number
        The rectangle bottom y coordinate.
    width : Int
        The rectangle width.
    height : Int
        The Rectangle height.

    References
    ----------
    - RectangleGeom class
        - https://simon-ritchie.github.io/apysc/en/rectangle_geom.html
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
            The rectangle left x coordinate.
        center_x : Number
            The rectangle center x coordinate.
        right_x : Number
            The rectangle right x coordinate.
        top_y : Number
            The rectangle top y coordinate.
        center_y : Number
            The rectangle center y coordinate.
        bottom_y : Number
            The rectangle bottom y coordinate.
        width : Int
            The rectangle width.
        height : Int
            The Rectangle height.

        References
        ----------
        - RectangleGeom class
            - https://simon-ritchie.github.io/apysc/en/rectangle_geom.html
        """
        self._left_x = left_x
        self._center_x = center_x
        self._right_x = right_x
        self._top_y = top_y
        self._center_y = center_y
        self._bottom_y = bottom_y
        self._width = width
        self._height = height

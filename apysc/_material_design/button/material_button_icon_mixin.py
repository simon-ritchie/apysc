"""The mix-in class implementation for the material button's icon-related
methods.
"""


from typing import Optional, cast

from apysc._color.color import Color
from apysc._display.child_mixin import ChildMixIn
from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase
from apysc._display.x_mixin import XMixIn
from apysc._display.y_mixin import YMixIn
from apysc._geom.rectangle_geom import RectangleGeom
from apysc._type.variable_name_suffix_attr_or_var_mixin import VariableNameSuffixAttrOrVarMixIn
from apysc._validation import arg_validation_decos


class _InstanceStub(
    XMixIn,
    YMixIn,
    ChildMixIn,
    VariableNameSuffixAttrOrVarMixIn,
):
    pass


class MaterialButtonIconMixIn:
    """
    The mix-in class implementation for the material button's
    icon-related methods.
    """

    @arg_validation_decos.is_fixed_html_svg_icon(arg_position_index=1, optional=True)
    @arg_validation_decos.is_fixed_html_svg_icon(arg_position_index=2, optional=True)
    @arg_validation_decos.is_rectangle_geom(arg_position_index=3)
    def _locate_icons(
        self,
        *,
        prefix_icon: Optional[FixedHtmlSvgIconBase],
        suffix_icon: Optional[FixedHtmlSvgIconBase],
        background_bounding_box: RectangleGeom,
    ) -> None:
        """
        Locate each icon.

        Parameters
        ----------
        prefix_icon : Optional[FixedHtmlSvgIconBase]
            An icon to display on the left side of the label.
        suffix_icon : Optional[FixedHtmlSvgIconBase]
            An icon to display on the right side of the label.
        background_bounding_box : RectangleGeom
            A bounding box of the background.
        """
        from apysc._type.number import Number
        from apysc._material_design.button.material_button_const import ICON_OUTER_PADDING_WIDTH, ICON_SIZE, ICON_Y

        self_instance: _InstanceStub = cast(_InstanceStub, self)
        if prefix_icon is not None:
            suffix: str = self_instance._get_attr_or_variable_name_suffix(
                value_identifier="prefix_icon_x"
            )
            prefix_icon.x = Number(
                ICON_OUTER_PADDING_WIDTH, variable_name_suffix=suffix
            )

            suffix = self_instance._get_attr_or_variable_name_suffix(
                value_identifier="prefix_icon_y"
            )
            prefix_icon.y = Number(ICON_Y, variable_name_suffix=suffix)

        if suffix_icon is not None:
            suffix = self_instance._get_attr_or_variable_name_suffix(
                value_identifier="suffix_icon_x"
            )
            suffix_icon.x = Number(
                background_bounding_box.width
                - ICON_OUTER_PADDING_WIDTH
                - ICON_SIZE,
                variable_name_suffix=suffix,
            )

            suffix = self_instance._get_attr_or_variable_name_suffix(
                value_identifier="suffix_icon_y"
            )
            suffix_icon.y = Number(ICON_Y, variable_name_suffix=suffix)

    @arg_validation_decos.is_fixed_html_svg_icon(arg_position_index=1, optional=True)
    @arg_validation_decos.is_fixed_html_svg_icon(arg_position_index=2, optional=True)
    def _add_icons(
        self,
        *,
        prefix_icon: Optional[FixedHtmlSvgIconBase],
        suffix_icon: Optional[FixedHtmlSvgIconBase],
    ) -> None:
        """
        Add each icon to this button.

        Parameters
        ----------
        prefix_icon : Optional[FixedHtmlSvgIconBase]
            An icon to display on the left side of the label.
        suffix_icon : Optional[FixedHtmlSvgIconBase]
            An icon to display on the right side of the label.
        """
        self_instance: _InstanceStub = cast(_InstanceStub, self)
        if prefix_icon is not None:
            self_instance.add_child(child=prefix_icon)
        if suffix_icon is not None:
            self_instance.add_child(child=suffix_icon)

    @arg_validation_decos.is_fixed_html_svg_icon(arg_position_index=1, optional=True)
    @arg_validation_decos.is_fixed_html_svg_icon(arg_position_index=2, optional=True)
    def _resize_icon_size(
        self,
        *,
        prefix_icon: Optional[FixedHtmlSvgIconBase],
        suffix_icon: Optional[FixedHtmlSvgIconBase],
    ) -> None:
        """
        Resize the icon size if each icon is specified.

        Parameters
        ----------
        prefix_icon : Optional[FixedHtmlSvgIconBase]
            An icon to display on the left side of the label.
        suffix_icon : Optional[FixedHtmlSvgIconBase]
            An icon to display on the right side of the label.
        """
        from apysc._type.int import Int
        from apysc._material_design.button.material_button_const import ICON_SIZE

        if prefix_icon is not None:
            prefix_icon.width = Int(
                ICON_SIZE, variable_name_suffix="prefix_icon_width"
            )
            prefix_icon.height = Int(
                ICON_SIZE, variable_name_suffix="prefix_icon_height"
            )
        if suffix_icon is not None:
            suffix_icon.width = Int(
                ICON_SIZE, variable_name_suffix="suffix_icon_width"
            )
            suffix_icon.height = Int(
                ICON_SIZE, variable_name_suffix="suffix_icon_height"
            )

    @arg_validation_decos.is_fixed_html_svg_icon(arg_position_index=2, optional=True)
    @arg_validation_decos.is_fixed_html_svg_icon(arg_position_index=3, optional=True)
    def _set_fill_color_to_icons(
        self,
        *,
        color: Color,
        prefix_icon: Optional[FixedHtmlSvgIconBase],
        suffix_icon: Optional[FixedHtmlSvgIconBase],
    ) -> None:
        """
        Set a fill-color to the icons.

        Parameters
        ----------
        color : Color
            A color to set.
        prefix_icon : Optional[FixedHtmlSvgIconBase]
            An icon to display on the left side of the label.
        suffix_icon : Optional[FixedHtmlSvgIconBase]
            An icon to display on the right side of the label.
        """
        if prefix_icon is not None:
            prefix_icon.fill_color = color
        if suffix_icon is not None:
            suffix_icon.fill_color = color

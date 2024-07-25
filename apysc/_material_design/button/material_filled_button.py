"""The class implementation for the material design filled button.
"""

from typing import List
from typing import Optional
from typing import Union

from apysc._color.color import Color
from apysc._display.add_to_parent_mixin import AddToParentMixIn
from apysc._display.child_mixin import ChildMixIn
from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase
from apysc._display.sprite import Sprite
from apysc._geom.rectangle_geom import RectangleGeom
from apysc._material_design.button.material_button_const import BUTTON_HEIGHT
from apysc._material_design.button.material_button_const import ICON_SIZE
from apysc._material_design.button.material_button_const import NO_ICON_OUTER_PADDING
from apysc._material_design.button.material_button_icon_mixin import (
    MaterialButtonIconMixIn,
)
from apysc._material_design.button.material_button_label_mixin import (
    MaterialButtonLabelMixIn,
)
from apysc._material_design.geom.material_x_and_y_attributes_mixin import (
    MaterialXAndYAttributesMixIn,
)
from apysc._type.array import Array
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String
from apysc._validation import arg_validation_decos


class MaterialFilledButton(
    Sprite,
    MaterialButtonLabelMixIn,
    MaterialButtonIconMixIn,
    MaterialXAndYAttributesMixIn,
    AddToParentMixIn,
):
    """
    The class for the material design filled button.

    References
    ----------
    - Material design filled button document
        - https://m3.material.io/components/buttons/specs#0b1b7bd2-3de8-431a-afa1-d692e2e18b0d  # noqa
    """

    _background_color: Color

    # label
    @arg_validation_decos.is_string(arg_position_index=1, optional=False)
    # prefix_icon
    @arg_validation_decos.is_fixed_html_svg_icon(arg_position_index=2, optional=True)
    # suffix_icon
    @arg_validation_decos.is_fixed_html_svg_icon(arg_position_index=3, optional=True)
    # x
    @arg_validation_decos.is_num(arg_position_index=4, optional=False)
    # y
    @arg_validation_decos.is_num(arg_position_index=5, optional=False)
    # text_color
    @arg_validation_decos.is_color(arg_position_index=6, optional=True)
    # font_family
    @arg_validation_decos.is_builtin_str_list_or_apysc_str_arr(
        arg_position_index=7, optional=True
    )
    # font_size
    @arg_validation_decos.is_integer(arg_position_index=8, optional=False)
    # background_color
    @arg_validation_decos.is_color(arg_position_index=9, optional=True)
    # parent
    @arg_validation_decos.is_display_object_container(
        arg_position_index=10, optional=True
    )
    # variable_name_suffix
    @arg_validation_decos.is_builtin_string(arg_position_index=11, optional=False)
    def __init__(
        self,
        *,
        label: Union[str, String],
        prefix_icon: Optional[FixedHtmlSvgIconBase] = None,
        suffix_icon: Optional[FixedHtmlSvgIconBase] = None,
        x: Union[float, Number] = 0.0,
        y: Union[float, Number] = 0.0,
        text_color: Optional[Color] = None,
        font_family: Optional[Union[Array[String], List[str]]] = None,
        font_size: Union[int, Int] = 14,
        background_color: Optional[Color] = None,
        parent: Optional[ChildMixIn] = None,
        variable_name_suffix: str = "",
    ) -> None:
        """
        The class for the material design filled button.

        References
        ----------
        - Material design filled button document
            - https://m3.material.io/components/buttons/specs#0b1b7bd2-3de8-431a-afa1-d692e2e18b0d  # noqa

        Parameters
        ----------
        label : Union[str, String]
            The label text to display on this button.
        prefix_icon : Optional[FixedHtmlSvgIconBase], optional
            An icon to display on the left side of the label.
        suffix_icon : Optional[FixedHtmlSvgIconBase], optional
            An icon to display on the right side of the label.
        x : Union[float, Number], optional
            X-coordinate of this button.
        y : Union[float, Number], optional
            Y-coordinate of this button.
        text_color : Optional[Color], optional
            The color of the label text.
            The label color becomes according to the following priorities:
            1. If this argument is not omitted (i.e., it is not `None`)
            2. If a color scheme is set in the `MaterialSettings` (this button
                refers to the `primary` color)
            3. A fixed color value.
        font_family : Optional[Union[Array[String], List[str]]], optional
            A font-family setting.
        font_size : Union[int, Int], optional
            A font-size setting.
        background_color : Optional[Color], optional
            The background color of this button.
            The background color becomes according to the following priorities:
            1. If this argument is not omitted (i.e., it is not `None`)
            2. If a color scheme is set in the `MaterialSettings` (this button
                refers to the `on_primary` color)
            3. A fixed color value.
        parent : Optional[ChildMixIn], optional
            A parent instance to add this instance.
            If the specified value is None, this interface uses
            a stage instance.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        from apysc._material_design.setting.material_settings_utils import (
            MaterialSettingsUtils,
        )

        self._variable_name_suffix = variable_name_suffix
        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.MATERIAL_FILLED_BUTTON,
        )
        super(MaterialFilledButton, self).__init__(
            variable_name=variable_name, variable_name_suffix=variable_name_suffix
        )

        on_primary_color: Color = MaterialSettingsUtils.get_on_primary_color(
            argument_color=text_color
        )
        self._initialize_label(
            label=label,
            text_color=on_primary_color,
            font_family=font_family,
            font_size=font_size,
        )
        self._background_color = MaterialSettingsUtils.get_primary_color(
            argument_color=background_color
        )
        label_text_initial_bounding_box: RectangleGeom = self._label_text.get_bounds(
            target_coordinate_space_object=self
        )
        self._resize_icon_size(prefix_icon=prefix_icon, suffix_icon=suffix_icon)
        self._add_icons(prefix_icon=prefix_icon, suffix_icon=suffix_icon)
        self._redraw_background(
            label_text_bounding_box=label_text_initial_bounding_box,
            prefix_icon=prefix_icon,
            suffix_icon=suffix_icon,
        )
        background_initial_bounding_box: RectangleGeom = self.get_bounds()
        self._locate_icons(
            prefix_icon=prefix_icon,
            suffix_icon=suffix_icon,
            background_bounding_box=background_initial_bounding_box,
        )
        self._locate_label_text(
            label_text_bounding_box=label_text_initial_bounding_box,
            prefix_icon=prefix_icon,
        )
        self._set_fill_color_to_icons(
            color=on_primary_color, prefix_icon=prefix_icon, suffix_icon=suffix_icon
        )
        self._set_x_and_y_coordinates(x=x, y=y)
        self._add_to_parent(parent=parent)

    def _redraw_background(
        self,
        *,
        label_text_bounding_box: RectangleGeom,
        prefix_icon: Optional[FixedHtmlSvgIconBase],
        suffix_icon: Optional[FixedHtmlSvgIconBase],
    ) -> None:
        """
        Redraw the background of this button.

        Parameters
        ----------
        label_text_bounding_box : RectangleGeom
            The bounding box of the label text.
        prefix_icon : Optional[FixedHtmlSvgIconBase]
            An icon to display on the left side of the label.
        suffix_icon : Optional[FixedHtmlSvgIconBase]
            An icon to display on the right side of the label.
        """
        self.graphics.clear()
        self.graphics.begin_fill(color=self._background_color)
        additional_width: int = 0
        if prefix_icon is not None:
            additional_width += ICON_SIZE
        if suffix_icon is not None:
            additional_width += ICON_SIZE
        self.graphics.draw_round_rect(
            x=0,
            y=0,
            width=(
                label_text_bounding_box.width
                + NO_ICON_OUTER_PADDING * 2
                + additional_width
            ),
            height=BUTTON_HEIGHT,
            ellipse_width=int(BUTTON_HEIGHT / 2),
            ellipse_height=int(BUTTON_HEIGHT / 2),
        )

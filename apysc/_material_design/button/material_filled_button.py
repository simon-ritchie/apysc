"""The class implementation for the material design filled button.
"""

from typing import List, Optional, Union
from apysc._color.color import Color
from apysc._display.child_mixin import ChildMixIn
from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase
from apysc._display.sprite import Sprite
from apysc._type.array import Array
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String
from apysc._validation import arg_validation_decos
from apysc._material_design.button.material_button_label_mixin import (
    MaterialButtonLabelMixIn
)


class MaterialFilledButton(
    Sprite,
    MaterialButtonLabelMixIn,
):
    """
    The class for the material design filled button.

    References
    ----------
    - Material design filled button document
        - https://m3.material.io/components/buttons/specs#0b1b7bd2-3de8-431a-afa1-d692e2e18b0d  # noqa
    """

    _prefix_icon: Optional[FixedHtmlSvgIconBase]

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
            1. If this argument is not omitted (i.e, it is not `None`)
            2. If a color scheme is set in the `MaterialSettings` (this button
                refers the `primary` color)
            3. A fixed color value.
        font_family : Optional[Union[Array[String], List[str]]], optional
            A font-family setting.
        font_size : Union[int, Int], optional
            A font-size setting.
        background_color : Optional[Color], optional
            The background color of this button.
            The background color becomes according to the following priorities:
            1. If this argument is not omitted (i.e, it is not `None`)
            2. If a color scheme is set in the `MaterialSettings` (this button
                refers the `on_primary` color)
            3. A fixed color value.
        parent : Optional[ChildMixIn], optional
            A parent instance to add this instance.
            If the specified value is None, this interface uses
            a stage instance.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        self._variable_name_suffix = variable_name_suffix
        pass

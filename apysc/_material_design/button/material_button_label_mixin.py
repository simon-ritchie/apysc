"""The mix-in class implementation for the material design button's label.
"""

from typing import List
from typing import Optional
from typing import Union

from apysc._color.color import Color
from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase
from apysc._display.svg_text import SvgText
from apysc._geom.rectangle_geom import RectangleGeom
from apysc._type.array import Array
from apysc._type.int import Int
from apysc._type.string import String


class MaterialButtonLabelMixIn:
    _label: String
    _label_text: SvgText
    _text_color: Color
    _font_family: Array[String]
    _font_size: Int

    def _initialize_label(
        self,
        *,
        label: Union[str, String],
        text_color: Color,
        font_family: Optional[Union[Array[String], List[str]]],
        font_size: Union[int, Int],
    ) -> None:
        """
        Initialize the label setting with the specified argument.

        Parameters
        ----------
        label : Union[str, String]
            A label text to display on this button.
        text_color : Color
            The color of the label text.
        font_family : Optional[Union[Array[String], List[str]]]
            A font-family setting.
        font_size : Union[int, Int]
            A font-size setting.
        """
        from apysc._converter.list_of_strs_to_array import (
            list_of_strs_to_array_of_string,
        )
        from apysc._converter.to_apysc_val_from_builtin import (
            get_copied_int_from_builtin_val,
        )
        from apysc._converter.to_apysc_val_from_builtin import (
            get_copied_string_from_builtin_val,
        )
        from apysc._display.child_mixin import ChildMixIn
        from apysc._material_design.setting.material_settings_utils import (
            MaterialSettingsUtils,
        )
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )
        from apysc._validation.display_validation import (
            validate_display_object_container,
        )

        self._label = get_copied_string_from_builtin_val(
            string=label,
            variable_name_suffix=get_attr_or_variable_name_suffix(
                instance=self, value_identifier="material_button_label"
            ),
        )
        self._text_color = text_color
        self._font_family = MaterialSettingsUtils.get_font_family(
            argument_font_family=list_of_strs_to_array_of_string(
                optional_list_or_arr=font_family,
                variable_name_suffix=get_attr_or_variable_name_suffix(
                    instance=self, value_identifier="material_button_label_font_family"
                ),
            )
        )
        self._font_size = get_copied_int_from_builtin_val(
            integer=font_size,
            variable_name_suffix=get_attr_or_variable_name_suffix(
                instance=self, value_identifier="material_button_label_font_size"
            ),
        )

        parent: ChildMixIn = validate_display_object_container(container_object=self)
        self._label_text = SvgText(
            text=self._label,
            font_size=self._font_size,
            font_family=self._font_family,
            fill_color=self._text_color,
            variable_name_suffix=get_attr_or_variable_name_suffix(
                instance=self, value_identifier="material_button_label_text"
            ),
            parent=parent,
        )

    def _locate_label_text(
        self,
        *,
        label_text_bounding_box: RectangleGeom,
        prefix_icon: Optional[FixedHtmlSvgIconBase],
    ) -> None:
        """
        Locate the label text.

        Parameters
        ----------
        label_text_bounding_box : RectangleGeom
            The bounding box of the label text.
        prefix_icon : Optional[FixedHtmlSvgIconBase]
            An icon to display on the left side of the label.
        """
        from apysc._material_design.button.material_button_const import BUTTON_HEIGHT
        from apysc._material_design.button.material_button_const import (
            ICON_INNER_PADDING_WIDTH,
        )
        from apysc._material_design.button.material_button_const import (
            ICON_OUTER_PADDING_WIDTH,
        )
        from apysc._material_design.button.material_button_const import ICON_SIZE
        from apysc._material_design.button.material_button_const import (
            NO_ICON_OUTER_PADDING,
        )
        from apysc._type.number import Number
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        suffix: str = get_attr_or_variable_name_suffix(
            instance=self,
            value_identifier="label_text_x",
        )
        if prefix_icon is None:
            self._label_text.x = Number(
                NO_ICON_OUTER_PADDING,
                variable_name_suffix=suffix,
            )
        else:
            self._label_text.x = Number(
                ICON_OUTER_PADDING_WIDTH + ICON_SIZE + ICON_INNER_PADDING_WIDTH,
                variable_name_suffix=suffix,
            )

        half_button_height: float = BUTTON_HEIGHT / 2
        suffix = get_attr_or_variable_name_suffix(
            instance=self,
            value_identifier="label_text_y",
        )
        self._label_text.y = (
            Number(
                half_button_height,
                variable_name_suffix=suffix,
            )
            - label_text_bounding_box.height / 2
        )

"""Class implementation for a SVG text.
"""

from typing import List
from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._display.child_mixin import ChildMixIn
from apysc._display.fill_alpha_mixin import FillAlphaMixIn
from apysc._display.fill_color_mixin import FillColorMixIn
from apysc._display.flip_x_mixin import FlipXMixIn
from apysc._display.flip_y_mixin import FlipYMixIn
from apysc._display.graphics_base import GraphicsBase
from apysc._display.line_alpha_mixin import LineAlphaMixIn
from apysc._display.line_color_mixin import LineColorMixIn
from apysc._display.line_thickness_mixin import LineThicknessMixIn
from apysc._display.rotation_around_center_mixin import RotationAroundCenterMixIn
from apysc._display.rotation_around_point_mixin import RotationAroundPointMixIn
from apysc._display.scale_x_from_center_mixin import ScaleXFromCenterMixIn
from apysc._display.scale_x_from_point_mixin import ScaleXFromPointMixIn
from apysc._display.scale_y_from_center_mixin import ScaleYFromCenterMixIn
from apysc._display.scale_y_from_point_mixin import ScaleYFromPointMixIn
from apysc._display.svg_text_font_family_mixin import SVGTextFontFamilyMixIn
from apysc._display.svg_text_font_size_mixin import SVGTextFontSizeMixIn
from apysc._display.svg_text_leading_mixin import SVGTextLeadingMixIn
from apysc._display.svg_text_text_mixin import SVGTextTextMixIn
from apysc._display.svg_text_align_mixin import SVGTextAlignMixIn, SVGTextAlign
from apysc._display.x_mixin import XMixIn
from apysc._display.y_mixin import YMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.array import Array
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String
from apysc._validation import arg_validation_decos


class SVGText(
    XMixIn,
    YMixIn,
    GraphicsBase,
    RotationAroundCenterMixIn,
    RotationAroundPointMixIn,
    ScaleXFromCenterMixIn,
    ScaleYFromCenterMixIn,
    ScaleXFromPointMixIn,
    ScaleYFromPointMixIn,
    FlipXMixIn,
    FlipYMixIn,
    FillColorMixIn,
    FillAlphaMixIn,
    LineColorMixIn,
    LineAlphaMixIn,
    LineThicknessMixIn,
    SVGTextTextMixIn,
    SVGTextFontFamilyMixIn,
    SVGTextFontSizeMixIn,
    SVGTextLeadingMixIn,
    SVGTextAlignMixIn,
):

    # text
    @arg_validation_decos.is_string(arg_position_index=1)
    # font_size
    @arg_validation_decos.is_integer(arg_position_index=2)
    # font_family
    @arg_validation_decos.is_builtin_str_list_or_apysc_str_arr(
        arg_position_index=3, optional=True
    )
    # x
    @arg_validation_decos.is_num(arg_position_index=4)
    # y
    @arg_validation_decos.is_num(arg_position_index=5)
    # fill_color
    @arg_validation_decos.is_hex_color_code_format(arg_position_index=6)
    # fill_alpha
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=7)
    # line_color
    @arg_validation_decos.is_hex_color_code_format(arg_position_index=8)
    # line_alpha
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=9)
    # line_thickness
    @arg_validation_decos.is_integer(arg_position_index=10)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=10)
    # leading
    @arg_validation_decos.is_num(arg_position_index=11)
    # align
    @arg_validation_decos.is_svg_text_align(arg_position_index=12)
    # parent
    @arg_validation_decos.is_display_object_container(
        arg_position_index=13, optional=True
    )
    # variable_name_suffix
    @arg_validation_decos.is_builtin_string(arg_position_index=14, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        *,
        text: Union[str, String],
        font_size: Union[int, Int] = 16,
        font_family: Optional[Union[Array[String], List[str]]] = None,
        x: Union[float, Number] = 0.0,
        y: Union[float, Number] = 0.0,
        fill_color: Union[str, String] = "#666",
        fill_alpha: Union[float, Number] = 1.0,
        line_color: Union[str, String] = "",
        line_alpha: Union[float, Number] = 1.0,
        line_thickness: Union[int, Int] = 1,
        leading: Union[float, Number] = 1.5,
        align: SVGTextAlign = SVGTextAlign.LEFT,
        parent: Optional[ChildMixIn] = None,
        variable_name_suffix: str = "",
    ) -> None:
        """
        The class for a SVG text.

        Parameters
        ----------
        text : Union[str, String]
            A text to use in this class.
        font_size : Union[int, Int], optional
            A font-size setting.
        font_family : Optional[Union[Array[String], List[str]]], optional
            A font-family setting.
            Each string in an array needs to be a font name (e.g., `Times New Roman`).
        x : float or Number, default 0.0
            X-coordinate to start drawing.
        y : float or Number, default 0.0
            Y-coordinate to start drawing.
        fill_color : str or String, default '#666'
            A fill-color to set.
        fill_alpha : float or Number, default 1.0
            A fill-alpha to set.
        line_color : str or String, default ''
            A line-color to set.
        line_alpha : float or Number, default 1.0
            A line-alpha to set.
        line_thickness : int or Int, default 1
            A line-thickness (line-width) to set.
        leading : float or Number, default 1.5
            A text-leading size.
        align : SVGTextAlign, default SVGTextAlign.LEFT
            A text-align setting.
        parent : ChildMixIn or None, default None
            A parent instance to add this instance.
            If a specified value is None, this interface uses
            a stage instance.
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.SVG_TEXT,
        )
        self.variable_name = variable_name
        self._variable_name_suffix = variable_name_suffix
        self._update_x_and_skip_appending_exp(x=x)
        self._update_y_and_skip_appending_exp(y=y)
        self._set_initial_basic_values(
            fill_color=fill_color,
            fill_alpha=fill_alpha,
            line_color=line_color,
            line_thickness=line_thickness,
            line_alpha=line_alpha,
            line_cap=None,
            line_joints=None,
        )
        self._append_constructor_expression()
        self._set_text_value(text=text)
        self._set_font_size_value(font_size=font_size)
        self._set_font_family(font_family=font_family)
        self._set_leading(leading=leading)
        self._set_align(align=align)

        # Since the SVG-text constructor's y-coordinate is different from
        # the y-attribute updating, this class sets the y-coordinate attribute
        # value after the constructor.
        self.y = self.y

        super(SVGText, self).__init__(
            parent=parent,
            variable_name=variable_name,
        )

    @final
    def _append_constructor_expression(self) -> None:
        """
        Append a constructor expression string.
        """
        import apysc as ap

        variable_name: str = self.variable_name
        stage: ap.Stage = ap.get_stage()
        expression: str = (
            f"var {variable_name} = {stage.variable_name}" "\n  .text()" "\n  .attr({"
        )
        expression = self._append_basic_vals_expression(
            expression=expression, indent_num=2
        )
        expression += "\n  });"
        ap.append_js_expression(expression=expression)

    def _set_align(self, *, align: SVGTextAlign) -> None:
        """
        Set a text-align setting.

        Parameters
        ----------
        align : SVGTextAlign
            A text-align setting.
        """
        self.align = align

    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_leading(self, *, leading: Union[float, Number]) -> None:
        """
        Set a leading value.

        Parameters
        ----------
        leading : Union[float, Number]
            A text-leading value.
        """
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        if isinstance(leading, float):
            suffix: str = get_attr_or_variable_name_suffix(
                instance=self, value_identifier="leading"
            )
            leading_: Number = Number(leading, variable_name_suffix=suffix)
        else:
            leading_ = leading
        self.leading = leading_

    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_font_size_value(self, *, font_size: Union[int, Int]) -> None:
        """
        Set a font-size value.

        Parameters
        ----------
        font_size : Union[int, Int]
            A target font-size value.
        """
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        if isinstance(font_size, int):
            suffix: str = get_attr_or_variable_name_suffix(
                instance=self, value_identifier="font_size"
            )
            font_size_: Int = Int(font_size, variable_name_suffix=suffix)
        else:
            font_size_ = font_size
        self.font_size = font_size_

    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_text_value(self, *, text: Union[str, String]) -> None:
        """
        Set a text value.

        Parameters
        ----------
        text : Union[str, String]
            A target text.

        Returns
        -------
        text_ : String
            A set text.
        """
        from apysc._string import string_util

        if isinstance(text, str):
            text = string_util.escape_str(string=text)
            text_: String = String(
                text,
                variable_name_suffix=self._variable_name_suffix,
            )
        else:
            text_ = text
        self.text = text_

    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_font_family(
        self,
        *,
        font_family: Optional[Union[Array[String], List[str]]],
    ) -> None:
        """
        Set a font-family value.

        Parameters
        ----------
        font_family : Optional[Array[String]]
            A font-family setting.
        """
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        if font_family is None:
            return
        if isinstance(font_family, list):
            suffix: str = get_attr_or_variable_name_suffix(
                instance=self,
                value_identifier="font_family",
            )
            font_family_: Array[String] = Array(
                [String(font_name) for font_name in font_family],
                variable_name_suffix=suffix,
            )
        else:
            font_family_ = font_family
        self.font_family = font_family_

    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of
        debugging).

        Returns
        -------
        repr_str : str
            This interface returns a type name and variable name
            (e.g., `SVGText("<variable_name>")`).
        """
        repr_str: str = f'{SVGText.__name__}("{self._variable_name}")'
        return repr_str

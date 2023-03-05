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
from apysc._display.svg_text_align_mixin import SVGTextAlign
from apysc._display.svg_text_align_mixin import SVGTextAlignMixIn
from apysc._display.svg_text_bold_mixin import SVGTextBoldMixIn
from apysc._display.svg_text_font_family_mixin import SVGTextFontFamilyMixIn
from apysc._display.svg_text_font_size_mixin import SVGTextFontSizeMixIn
from apysc._display.svg_text_italic_mixin import SVGTextItalicMixIn
from apysc._display.svg_text_leading_mixin import SVGTextLeadingMixIn
from apysc._display.svg_text_text_mixin import SVGTextTextMixIn
from apysc._display.svg_text_set_text_value_mixin import SVGTextSetTextValueMixIn
from apysc._display.svg_text_set_font_size_value_mixin import (
    SVGTextSetFontSizeValueMixIn
)
from apysc._display.svg_text_set_font_family_mixin import SVGTextSetFontFamilyMixIn
from apysc._display.svg_text_set_leading_mixin import SVGTextSetLeadingMixIn
from apysc._display.svg_text_set_align_mixin import SVGTextSetAlignMixIn
from apysc._display.svg_text_set_bold_mixin import SVGTextSetBoldMixIn
from apysc._display.svg_text_set_italic_mixin import SVGTextSetItalicMixIn
from apysc._display.x_mixin import XMixIn
from apysc._display.y_mixin import YMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.array import Array
from apysc._type.boolean import Boolean
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String
from apysc._validation import arg_validation_decos
from apysc._display.svg_text_span import SVGTextSpan


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
    SVGTextSetTextValueMixIn,
    SVGTextFontFamilyMixIn,
    SVGTextSetFontFamilyMixIn,
    SVGTextFontSizeMixIn,
    SVGTextSetFontSizeValueMixIn,
    SVGTextLeadingMixIn,
    SVGTextSetLeadingMixIn,
    SVGTextAlignMixIn,
    SVGTextSetAlignMixIn,
    SVGTextItalicMixIn,
    SVGTextSetItalicMixIn,
    SVGTextBoldMixIn,
    SVGTextSetBoldMixIn,
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
    # bold
    @arg_validation_decos.is_boolean(arg_position_index=13)
    # italic
    @arg_validation_decos.is_boolean(arg_position_index=14)
    # parent
    @arg_validation_decos.is_display_object_container(
        arg_position_index=15, optional=True
    )
    # variable_name_suffix
    @arg_validation_decos.is_builtin_string(arg_position_index=16, optional=False)
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
        bold: Union[bool, Boolean] = False,
        italic: Union[bool, Boolean] = False,
        parent: Optional[ChildMixIn] = None,
        variable_name_suffix: str = "",
        skip_init_constructor_and_text_settings: bool = False,
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
        bold : Union[bool, Boolean], default False
            A boolean, whether this text is bold style or not.
        italic : Union[bool, Boolean], default False
            A boolean, whether a text is an italic style or not (normal).
        parent : ChildMixIn or None, default None
            A parent instance to add this instance.
            If a specified value is None, this interface uses
            a stage instance.
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        skip_init_constructor_and_text_settings : bool, default False
            A boolean, whether to skip a constuctor's expression and
            text settings. The `SVGText` class uses this option internally.
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

        super(SVGText, self).__init__(
            variable_name=variable_name,
        )

        if not skip_init_constructor_and_text_settings:
            self._append_constructor_expression()
            self._set_text_value(text=text)
            self._set_font_size_value(font_size=font_size)
            self._set_font_family(font_family=font_family)
            self._set_leading(leading=leading)
            self._set_align(align=align)
            self._set_bold(bold=bold)
            self._set_italic(italic=italic)
            self._add_to_parent(parent=parent)
            self._set_overflow_visible_setting()

        # Since the SVG-text constructor's y-coordinate is different from
        # the y-attribute updating, this class sets the y-coordinate attribute
        # value after the constructor.
        self.y = self.y

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_constructor_expression(self) -> None:
        """
        Append a constructor expression string.
        """
        import apysc as ap

        variable_name: str = self.variable_name
        stage: ap.Stage = ap.get_stage()
        expression: str = (
            f"var {variable_name} = {stage.variable_name}" "\n  .text()\n  .attr({"
        )
        expression = self._append_basic_vals_expression(
            expression=expression, indent_num=2
        )
        expression += "\n  });"
        ap.append_js_expression(expression=expression)

    @classmethod
    # text_spans
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
    # bold
    @arg_validation_decos.is_boolean(arg_position_index=13)
    # italic
    @arg_validation_decos.is_boolean(arg_position_index=14)
    # parent
    @arg_validation_decos.is_display_object_container(
        arg_position_index=15, optional=True
    )
    # variable_name_suffix
    @arg_validation_decos.is_builtin_string(arg_position_index=16, optional=False)
    def create_with_svg_text_spans(
        cls,
        *,
        text_spans: Union[List[SVGTextSpan], Array[SVGTextSpan]],
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
        bold: Union[bool, Boolean] = False,
        italic: Union[bool, Boolean] = False,
        parent: Optional[ChildMixIn] = None,
        variable_name_suffix: str = "",
    ) -> "SVGText":
        """
        Create a `SVGText` instance with specified text spans.

        Parameters
        ----------
        text_spans : Union[List[SVGTextSpan], Array[SVGTextSpan]]
            Text spans.
        font_size : Union[int, Int], optional
            A font-size setting for an overall text.
        font_family : Optional[Union[Array[String], List[str]]], optional
            A font-family setting for an overall text.
            Each string in an array needs to be a font name (e.g., `Times New Roman`).
        x : Union[float, Number], optional
            X-coordinate to start drawing.
        y : Union[float, Number], optional
            Y-coordinate to start drawing.
        fill_color : Union[str, String], optional
            A fill-color setting for an overall text.
        fill_alpha : Union[float, Number], optional
            A fill-alpha setting for an overall text.
        line_color : Union[str, String], optional
            A line-color setting for an overall text.
        line_alpha : Union[float, Number], optional
            A line-alpha setting for an overall text.
        line_thickness : Union[int, Int], optional
            A line-thickness setting for an overall text.
        leading : Union[float, Number], optional
            A text-leading size setting for an overall text.
        align : SVGTextAlign, optional
            A text-align setting for an overall text.
        bold : Union[bool, Boolean], optional
            A boolean for an overall text, whether this text is bold style or not.
        italic : Union[bool, Boolean], optional
            A boolean for an overall text, whether a text is an italic
            style or not (normal).
        parent : Optional[ChildMixIn], optional
            A parent instance to add this instance.
            If a specified value is None, this interface uses
            a stage instance.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        svg_text : SVGText
            A created `SVGText` instance.
        """
        svg_text: SVGText = SVGText(
            text='',
            font_size=font_size,
            font_family=font_family,
            x=x,
            y=y,
            fill_color=fill_color,
            fill_alpha=fill_alpha,
            line_color=line_color,
            line_alpha=line_alpha,
            line_thickness=line_thickness,
            leading=leading,
            align=align,
            bold=bold,
            italic=italic,
            parent=parent,
            variable_name_suffix=variable_name_suffix,
        )
        text_spans_: Array[SVGTextSpan] = svg_text._convert_text_spans_list_to_array(
            text_spans=text_spans
        )
        svg_text._append_constructor_expression_with_text_spans()
        pass

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_constructor_expression_with_text_spans(self) -> None:
        """
        Append a constructor expression string with text spans.
        """
        pass

    @final
    @add_debug_info_setting(module_name=__name__)
    def _convert_text_spans_list_to_array(
        self,
        *,
        text_spans: Union[List[SVGTextSpan], Array[SVGTextSpan]],
    ) -> Array[SVGTextSpan]:
        """
        Convert text spans' list to an array.

        Parameters
        ----------
        text_spans : Union[List[SVGTextSpan], Array[SVGTextSpan]]
            Text spans.

        Returns
        -------
        text_spans_ : Array[SVGTextSpan]
            A converted array.
        """
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )
        if isinstance(text_spans, Array):
            return text_spans
        suffix: str = get_attr_or_variable_name_suffix(
            instance=self,
            value_identifier="text_spans",
        )
        text_spans_: Array[SVGTextSpan] = Array(text_spans, variable_name_suffix=suffix)
        return text_spans_

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

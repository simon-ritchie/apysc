"""Class implementation for an SVG text-span.
"""

from typing import List
from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._display.append_fill_alpha_attr_expression_mixin import (
    AppendFillAlphaAttrExpressionMixIn,
)
from apysc._display.append_fill_color_expression_mixin import (
    AppendFillColorAttrExpressionMixIn,
)
from apysc._display.append_line_alpha_attr_expression_mixin import (
    AppendLineAlphaAttrExpressionMixIn,
)
from apysc._display.append_line_color_attr_expression_mixin import (
    AppendLineColorAttrExpressionMixIn,
)
from apysc._display.append_line_thickness_attr_expression_mixin import (
    AppendLineThicknessAttrExpressionMixIn,
)
from apysc._display.fill_alpha_mixin import FillAlphaMixIn
from apysc._display.fill_color_mixin import FillColorMixIn
from apysc._display.graphics_base import GraphicsBase
from apysc._display.line_alpha_mixin import LineAlphaMixIn
from apysc._display.line_color_mixin import LineColorMixIn
from apysc._display.line_thickness_mixin import LineThicknessMixIn
from apysc._display.svg_text_bold_mixin import SVGTextBoldMixIn
from apysc._display.svg_text_font_family_mixin import SVGTextFontFamilyMixIn
from apysc._display.svg_text_font_size_mixin import SVGTextFontSizeMixIn
from apysc._display.svg_text_italic_mixin import SVGTextItalicMixIn
from apysc._display.svg_text_set_bold_mixin import SVGTextSetBoldMixIn
from apysc._display.svg_text_set_font_family_mixin import SVGTextSetFontFamilyMixIn
from apysc._display.svg_text_set_font_size_value_mixin import (
    SVGTextSetFontSizeValueMixIn,
)
from apysc._display.svg_text_set_italic_mixin import SVGTextSetItalicMixIn
from apysc._display.svg_text_set_text_value_mixin import SVGTextSetTextValueMixIn
from apysc._display.svg_text_text_mixin import SVGTextTextMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.array import Array
from apysc._type.boolean import Boolean
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String
from apysc._validation import arg_validation_decos


class SVGTextSpan(
    GraphicsBase,
    FillColorMixIn,
    AppendFillColorAttrExpressionMixIn,
    FillAlphaMixIn,
    AppendFillAlphaAttrExpressionMixIn,
    LineColorMixIn,
    AppendLineColorAttrExpressionMixIn,
    LineAlphaMixIn,
    AppendLineAlphaAttrExpressionMixIn,
    AppendLineThicknessAttrExpressionMixIn,
    LineThicknessMixIn,
    SVGTextTextMixIn,
    SVGTextSetTextValueMixIn,
    SVGTextFontFamilyMixIn,
    SVGTextSetFontFamilyMixIn,
    SVGTextFontSizeMixIn,
    SVGTextSetFontSizeValueMixIn,
    SVGTextItalicMixIn,
    SVGTextSetItalicMixIn,
    SVGTextBoldMixIn,
    SVGTextSetBoldMixIn,
):

    # text
    @arg_validation_decos.is_string(arg_position_index=1)
    # font_size
    @arg_validation_decos.is_integer(arg_position_index=2, optional=True)
    # font_family
    @arg_validation_decos.is_builtin_str_list_or_apysc_str_arr(
        arg_position_index=3, optional=True
    )
    # fill_color
    @arg_validation_decos.is_hex_color_code_format(arg_position_index=4)
    # fill_alpha
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=5)
    # line_color
    @arg_validation_decos.is_hex_color_code_format(arg_position_index=6)
    # line_alpha
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=7)
    # line_thickness
    @arg_validation_decos.is_integer(arg_position_index=8, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=8)
    # bold
    @arg_validation_decos.is_boolean(arg_position_index=9)
    # italic
    @arg_validation_decos.is_boolean(arg_position_index=10)
    # variable_name_suffix
    @arg_validation_decos.is_builtin_string(arg_position_index=11, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        *,
        text: Union[str, String],
        font_size: Optional[Union[int, Int]] = None,
        font_family: Optional[Union[Array[String], List[str]]] = None,
        fill_color: Union[str, String] = "",
        fill_alpha: Union[float, Number] = 1.0,
        line_color: Union[str, String] = "",
        line_alpha: Union[float, Number] = 1.0,
        line_thickness: Union[int, Int] = 1,
        bold: Union[bool, Boolean] = False,
        italic: Union[bool, Boolean] = False,
        variable_name_suffix: str = "",
    ) -> None:
        """
        The class for an SVG text-span (the child class of `SVGText`).

        Parameters
        ----------
        text : Union[str, String]
            A text to use in this class.
        font_size : Optional[Union[int, Int]], optional
            A font-size setting.
        font_family : Optional[Union[Array[String], List[str]]], optional
            A font-family setting.
            Each string in an array needs to be a font name (e.g., `Times New Roman`).
        fill_color : Union[str, String], optional
            A fill-color to set.
        fill_alpha : Union[float, Number], optional
            A fill-alpha to set.
        line_color : Union[str, String], optional
            A line-color to set.
        line_alpha : Union[float, Number], optional
            A line-alpha to set.
        line_thickness : Union[int, Int], optional
            A line-thickness (line-width) to set.
        bold : Union[bool, Boolean], optional
            A boolean, whether this text is bold style or not.
        italic : Union[bool, Boolean], optional
            A boolean, whether a text is an italic style or not (normal).
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.SVG_TEXT_SPAN,
        )
        self.variable_name = variable_name
        self._variable_name_suffix = variable_name_suffix
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
        self._set_bold(bold=bold)
        self._set_italic(italic=italic)

        super(SVGTextSpan, self).__init__(variable_name=variable_name)
        self._set_overflow_visible_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_constructor_expression(self) -> None:
        """
        Append a constructor expression string.
        """
        import apysc as ap
        from apysc._display.svg_text_singleton_for_text_span import (
            SVGTextSingletonForTextSpan,
        )

        INDENT_NUM: int = 2
        parent: ap.SVGText = SVGTextSingletonForTextSpan.get_instance()
        variable_name: str = self.variable_name
        expression: str = (
            f"var {variable_name} = {parent.variable_name}" "\n  .tspan()\n  .attr({"
        )
        expression = self._append_fill_color_attr_expression(
            expression=expression, indent_num=INDENT_NUM
        )
        expression = self._append_fill_alpha_attr_expression(
            expression=expression, indent_num=INDENT_NUM
        )
        expression = self._append_line_color_attr_expression(
            expression=expression, indent_num=INDENT_NUM
        )
        expression = self._append_line_thickness_attr_expression(
            expression=expression, indent_num=INDENT_NUM
        )
        expression = self._append_line_alpha_attr_expression(
            expression=expression, indent_num=INDENT_NUM
        )
        expression += "\n});"
        ap.append_js_expression(expression=expression)

    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of
        debugging).

        Returns
        -------
        repr_str : str
            This interface returns a type name and variable name
            (e.g., `SVGTextSpan("<variable_name>")`).
        """
        repr_str: str = f'{SVGTextSpan.__name__}("{self.variable_name}")'
        return repr_str

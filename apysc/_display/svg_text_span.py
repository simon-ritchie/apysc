"""Class implementation for a SVG text-span.
"""

from typing import List
from typing import Optional
from typing import Union, TYPE_CHECKING

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos
from apysc._display.graphics_base import GraphicsBase
from apysc._type.string import String
from apysc._type.int import Int
from apysc._type.array import Array
from apysc._type.number import Number
from apysc._type.boolean import Boolean
from apysc._display.x_mixin import XMixIn
from apysc._display.y_mixin import YMixIn
from apysc._display.fill_alpha_mixin import FillAlphaMixIn
from apysc._display.fill_color_mixin import FillColorMixIn
from apysc._display.line_alpha_mixin import LineAlphaMixIn
from apysc._display.line_color_mixin import LineColorMixIn
from apysc._display.line_thickness_mixin import LineThicknessMixIn
from apysc._display.svg_text_text_mixin import SVGTextTextMixIn
from apysc._display.svg_text_bold_mixin import SVGTextBoldMixIn
from apysc._display.svg_text_font_family_mixin import SVGTextFontFamilyMixIn
from apysc._display.svg_text_font_size_mixin import SVGTextFontSizeMixIn
from apysc._display.svg_text_italic_mixin import SVGTextItalicMixIn

if TYPE_CHECKING:
    from apysc._display.svg_text import SVGText


class SVGTextSpan(
    XMixIn,
    YMixIn,
    GraphicsBase,
    FillColorMixIn,
    FillAlphaMixIn,
    LineColorMixIn,
    LineAlphaMixIn,
    LineThicknessMixIn,
    SVGTextTextMixIn,
    SVGTextFontFamilyMixIn,
    SVGTextFontSizeMixIn,
    SVGTextItalicMixIn,
    SVGTextBoldMixIn,
):

    # text
    @arg_validation_decos.is_string(arg_position_index=1)
    # font_size
    @arg_validation_decos.is_integer(arg_position_index=2)
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
    @arg_validation_decos.is_integer(arg_position_index=8)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=8)
    # bold
    @arg_validation_decos.is_boolean(arg_position_index=9)
    # italic
    @arg_validation_decos.is_boolean(arg_position_index=10)
    # variable_name_suffix
    @arg_validation_decos.is_builtin_string(arg_position_index=11, optional=False)
    def __init__(
        self,
        *,
        text: Union[str, String],
        font_size: Union[int, Int] = 16,
        font_family: Optional[Union[Array[String], List[str]]] = None,
        fill_color: Union[str, String] = "#666",
        fill_alpha: Union[float, Number] = 1.0,
        line_color: Union[str, String] = "",
        line_alpha: Union[float, Number] = 1.0,
        line_thickness: Union[int, Int] = 1,
        bold: Union[bool, Boolean] = False,
        italic: Union[bool, Boolean] = False,
        variable_name_suffix: str = "",
    ) -> None:
        """
        The class for a SVG text-span (the child class of `SVGText`).

        Parameters
        ----------
        text : Union[str, String]
            A text to use in this class.
        font_size : Union[int, Int], optional
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
            A boolean whether this text is bold style or not.
        italic : Union[bool, Boolean], optional
            A boolean indicating whether a text is italic style or not (normal).
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        pass

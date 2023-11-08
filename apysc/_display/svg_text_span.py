"""Class implementation for an SVG text-span.
"""

from typing import List
from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._color.color import Color
from apysc._color.colorless import COLORLESS
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
from apysc._display.css_mixin import CssMixIn
from apysc._display.fill_alpha_mixin import FillAlphaMixIn
from apysc._display.fill_color_mixin import FillColorMixIn
from apysc._display.get_bounds_mixin import GetBoundsMixIn
from apysc._display.graphics_base import GraphicsBase
from apysc._display.line_alpha_mixin import LineAlphaMixIn
from apysc._display.line_color_mixin import LineColorMixIn
from apysc._display.line_thickness_mixin import LineThicknessMixIn
from apysc._display.set_overflow_visible_setting_mixin import (
    SetOverflowVisibleSettingMixIn,
)
from apysc._display.svg_text_bold_mixin import SvgTextBoldMixIn
from apysc._display.svg_text_delta_x_mixin import SvgTextDeltaXMixIn
from apysc._display.svg_text_delta_y_mixin import SvgTextDeltaYMixIn
from apysc._display.svg_text_font_family_mixin import SvgTextFontFamilyMixIn
from apysc._display.svg_text_font_size_mixin import SvgTextFontSizeMixIn
from apysc._display.svg_text_italic_mixin import SvgTextItalicMixIn
from apysc._display.svg_text_set_bold_mixin import SvgTextSetBoldMixIn
from apysc._display.svg_text_set_delta_x_mixin import SvgTextSetDeltaXMixIn
from apysc._display.svg_text_set_delta_y_mixin import SvgTextSetDeltaYMixIn
from apysc._display.svg_text_set_font_family_mixin import SvgTextSetFontFamilyMixIn
from apysc._display.svg_text_set_font_size_value_mixin import (
    SvgTextSetFontSizeValueMixIn,
)
from apysc._display.svg_text_set_italic_mixin import SvgTextSetItalicMixIn
from apysc._display.svg_text_set_text_value_mixin import SvgTextSetTextValueMixIn
from apysc._display.svg_text_skip_fill_alpha_exp_appending_mixin import (
    SvgTextSkipFillAlphaExpAppendingMixIn,
)
from apysc._display.svg_text_skip_fill_color_exp_appending_mixin import (
    SvgTextSkipFillColorExpAppendingMixIn,
)
from apysc._display.svg_text_skip_line_alpha_exp_appending_mixin import (
    SvgTextSkipLineAlphaExpAppendingMixIn,
)
from apysc._display.svg_text_skip_line_color_exp_appending_mixin import (
    SvgTextSkipLineColorExpAppendingMixIn,
)
from apysc._display.svg_text_skip_line_thickness_exp_appending_mixin import (
    SvgTextSkipLineThicknessExpAppendingMixIn,
)
from apysc._display.svg_text_text_mixin import SvgTextTextMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._loop.initialize_with_base_value_interface import (
    InitializeWithBaseValueInterface,
)
from apysc._type.array import Array
from apysc._type.boolean import Boolean
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.repr_interface import ReprInterface
from apysc._type.string import String
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos


class SvgTextSpan(
    ReprInterface,
    SetOverflowVisibleSettingMixIn,
    CssMixIn,
    GraphicsBase,
    FillColorMixIn,
    AppendFillColorAttrExpressionMixIn,
    SvgTextSkipFillColorExpAppendingMixIn,
    FillAlphaMixIn,
    AppendFillAlphaAttrExpressionMixIn,
    SvgTextSkipFillAlphaExpAppendingMixIn,
    LineColorMixIn,
    AppendLineColorAttrExpressionMixIn,
    SvgTextSkipLineColorExpAppendingMixIn,
    LineAlphaMixIn,
    AppendLineAlphaAttrExpressionMixIn,
    SvgTextSkipLineAlphaExpAppendingMixIn,
    AppendLineThicknessAttrExpressionMixIn,
    LineThicknessMixIn,
    SvgTextSkipLineThicknessExpAppendingMixIn,
    SvgTextTextMixIn,
    SvgTextSetTextValueMixIn,
    SvgTextFontFamilyMixIn,
    SvgTextSetFontFamilyMixIn,
    SvgTextFontSizeMixIn,
    SvgTextSetFontSizeValueMixIn,
    SvgTextItalicMixIn,
    SvgTextSetItalicMixIn,
    SvgTextBoldMixIn,
    SvgTextSetBoldMixIn,
    SvgTextDeltaXMixIn,
    SvgTextSetDeltaXMixIn,
    SvgTextDeltaYMixIn,
    SvgTextSetDeltaYMixIn,
    GetBoundsMixIn,
    VariableNameSuffixMixIn,
    InitializeWithBaseValueInterface,
):
    """
    The class for an SVG text-span (the child class of `SvgText`).

    Notes
    -----
    - If style settings are `None`, its styles inherit parent
        style settings.

    References
    ----------
    - SvgText class
        - https://simon-ritchie.github.io/apysc/en/svg_text.html
    - SvgTextSpan class
        - https://simon-ritchie.github.io/apysc/en/svg_text_span.html
    """

    # text
    @arg_validation_decos.is_string(arg_position_index=1, optional=False)
    # font_size
    @arg_validation_decos.is_integer(arg_position_index=2, optional=True)
    # font_family
    @arg_validation_decos.is_builtin_str_list_or_apysc_str_arr(
        arg_position_index=3, optional=True
    )
    # fill_color
    @arg_validation_decos.is_color(arg_position_index=4, optional=True)
    # fill_alpha
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=5, optional=True)
    # line_color
    @arg_validation_decos.is_color(arg_position_index=6, optional=True)
    # line_alpha
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=7, optional=True)
    # line_thickness
    @arg_validation_decos.is_integer(arg_position_index=8, optional=True)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=8, optional=True)
    # bold
    @arg_validation_decos.is_boolean(arg_position_index=9, optional=True)
    # italic
    @arg_validation_decos.is_boolean(arg_position_index=10, optional=True)
    # delta_x
    @arg_validation_decos.is_num(arg_position_index=11, optional=False)
    # delta_y
    @arg_validation_decos.is_num(arg_position_index=12, optional=False)
    # variable_name_suffix
    @arg_validation_decos.is_builtin_string(arg_position_index=13, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        *,
        text: Union[str, String],
        font_size: Optional[Union[int, Int]] = None,
        font_family: Optional[Union[Array[String], List[str]]] = None,
        fill_color: Optional[Color] = None,
        fill_alpha: Optional[Union[float, Number]] = None,
        line_color: Optional[Color] = None,
        line_alpha: Optional[Union[float, Number]] = None,
        line_thickness: Optional[Union[int, Int]] = None,
        bold: Optional[Union[bool, Boolean]] = None,
        italic: Optional[Union[bool, Boolean]] = None,
        delta_x: Union[float, Number] = 0.0,
        delta_y: Union[float, Number] = 0.0,
        variable_name_suffix: str = "",
    ) -> None:
        """
        The class for an SVG text-span (the child class of `SvgText`).

        Notes
        -----
        - If style settings are `None`, its styles inherit parent
            style settings.

        References
        ----------
        - SvgText class
            - https://simon-ritchie.github.io/apysc/en/svg_text.html
        - SvgTextSpan class
            - https://simon-ritchie.github.io/apysc/en/svg_text_span.html

        Parameters
        ----------
        text : Union[str, String]
            A text to use in this class.
        font_size : Optional[Union[int, Int]], optional
            A font-size setting.
        font_family : Optional[Union[Array[String], List[str]]], optional
            A font-family setting.
            Each string in an array needs to be a font name (e.g., `Times New Roman`).
        fill_color : Optional[Color], optional
            A fill-color setting.
        fill_alpha : Optional[Union[float, Number]], optional
            A fill-alpha setting.
        line_color : Optional[Color], optional
            A line-color setting.
        line_alpha : Optional[Union[float, Number]], optional
            A line-alpha setting.
        line_thickness : Optional[Union[int, Int]], optional
            A line-thickness (line-width) to set.
        bold : Optional[Union[bool, Boolean]], optional
            A boolean, whether this text is a bold style or not.
        italic : Optional[Union[bool, Boolean]], optional
            A boolean, whether a text is an italic style or not (normal).
        delta_x : Union[float, Number], optional
            A coordinate delta-x setting.
            Notes: This setting also changes a coordinate of subsequent
            `SvgTextSpan`'s instance.
        delta_y : Union[float, Number], optional
            A coordinate delta-y setting.
            Notes: This setting also changes a coordinate of subsequent
            `SvgTextSpan`'s instance.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage(
        ...     background_color=ap.Color("#333"), stage_width=200, stage_height=50
        ... )
        >>> svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
        ...     text_spans=[
        ...         ap.SvgTextSpan(text="Hello, "),
        ...         ap.SvgTextSpan(text="Hello, ", font_size=14),
        ...     ],
        ...     font_size=20,
        ...     fill_color=ap.Color("#0af"),
        ... )
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.SVG_TEXT_SPAN,
        )
        self.variable_name = variable_name
        self._variable_name_suffix = variable_name_suffix
        self._set_fill_color_expression_skipping_attr(fill_color=fill_color)
        self._set_fill_alpha_expression_skipping_attr(fill_alpha=fill_alpha)
        self._set_line_color_expression_skipping_attr(line_color=line_color)
        self._set_line_alpha_expression_skipping_attr(line_alpha=line_alpha)
        self._set_line_thickness_expression_skipping_attr(line_thickness=line_thickness)
        self._set_initial_basic_values(
            fill_color=_get_init_fill_color(fill_color=fill_color),
            fill_alpha=_get_init_fill_alpha_num(fill_alpha=fill_alpha),
            line_color=_get_init_line_color(line_color=line_color),
            line_thickness=_get_init_line_thickness_num(line_thickness=line_thickness),
            line_alpha=_get_init_line_alpha_num(line_alpha=line_alpha),
            line_cap=None,
            line_joints=None,
        )
        self._append_constructor_expression()
        self._set_text_value(text=text)
        self._set_font_size_value(font_size=font_size)
        self._set_font_family(font_family=font_family)
        self._set_bold(bold=bold)
        self._set_italic(italic=italic)
        self._set_delta_x(delta_x=delta_x)
        self._set_delta_y(delta_y=delta_y)

        super(SvgTextSpan, self).__init__(variable_name=variable_name)
        self._set_overflow_visible_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_constructor_expression(self) -> None:
        """
        Append a constructor expression string.
        """
        from apysc._display.svg_text import SvgText
        from apysc._display.svg_text_singleton_for_text_span import (
            SvgTextSingletonForTextSpan,
        )
        from apysc._expression import expression_data_util

        INDENT_NUM: int = 2
        parent: SvgText = SvgTextSingletonForTextSpan.get_instance()
        variable_name: str = self.variable_name
        expression: str = (
            f"var {variable_name} = {parent.variable_name}" "\n  .tspan()\n  .attr({"
        )
        expression = self._append_fill_color_attr_expression(
            expression=expression,
            indent_num=INDENT_NUM,
            skip_appending=self._skip_fill_color_expression_appending,
        )
        expression = self._append_fill_alpha_attr_expression(
            expression=expression,
            indent_num=INDENT_NUM,
            skip_appending=self._skip_fill_alpha_expression_appending,
        )
        expression = self._append_line_color_attr_expression(
            expression=expression,
            indent_num=INDENT_NUM,
            skip_appending=self._skip_line_color_expression_appending,
        )
        expression = self._append_line_thickness_attr_expression(
            expression=expression,
            indent_num=INDENT_NUM,
            skip_appending=self._skip_line_thickness_expression_appending,
        )
        expression = self._append_line_alpha_attr_expression(
            expression=expression,
            indent_num=INDENT_NUM,
            skip_appending=self._skip_line_alpha_expression_appending,
        )
        expression += "\n});"
        expression_data_util.append_js_expression(expression=expression)

    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of
        debugging).

        Returns
        -------
        repr_str : str
            This interface returns a type name and variable name
            (e.g., `SvgTextSpan("<variable_name>")`).
        """
        repr_str: str = f'{SvgTextSpan.__name__}("{self.variable_name}")'
        return repr_str

    @classmethod
    @final
    def _initialize_with_base_value(cls) -> "SvgTextSpan":
        """
        Initialize this class with a base value(s).

        Returns
        -------
        svg_text_span : SvgTextSpan
            An initialized text span instance.
        """
        svg_text_span: SvgTextSpan = SvgTextSpan(text="")
        svg_text_span.visible = Boolean(False)
        return svg_text_span


def _get_init_line_color(*, line_color: Optional[Color]) -> Color:
    """
    Get an initial line-color.

    Parameters
    ----------
    line_color : Optional[Color]
        A line-color.

    Returns
    -------
    line_color_ : Color
        If the specified value is None, this interface returns the COLORLESS
        constant.
    """
    if line_color is None:
        return COLORLESS
    return line_color


def _get_init_fill_alpha_num(
    *, fill_alpha: Optional[Union[float, Number]]
) -> Union[float, Number]:
    """
    Get an initial fill-alpha number.

    Parameters
    ----------
    fill_alpha : Optional[Union[float, Number]]
        A fill-alpha setting.

    Returns
    -------
    fill_alpha_ : Union[float, Number]
        If the specified value is None, this interface returns a 1.0 number.
    """
    if fill_alpha is None:
        return 1.0
    return fill_alpha


def _get_init_fill_color(*, fill_color: Optional[Color]) -> Color:
    """
    Get an initial fill-color.

    Parameters
    ----------
    fill_color : Optional[Color]
        A fill-color setting.

    Returns
    -------
    fill_color_ : Color
        If the specified value is None, this interface returns the COLORLESS
        constant.
    """
    if fill_color is None:
        return COLORLESS
    return fill_color


def _get_init_line_alpha_num(
    *,
    line_alpha: Optional[Union[float, Number]],
) -> Union[float, Number]:
    """
    Get an initial line-alpha number.

    Parameters
    ----------
    line_alpha : Optional[Union[float, Number]]
        A line-alpha setting.

    Returns
    -------
    line_alpha_ : Union[float, Number]
        If the specified value is None, this interface returns a 1.0 number.
    """
    if line_alpha is None:
        return 1.0
    return line_alpha


def _get_init_line_thickness_num(
    *,
    line_thickness: Optional[Union[int, Int]],
) -> Union[int, Int]:
    """
    Get an initial line-thickness (line-width) number.

    Parameters
    ----------
    line_thickness : Optional[Union[int, Int]]
        A line-thickness (line-width) setting.

    Returns
    -------
    line_thickness_ : Union[int, Int]
        If the specified value is None, this interface returns 1 number.
    """
    if line_thickness is None:
        return 1
    return line_thickness

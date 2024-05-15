"""Class implementation for an SVG text.
"""

from typing import List
from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._color.color import Color
from apysc._color.colorless import COLORLESS
from apysc._color.colors import Colors
from apysc._color.copy_color_if_default_value_specified_mixin import (
    CopyColorIfDefaultValueSpecifiedMixIn,
)
from apysc._display.add_to_parent_mixin import AddToParentMixIn
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
from apysc._display.append_x_attr_expression_mixin import AppendXAttrExpressionMixIn
from apysc._display.append_y_attr_expression_mixin import AppendYAttrExpressionMixIn
from apysc._display.child_mixin import ChildMixIn
from apysc._display.css_mixin import CssMixIn
from apysc._display.fill_alpha_mixin import FillAlphaMixIn
from apysc._display.fill_color_mixin import FillColorMixIn
from apysc._display.flip_x_mixin import FlipXMixIn
from apysc._display.flip_y_mixin import FlipYMixIn
from apysc._display.get_bounds_mixin import GetBoundsMixIn
from apysc._display.graphics_base import GraphicsBase
from apysc._display.line_alpha_mixin import LineAlphaMixIn
from apysc._display.line_color_mixin import LineColorMixIn
from apysc._display.line_thickness_mixin import LineThicknessMixIn
from apysc._display.rotation_around_center_mixin import RotationAroundCenterMixIn
from apysc._display.rotation_around_point_mixin import RotationAroundPointMixIn
from apysc._display.scale_x_from_center_mixin import ScaleXFromCenterMixIn
from apysc._display.scale_x_from_point_mixin import ScaleXFromPointMixIn
from apysc._display.set_overflow_visible_setting_mixin import (
    SetOverflowVisibleSettingMixIn,
)
from apysc._display.skew_x_mixin import SkewXMixIn
from apysc._display.skew_y_mixin import SkewYMixIn
from apysc._display.svg_text_align_mixin import SvgTextAlign
from apysc._display.svg_text_align_mixin import SvgTextAlignMixIn
from apysc._display.svg_text_bold_mixin import SvgTextBoldMixIn
from apysc._display.svg_text_font_family_mixin import SvgTextFontFamilyMixIn
from apysc._display.svg_text_font_size_mixin import SvgTextFontSizeMixIn
from apysc._display.svg_text_italic_mixin import SvgTextItalicMixIn
from apysc._display.svg_text_leading_mixin import SvgTextLeadingMixIn
from apysc._display.svg_text_set_align_mixin import SvgTextSetAlignMixIn
from apysc._display.svg_text_set_bold_mixin import SvgTextSetBoldMixIn
from apysc._display.svg_text_set_font_family_mixin import SvgTextSetFontFamilyMixIn
from apysc._display.svg_text_set_font_size_value_mixin import (
    SvgTextSetFontSizeValueMixIn,
)
from apysc._display.svg_text_set_italic_mixin import SvgTextSetItalicMixIn
from apysc._display.svg_text_set_leading_mixin import SvgTextSetLeadingMixIn
from apysc._display.svg_text_set_text_value_mixin import SvgTextSetTextValueMixIn
from apysc._display.svg_text_span import SvgTextSpan
from apysc._display.svg_text_text_mixin import SvgTextTextMixIn
from apysc._display.x_mixin import XMixIn
from apysc._display.y_mixin import YMixIn
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


class SvgText(
    ReprInterface,
    XMixIn,
    AppendXAttrExpressionMixIn,
    YMixIn,
    AppendYAttrExpressionMixIn,
    SetOverflowVisibleSettingMixIn,
    CssMixIn,
    GraphicsBase,
    RotationAroundCenterMixIn,
    RotationAroundPointMixIn,
    ScaleXFromCenterMixIn,
    ScaleXFromPointMixIn,
    FlipXMixIn,
    FlipYMixIn,
    SkewXMixIn,
    SkewYMixIn,
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
    SvgTextTextMixIn,
    SvgTextSetTextValueMixIn,
    SvgTextFontFamilyMixIn,
    SvgTextSetFontFamilyMixIn,
    SvgTextFontSizeMixIn,
    SvgTextSetFontSizeValueMixIn,
    SvgTextLeadingMixIn,
    SvgTextSetLeadingMixIn,
    SvgTextAlignMixIn,
    SvgTextSetAlignMixIn,
    SvgTextItalicMixIn,
    SvgTextSetItalicMixIn,
    SvgTextBoldMixIn,
    SvgTextSetBoldMixIn,
    GetBoundsMixIn,
    VariableNameSuffixMixIn,
    InitializeWithBaseValueInterface,
    CopyColorIfDefaultValueSpecifiedMixIn,
    AddToParentMixIn,
):
    """
    The class for an SVG text.

    Notes
    -----
    - SvgText's y-coordinate zero-position starts at the bottom of a text.
        So if you set y=0, a text becomes almost invisible.

    References
    ----------
    - SvgText class
        - https://simon-ritchie.github.io/apysc/en/svg_text.html

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage(
    ...     background_color=ap.Color("#333"),
    ...     stage_width=200,
    ...     stage_height=50,
    ... )
    >>> svg_text: ap.SvgText = ap.SvgText(
    ...     text="Hello, world!",
    ...     font_size=20,
    ...     fill_color=ap.Color("#0af"),
    ... )
    >>> svg_text.text
    String("Hello, world!")
    >>> svg_text.font_size
    Int(20)
    >>> svg_text.fill_color
    Color("#00aaff")
    """

    # text
    @arg_validation_decos.is_string(arg_position_index=1, optional=False)
    # font_size
    @arg_validation_decos.is_integer(arg_position_index=2, optional=False)
    # font_family
    @arg_validation_decos.is_builtin_str_list_or_apysc_str_arr(
        arg_position_index=3, optional=True
    )
    # x
    @arg_validation_decos.is_num(arg_position_index=4, optional=False)
    # y
    @arg_validation_decos.is_num(arg_position_index=5, optional=False)
    # fill_color
    @arg_validation_decos.is_color(arg_position_index=6, optional=False)
    # fill_alpha
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=7, optional=False)
    # line_color
    @arg_validation_decos.is_color(arg_position_index=8, optional=False)
    # line_alpha
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=9, optional=False)
    # line_thickness
    @arg_validation_decos.is_integer(arg_position_index=10, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=10, optional=False)
    # leading
    @arg_validation_decos.is_num(arg_position_index=11, optional=False)
    # align
    @arg_validation_decos.is_svg_text_align(arg_position_index=12)
    # bold
    @arg_validation_decos.is_boolean(arg_position_index=13, optional=False)
    # italic
    @arg_validation_decos.is_boolean(arg_position_index=14, optional=False)
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
        y: Union[float, Number] = 16.0,
        fill_color: Color = Colors.GRAY_666666,
        fill_alpha: Union[float, Number] = 1.0,
        line_color: Color = COLORLESS,
        line_alpha: Union[float, Number] = 1.0,
        line_thickness: Union[int, Int] = 1,
        leading: Union[float, Number] = 1.5,
        align: SvgTextAlign = SvgTextAlign.LEFT,
        bold: Union[bool, Boolean] = False,
        italic: Union[bool, Boolean] = False,
        parent: Optional[ChildMixIn] = None,
        variable_name_suffix: str = "",
    ) -> None:
        """
        The class for an SVG text.

        Notes
        -----
        - SvgText's y-coordinate zero-position starts at the bottom of a text.
            So if you set y=0, a text becomes almost invisible.

        References
        ----------
        - SvgText class
            - https://simon-ritchie.github.io/apysc/en/svg_text.html

        Parameters
        ----------
        text : Union[str, String]
            A text to use in this class.
        font_size : Union[int, Int], optional
            A font-size setting.
        font_family : Optional[Union[Array[String], List[str]]], optional
            A font-family setting.
            Each string in an array needs to be a font name (e.g., `Times New Roman`).
        x : float or Number, optional
            X-coordinate to start drawing.
        y : float or Number, optional
            Y-coordinate to start drawing (please see also the `Notes` section).
        fill_color : Color
            A fill-color setting.
        fill_alpha : float or Number, optional
            A fill-alpha setting.
        line_color : Color, optional
            A line-color setting.
        line_alpha : float or Number, optional
            A line-alpha setting.
        line_thickness : int or Int, optional
            A line-thickness (line-width) setting.
        leading : float or Number, optional
            A text-leading size.
        align : SvgTextAlign, default SvgTextAlign.LEFT
            A text-align setting.
        bold : Union[bool, Boolean], optional
            A boolean, whether this text is a bold style or not.
        italic : Union[bool, Boolean], optional
            A boolean, whether a text is an italic style or not (normal).
        parent : ChildMixIn or None, optional
            A parent instance to add this instance.
            If the specified value is None, this interface uses
            a stage instance.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage(
        ...     background_color=ap.Color("#333"),
        ...     stage_width=200,
        ...     stage_height=50,
        ...     stage_elem_id="stage",
        ... )
        >>> svg_text: ap.SvgText = ap.SvgText(
        ...     text="Hello, world!",
        ...     font_size=20,
        ...     fill_color=ap.Color("#0af"),
        ... )
        >>> svg_text.text
        String("Hello, world!")
        >>> svg_text.font_size
        Int(20)
        >>> svg_text.fill_color
        Color("#00aaff")
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        fill_color = self._copy_color_if_default_value_specified(
            color=fill_color,
            default_color=Colors.GRAY_666666,
        )

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

        super(SvgText, self).__init__(
            variable_name=variable_name,
        )

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

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_constructor_expression(self) -> None:
        """
        Append a constructor expression string.
        """
        from apysc._display.stage import Stage
        from apysc._display.stage import get_stage
        from apysc._expression import expression_data_util

        INDENT_NUM: int = 2
        variable_name: str = self.variable_name
        stage: Stage = get_stage()
        expression: str = (
            f"var {variable_name} = {stage.variable_name}" "\n  .text()\n  .attr({"
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
        expression = self._append_x_attr_expression(
            expression=expression, indent_num=INDENT_NUM
        )
        expression = self._append_y_attr_expression(
            expression=expression, indent_num=INDENT_NUM
        )
        expression += "\n  });"
        expression_data_util.append_js_expression(expression=expression)

    @classmethod
    # text_spans
    @arg_validation_decos.are_text_spans(arg_position_index=1)
    # font_size
    @arg_validation_decos.is_integer(arg_position_index=2, optional=False)
    # font_family
    @arg_validation_decos.is_builtin_str_list_or_apysc_str_arr(
        arg_position_index=3, optional=True
    )
    # x
    @arg_validation_decos.is_num(arg_position_index=4, optional=False)
    # y
    @arg_validation_decos.is_num(arg_position_index=5, optional=False)
    # fill_color
    @arg_validation_decos.is_color(arg_position_index=6, optional=False)
    # fill_alpha
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=7, optional=False)
    # line_color
    @arg_validation_decos.is_color(arg_position_index=8, optional=False)
    # line_alpha
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=9, optional=False)
    # line_thickness
    @arg_validation_decos.is_integer(arg_position_index=10, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=10, optional=False)
    # leading
    @arg_validation_decos.is_num(arg_position_index=11, optional=False)
    # align
    @arg_validation_decos.is_svg_text_align(arg_position_index=12)
    # bold
    @arg_validation_decos.is_boolean(arg_position_index=13, optional=False)
    # italic
    @arg_validation_decos.is_boolean(arg_position_index=14, optional=False)
    # parent
    @arg_validation_decos.is_display_object_container(
        arg_position_index=15, optional=True
    )
    # variable_name_suffix
    @arg_validation_decos.is_builtin_string(arg_position_index=16, optional=False)
    def create_with_svg_text_spans(
        cls,
        *,
        text_spans: Union[List[SvgTextSpan], Array[SvgTextSpan]],
        font_size: Union[int, Int] = 16,
        font_family: Optional[Union[Array[String], List[str]]] = None,
        x: Union[float, Number] = 0.0,
        y: Union[float, Number] = 16.0,
        fill_color: Color = Colors.GRAY_666666,
        fill_alpha: Union[float, Number] = 1.0,
        line_color: Color = COLORLESS,
        line_alpha: Union[float, Number] = 1.0,
        line_thickness: Union[int, Int] = 1,
        leading: Union[float, Number] = 1.5,
        align: SvgTextAlign = SvgTextAlign.LEFT,
        bold: Union[bool, Boolean] = False,
        italic: Union[bool, Boolean] = False,
        parent: Optional[ChildMixIn] = None,
        variable_name_suffix: str = "",
    ) -> "SvgText":
        """
        Create an `SvgText` instance with specified text spans.

        Notes
        -----
        - SvgText's y-coordinate zero-position starts at the bottom of a text.
            So if you set y=0, a text becomes almost invisible.

        References
        ----------
        - SvgText class
            - https://simon-ritchie.github.io/apysc/en/svg_text.html
        - SvgTextSpan class
            - https://simon-ritchie.github.io/apysc/en/svg_text_span.html

        Parameters
        ----------
        text_spans : Union[List[SvgTextSpan], Array[SvgTextSpan]]
            Text spans.
        font_size : Union[int, Int], optional
            A font-size setting for an overall text.
        font_family : Optional[Union[Array[String], List[str]]], optional
            A font-family setting for an overall text.
            Each string in an array needs to be a font name (e.g., `Times New Roman`).
        x : Union[float, Number], optional
            X-coordinate to start drawing.
        y : Union[float, Number], optional
            Y-coordinate to start drawing (please see also the `Notes` section).
        fill_color : Color, optional
            A fill-color setting for an overall text.
        fill_alpha : float or Number, optional
            A fill-alpha setting for an overall text.
        line_color : Color, optional
            A line-color setting for an overall text.
        line_alpha : float or Number, optional
            A line-alpha setting for an overall text.
        line_thickness : int or Int, optional
            A line-thickness (line-width) setting for an overall text.
        leading : float or Number, optional
            A text-leading size for an overall text.
        align : SvgTextAlign, optional
            A text-align setting for an overall text.
        bold : Union[bool, Boolean], optional
            A boolean, whether this text is a bold style or not.
        italic : Union[bool, Boolean], optional
            A boolean, whether a text is an italic style or not (normal).
        parent : Optional[ChildMixIn], optional
            A parent instance to add this instance.
            If the specified value is None, this interface uses
            a stage instance.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        svg_text : SvgText
            A created `SvgText` instance.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage(
        ...     background_color=ap.Color("#333"),
        ...     stage_width=200,
        ...     stage_height=50,
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
        from apysc._expression import expression_data_util
        from apysc._loop.for_array_indices import ForArrayIndices

        svg_text: SvgText = SvgText(
            text="",
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
        text_spans_: Array[SvgTextSpan] = svg_text._convert_text_spans_list_to_array(
            text_spans=text_spans
        )
        i: Int
        with ForArrayIndices(
            arr=text_spans_,
            locals_=locals(),
            globals_=globals(),
        ) as i:
            text_span: SvgTextSpan = text_spans_[i]
            expression: str = (
                f"{svg_text.variable_name}.add({text_span.variable_name});"
            )
            expression_data_util.append_js_expression(expression=expression)
        return svg_text

    @final
    @add_debug_info_setting(module_name=__name__)
    def _convert_text_spans_list_to_array(
        self,
        *,
        text_spans: Union[List[SvgTextSpan], Array[SvgTextSpan]],
    ) -> Array[SvgTextSpan]:
        """
        Convert text spans' list to an array.

        Parameters
        ----------
        text_spans : Union[List[SvgTextSpan], Array[SvgTextSpan]]
            Text spans.

        Returns
        -------
        text_spans_ : Array[SvgTextSpan]
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
        text_spans_: Array[SvgTextSpan] = Array(text_spans, variable_name_suffix=suffix)
        return text_spans_

    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of
        debugging).

        Returns
        -------
        repr_str : str
            This interface returns a type name and variable name
            (e.g., `SvgText("<variable_name>")`).
        """

        repr_str: str = f'{SvgText.__name__}("{self.variable_name}")'
        return repr_str

    @classmethod
    @final
    def _initialize_with_base_value(cls) -> "SvgText":
        """
        Initialize this class with a base value(s).

        Returns
        -------
        svg_text : SvgText
            An initialized svg text instance.
        """
        svg_text: SvgText = SvgText(text="")
        svg_text.visible = Boolean(False)
        return svg_text

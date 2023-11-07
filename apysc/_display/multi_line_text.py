"""The class implementation for the `MultiLineText` class.
"""

from typing import Optional
from typing import Union

from apysc._color.color import Color
from apysc._color.colors import Colors
from apysc._display.add_foreign_object_child_mixin import AddForeignObjectChildMixIn
from apysc._display.add_to_parent_mixin import AddToParentMixIn
from apysc._display.append_foreign_object_constructor_expression_mixin import (
    AppendForeignObjectConstructorExpressionMixIn,
)
from apysc._display.child_mixin import ChildMixIn
from apysc._display.css_mixin import CssMixIn
from apysc._display.css_text_align import CssTextAlign
from apysc._display.css_text_align_last import CssTextAlignLast
from apysc._display.display_object import DisplayObject
from apysc._display.opacity_css_mixin import OpacityCssMixIn
from apysc._display.set_overflow_visible_setting_mixin import (
    SetOverflowVisibleSettingMixIn,
)
from apysc._display.svg_foreign_object_child_mixin import SvgForeignObjectChildMixIn
from apysc._display.svg_foreign_object_initialize_width_mixin import (
    SVGForeignObjectInitializeWidthMixIn,
)
from apysc._display.svg_foreign_object_text_mixin import SVGForeignObjectTextMixIn
from apysc._display.text_align_css_mixin import TextAlignCssMixIn
from apysc._display.text_align_last_css_mixin import TextAlignLastCssMixIn
from apysc._display.text_bold_css_mixin import TextBoldCssMixIn
from apysc._display.text_fill_color_css_mixin import TextFillColorCssMixIn
from apysc._display.text_italic_css_mixin import TextItalicCssMixIn
from apysc._display.width_mixin import WidthMixIn
from apysc._display.x_mixin import XMixIn
from apysc._display.y_mixin import YMixIn
from apysc._loop.initialize_with_base_value_interface import (
    InitializeWithBaseValueInterface,
)
from apysc._type.boolean import Boolean
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos


class MultiLineText(
    XMixIn,
    YMixIn,
    DisplayObject,
    WidthMixIn,
    VariableNameSuffixMixIn,
    CssMixIn,
    SetOverflowVisibleSettingMixIn,
    InitializeWithBaseValueInterface,
    AddForeignObjectChildMixIn,
    AppendForeignObjectConstructorExpressionMixIn,
    SVGForeignObjectInitializeWidthMixIn,
    SVGForeignObjectTextMixIn,
    SvgForeignObjectChildMixIn,
    AddToParentMixIn,
    TextFillColorCssMixIn,
    OpacityCssMixIn,
    TextBoldCssMixIn,
    TextItalicCssMixIn,
    TextAlignCssMixIn,
    TextAlignLastCssMixIn,
):
    # text
    @arg_validation_decos.is_string(arg_position_index=1, optional=False)
    # x
    @arg_validation_decos.is_num(arg_position_index=2, optional=False)
    # y
    @arg_validation_decos.is_num(arg_position_index=3, optional=False)
    # width
    @arg_validation_decos.is_integer(arg_position_index=4, optional=False)
    # fill_color
    @arg_validation_decos.is_color(arg_position_index=5, optional=False)
    # fill_alpha
    @arg_validation_decos.is_num(arg_position_index=6, optional=False)
    # bold
    @arg_validation_decos.is_boolean(arg_position_index=7, optional=False)
    # italic
    @arg_validation_decos.is_boolean(arg_position_index=8, optional=False)
    # text_align
    @arg_validation_decos.is_css_text_align(arg_position_index=9)
    # text_align_last
    @arg_validation_decos.is_css_text_align_last(arg_position_index=10)
    # parent
    @arg_validation_decos.is_display_object_container(
        arg_position_index=11, optional=True
    )
    def __init__(
        self,
        *,
        text: Union[str, String],
        x: Union[float, Number] = 0,
        y: Union[float, Number] = 0,
        width: Union[int, Int] = 200,
        fill_color: Color = Colors.GRAY_666666,
        fill_alpha: Union[float, Number] = 1.0,
        bold: Union[bool, Boolean] = False,
        italic: Union[bool, Boolean] = False,
        text_align: CssTextAlign = CssTextAlign.LEFT,
        text_align_last: CssTextAlignLast = CssTextAlignLast.LEFT,
        parent: Optional[ChildMixIn] = None,
        variable_name_suffix: str = "",
    ) -> None:
        """
        The class implementation for a multiline text element.

        Parameters
        ----------
        text : Union[str, String]
            Text to display. An HTML tag is available.
        x : Union[float, Number], default 0
            X-coordinate.
        y : Union[float, Number], default 0
            Y-coordinate.
        width : Union[int, Int], default 200
            Width of the text to wrap.
        fill_color : Color, default Colors.GRAY_666666
            Text color.
        fill_alpha : Union[float, Number], default 1.0
            Text alpha (opacity). The minimum value is 0.0 (transparent),
            and the maximum value is 1.0 (solid).
        bold : Union[bool, Boolean], default False
            Whether to display the text in bold.
        italic : Union[bool, Boolean], default False
            Whether to display the text in italic.
        text_align : CssTextAlign, default `CssTextAlign.LEFT`
            Text align setting.
        text_align_last : CssTextAlignLast, default `CssTextAlignLast.LEFT`
            Last line's text-align setting.
        parent : ChildMixIn or None, default None
            A parent instance to add this instance.
            If the specified value is None, this interface uses
            a stage instance.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        from apysc._converter import to_apysc_val_from_builtin
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        self._variable_name_suffix = variable_name_suffix
        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.MULTILINE_TEXT,
        )
        super(MultiLineText, self).__init__(variable_name=variable_name)
        self._initialize_width(width=width)
        self._append_foreign_object_constructor_expression()
        self._add_to_parent(parent=parent)
        self._set_overflow_visible_setting()
        self._initialize_text(text=text)
        self._initialize_svg_foreign_object_child(
            html_str=self._text, variable_name_suffix=variable_name_suffix
        )
        self.x = to_apysc_val_from_builtin.get_copied_number_from_builtin_val(
            float_or_num=x
        )
        self.y = to_apysc_val_from_builtin.get_copied_number_from_builtin_val(
            float_or_num=y
        )
        self.fill_color = fill_color._copy()
        self.fill_alpha = to_apysc_val_from_builtin.get_copied_number_from_builtin_val(
            float_or_num=fill_alpha,
            variable_name_suffix=variable_name_suffix,
        )
        self.bold = to_apysc_val_from_builtin.get_copied_boolean_from_builtin_val(
            bool_val=bold,
            variable_name_suffix=variable_name_suffix,
        )
        self.italic = to_apysc_val_from_builtin.get_copied_boolean_from_builtin_val(
            bool_val=italic,
            variable_name_suffix=variable_name_suffix,
        )
        self.text_align = text_align
        self.text_align_last = text_align_last

    @classmethod
    def _initialize_with_base_value(cls) -> "MultiLineText":
        """
        Initialize this class with a base value(s).

        Returns
        -------
        text : MultiLineText
            An initialized instance.
        """
        text: MultiLineText = cls(text="", width=0)
        return text

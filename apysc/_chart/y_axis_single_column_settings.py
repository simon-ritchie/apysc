# mypy: disable-error-code=assignment

"""Class implementation for the single y-axis settings.
"""

from typing import List
from typing import Optional
from typing import TypeVar
from typing import Union

from apysc._chart.axis_label_bold_mixin import AxisLabelBoldMixIn
from apysc._chart.axis_label_fill_alpha_mixin import AxisLabelFillAlphaMixIn
from apysc._chart.axis_label_fill_color_mixin import AxisLabelFillColorMixIn
from apysc._chart.axis_label_font_family_mixin import AxisLabelFontFamilyMixIn
from apysc._chart.axis_label_font_size_mixin import AxisLabelFontSizeMixIn
from apysc._chart.axis_label_italic_mixin import AxisLabelItalicMixIn
from apysc._chart.axis_line_alpha_mixin import AxisLineAlphaMixIn
from apysc._chart.axis_line_color_mixin import AxisLineColorMixIn
from apysc._chart.axis_line_thickness_mixin import AxisLineThicknessMixIn
from apysc._chart.tick_culling_max_mixin import TickCullingMaxMixIn
from apysc._chart.tick_text_bold_mixin import TickTextBoldMixIn
from apysc._chart.tick_text_fill_alpha_mixin import TickTextFillAlphaMixIn
from apysc._chart.tick_text_fill_color_mixin import TickTextFillColorMixIn
from apysc._chart.tick_text_font_family_mixin import TickTextFontFamilyMixIn
from apysc._chart.tick_text_font_size_mixin import TickTextFontSizeMixIn
from apysc._chart.tick_text_italic_mixin import TickTextItalicMixIn
from apysc._chart.is_display_axis_label_mixin import IsDisplayAxisLabelMixIn
from apysc._chart.tick_culling_max_mixin import TickCullingMaxMixIn
from apysc._chart.tick_text_bold_mixin import TickTextBoldMixIn
from apysc._chart.tick_text_fill_alpha_mixin import TickTextFillAlphaMixIn
from apysc._chart.tick_text_fill_color_mixin import TickTextFillColorMixIn
from apysc._chart.tick_text_font_family_mixin import TickTextFontFamilyMixIn
from apysc._chart.tick_text_font_size_mixin import TickTextFontSizeMixIn
from apysc._chart.tick_text_italic_mixin import TickTextItalicMixIn
from apysc._chart.y_axis_column_name_mixin import YAxisColumnNameMixIn
from apysc._type.array import Array
from apysc._type.boolean import Boolean
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String
from apysc._validation import arg_validation_decos

_StrOrString = TypeVar("_StrOrString", str, String)


class YAxisSingleColumnSettings(
    YAxisColumnNameMixIn,
    TickCullingMaxMixIn,
    TickTextFontSizeMixIn,
    TickTextFontFamilyMixIn,
    TickTextFillColorMixIn,
    TickTextFillAlphaMixIn,
    TickTextBoldMixIn,
    TickTextItalicMixIn,
    AxisLineColorMixIn,
    AxisLineThicknessMixIn,
    AxisLineAlphaMixIn,
    IsDisplayAxisLabelMixIn,
    AxisLabelFontSizeMixIn,
    AxisLabelFontFamilyMixIn,
    AxisLabelFillColorMixIn,
    AxisLabelFillAlphaMixIn,
    AxisLabelBoldMixIn,
    AxisLabelItalicMixIn,
):
    def __init__(
        self,
        *,
        y_axis_column_name: Union[str, String],
        tick_culling_max: Optional[Union[int, Int]] = None,
        tick_text_font_size: Union[int, Int] = 12,
        tick_text_font_family: Optional[Union[Array[String], List[str]]] = None,
        tick_text_fill_color: _StrOrString = "#666666",
        tick_text_fill_alpha: Union[float, Number] = 1.0,
        tick_text_bold: Union[bool, Boolean] = False,
        tick_text_italic: Union[bool, Boolean] = False,
        line_color: _StrOrString = "#666666",
        line_thickness: Union[int, Int] = 1,
        line_alpha: Union[float, Number] = 1.0,
        is_display_axis_label: Union[bool, Boolean] = True,
        # axis_label_position: ,
        axis_label_font_size: Union[int, Int] = 12,
        axis_label_font_family: Optional[Union[Array[String], List[str]]] = None,
        axis_label_fill_color: _StrOrString = "#666666",
        axis_label_fill_alpha: Union[float, Number] = 1.0,
        axis_label_bold: Union[bool, Boolean] = False,
        axis_label_italic: Union[bool, Boolean] = False,
        variable_name_suffix: str = "",
    ):
        self._set_initial_y_axis_column_name(
            y_axis_column_name=y_axis_column_name,
            variable_name_suffix=variable_name_suffix,
        )
        self._set_initial_tick_culling_max(
            tick_culling_max=tick_culling_max,
            variable_name_suffix=variable_name_suffix,
        )
        self._set_initial_tick_text_font_size(
            tick_text_font_size=tick_text_font_size,
            variable_name_suffix=variable_name_suffix,
        )
        self._set_initial_tick_text_font_family(
            tick_text_font_family=tick_text_font_family,
            variable_name_suffix=variable_name_suffix,
        )
        self._set_initial_tick_text_fill_color(
            tick_text_fill_color=tick_text_fill_color,
            variable_name_suffix=variable_name_suffix,
        )
        self._set_initial_tick_text_fill_alpha(
            tick_text_fill_alpha=tick_text_fill_alpha,
            variable_name_suffix=variable_name_suffix,
        )
        self._set_initial_tick_text_bold(
            tick_text_bold=tick_text_bold,
            variable_name_suffix=variable_name_suffix,
        )
        self._set_initial_tick_text_italic(
            tick_text_italic=tick_text_italic,
            variable_name_suffix=variable_name_suffix,
        )
        self._set_initial_line_color(
            line_color=line_color,
            variable_name_suffix=variable_name_suffix,
        )
        self._set_initial_line_thickness(
            line_thickness=line_thickness,
            variable_name_suffix=variable_name_suffix,
        )
        self._set_initial_line_alpha(
            line_alpha=line_alpha,
            variable_name_suffix=variable_name_suffix,
        )
        self._set_initial_is_display_axis_label(
            is_display_axis_label=is_display_axis_label,
            variable_name_suffix=variable_name_suffix,
        )
        self._set_initial_axis_label_font_size(
            axis_label_font_size=axis_label_font_size,
            variable_name_suffix=variable_name_suffix,
        )
        self._set_initial_axis_label_font_family(
            axis_label_font_family=axis_label_font_family,
            variable_name_suffix=variable_name_suffix,
        )
        self._set_initial_axis_label_fill_color(
            axis_label_fill_color=axis_label_fill_color,
            variable_name_suffix=variable_name_suffix,
        )
        self._set_initial_axis_label_fill_alpha(
            axis_label_fill_alpha=axis_label_fill_alpha,
            variable_name_suffix=variable_name_suffix,
        )
        self._set_initial_axis_label_bold(
            axis_label_bold=axis_label_bold,
            variable_name_suffix=variable_name_suffix,
        )
        self._set_initial_axis_label_italic(
            axis_label_italic=axis_label_italic,
            variable_name_suffix=variable_name_suffix,
        )

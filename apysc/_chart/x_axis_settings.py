# mypy: disable-error-code=assignment

"""Class implementation for the x-axis settings.
"""

from typing import List
from typing import Optional
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
from apysc._chart.is_display_axis_label_mixin import IsDisplayAxisLabelMixIn
from apysc._chart.tick_max_num_mixin import TickMaxNumMixIn
from apysc._chart.tick_text_bold_mixin import TickTextBoldMixIn
from apysc._chart.tick_text_fill_alpha_mixin import TickTextFillAlphaMixIn
from apysc._chart.tick_text_fill_color_mixin import TickTextFillColorMixIn
from apysc._chart.tick_text_font_family_mixin import TickTextFontFamilyMixIn
from apysc._chart.tick_text_font_size_mixin import TickTextFontSizeMixIn
from apysc._chart.tick_text_italic_mixin import TickTextItalicMixIn
from apysc._chart.x_axis_column_name_mixin import XAxisColumnNameMixIn
from apysc._chart.x_axis_label_position import XAxisLabelPosition
from apysc._chart.x_axis_label_position_mixin import XAxisLabelPositionMixIn
from apysc._color.color import Color
from apysc._color.colors import Colors
from apysc._type.array import Array
from apysc._type.boolean import Boolean
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String
from apysc._validation import arg_validation_decos


class XAxisSettings(
    XAxisColumnNameMixIn,
    TickMaxNumMixIn,
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
    XAxisLabelPositionMixIn,
    AxisLabelFontSizeMixIn,
    AxisLabelFontFamilyMixIn,
    AxisLabelFillColorMixIn,
    AxisLabelFillAlphaMixIn,
    AxisLabelBoldMixIn,
    AxisLabelItalicMixIn,
):
    # x_axis_column_name
    @arg_validation_decos.is_builtin_string(arg_position_index=1, optional=False)
    # tick_max_num
    @arg_validation_decos.is_integer(arg_position_index=2, optional=True)
    # tick_text_font_size
    @arg_validation_decos.is_integer(arg_position_index=3, optional=False)
    # tick_text_font_family
    @arg_validation_decos.is_builtin_str_list_or_apysc_str_arr(
        arg_position_index=4, optional=True
    )
    # tick_text_fill_color
    @arg_validation_decos.is_color(arg_position_index=5, optional=False)
    # tick_text_fill_alpha
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=6, optional=False)
    # tick_text_bold
    @arg_validation_decos.is_boolean(arg_position_index=7, optional=False)
    # tick_text_italic
    @arg_validation_decos.is_boolean(arg_position_index=8, optional=False)
    # line_color
    @arg_validation_decos.is_color(arg_position_index=9, optional=False)
    # line_thickness
    @arg_validation_decos.is_integer(arg_position_index=10, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=10, optional=False)
    # line_alpha
    @arg_validation_decos.is_num(arg_position_index=11, optional=False)
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=11, optional=False)
    # is_display_axis_label
    @arg_validation_decos.is_boolean(arg_position_index=12, optional=False)
    # axis_label_position
    @arg_validation_decos.is_x_axis_label_position(arg_position_index=13)
    # axis_label_font_size
    @arg_validation_decos.is_integer(arg_position_index=14, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=14, optional=False)
    # axis_label_font_family
    @arg_validation_decos.is_builtin_str_list_or_apysc_str_arr(
        arg_position_index=15, optional=True
    )
    # axis_label_fill_color
    @arg_validation_decos.is_color(arg_position_index=16, optional=False)
    # axis_label_fill_alpha
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=17, optional=False)
    # axis_label_bold
    @arg_validation_decos.is_boolean(arg_position_index=18, optional=False)
    # axis_label_italic
    @arg_validation_decos.is_boolean(arg_position_index=19, optional=False)
    # variable_name_suffix
    @arg_validation_decos.is_builtin_string(arg_position_index=20, optional=False)
    def __init__(
        self,
        *,
        x_axis_column_name: str,
        tick_max_num: Optional[Union[int, Int]] = None,
        tick_text_font_size: Union[int, Int] = 12,
        tick_text_font_family: Optional[Union[Array[String], List[str]]] = None,
        tick_text_fill_color: Color = Colors.GRAY_666666,
        tick_text_fill_alpha: Union[float, Number] = 1.0,
        tick_text_bold: Union[bool, Boolean] = False,
        tick_text_italic: Union[bool, Boolean] = False,
        line_color: Color = Colors.GRAY_666666,
        line_thickness: Union[int, Int] = 1,
        line_alpha: Union[float, Number] = 1.0,
        is_display_axis_label: Union[bool, Boolean] = True,
        axis_label_position: XAxisLabelPosition = XAxisLabelPosition.OUTER_RIGHT,
        axis_label_font_size: Union[int, Int] = 12,
        axis_label_font_family: Optional[Union[Array[String], List[str]]] = None,
        axis_label_fill_color: Color = Colors.GRAY_666666,
        axis_label_fill_alpha: Union[float, Number] = 1.0,
        axis_label_bold: Union[bool, Boolean] = False,
        axis_label_italic: Union[bool, Boolean] = False,
        variable_name_suffix: str = "",
    ) -> None:
        """
        X-axis settings class.

        Parameters
        ----------
        x_axis_column_name : str
            X-axis column name.
        tick_max_num : Optional[Union[int, Int]], optional
            A tick max display number. Often tick display number
            becomes under this value.
        tick_text_font_size : Union[int, Int], optional
            A tick text font-size setting.
        tick_text_font_family : Optional[Union[Array[String], List[str]]], optional
            A tick text font family setting.
            Each string in an array needs to be a font name (e.g., `Times New Roman`).
        tick_text_fill_color : Color, optional
            A tick text fill-color setting.
        tick_text_fill_alpha : Union[float, Number], optional
            A tick text fill-alpha setting.
        tick_text_bold : Union[bool, Boolean], optional
            A boolean, whether a tick text is a bold style or not.
        tick_text_italic : Union[bool, Boolean], optional
            A boolean, whether a tick text is an italic style or not (normal).
        line_color : Color, optional
            An axis line color setting.
        line_thickness : Union[int, Int], optional
            An axis line thickness (line width) setting.
        line_alpha : Union[float, Number], optional
            An axis line alpha setting.
        is_display_axis_label : Union[bool, Boolean], optional
            A boolean, whether an axis label is visible or not.
        axis_label_position : XAxisLabelPosition, optional
            An axis label position setting.
        axis_label_font_size : Union[int, Int], optional
            An axis label font size setting.
        axis_label_font_family : Optional[Union[Array[String], List[str]]], optional
            An axis label font family setting.
        axis_label_fill_color : Color, optional
            An axis label fill-color setting.
        axis_label_fill_alpha : Union[float, Number], optional
            An axis label fill-alpha setting.
        axis_label_bold : Union[bool, Boolean], optional
            A boolean, whether an axis label is a bold style or not.
        axis_label_italic : Union[bool, Boolean], optional
            A boolean, whether an axis label is an italic style or not (normal).
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        self._set_initial_x_axis_column_name(
            x_axis_column_name=x_axis_column_name,
        )
        self._set_initial_tick_max_num(
            tick_max_num=tick_max_num,
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
        self._set_initial_x_axis_label_position(
            x_axis_label_position=axis_label_position,
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

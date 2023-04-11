"""Class implementation for the x-axis settings.
"""

from typing import Optional, Union, List

from apysc._type.string import String
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.array import Array
from apysc._type.boolean import Boolean
from apysc._chart.x_axis_label_position import XAxisLabelPosition
from apysc._chart.x_axis_column_name_mixin import XAxisColumnNameMixIn
from apysc._chart.tick_culling_max_mixin import TickCullingMaxMixIn


class XAxisSettings(
    XAxisColumnNameMixIn,
    TickCullingMaxMixIn,
):
    def __init__(
        self,
        *,
        x_axis_column_name: Union[str, String],
        tick_culling_max: Optional[Union[int, Int]] = None,
        tick_text_font_size: Union[int, Int] = 12,
        tick_text_font_family: Optional[Union[Array[String], List[str]]] = None,
        tick_text_fill_color: Union[str, String] = "#666666",
        tick_text_fill_alpha: Union[float, Number] = 1.0,
        tick_text_bold: Union[bool, Boolean] = False,
        tick_text_italic: Union[bool, Boolean] = False,
        line_color: Union[str, String] = "#666666",
        line_thickness: Union[int, Int] = 1,
        line_alpha: Union[float, Number] = 1.0,
        is_display_axis_label: Union[bool, Boolean] = True,
        axis_label_position: XAxisLabelPosition = XAxisLabelPosition.OUTER_RIGHT,
        axis_label_font_size: Union[int, Int] = 12,
        axis_label_font_family: Optional[Union[Array[String], List[str]]] = None,
        axis_label_fill_color: Union[str, String] = "#666666",
        axis_label_fill_alpha: Union[float, Number] = 1.0,
        axis_label_bold: Union[bool, Boolean] = False,
        axis_label_italic: Union[bool, Boolean] = False,
        variable_name_suffix: str = "",
    ) -> None:
        """
        X-axis settings class.

        Parameters
        ----------
        x_axis_column_name : Union[str, String]
            X-axis column name.
        tick_culling_max : Optional[Union[int, Int]], optional
            A tick max display number. Often tick display number
            becomes under this value.
        tick_text_font_size : Union[int, Int], optional
            A tick text font-size setting.
        tick_text_font_family : Optional[Union[Array[String], List[str]]], optional
            A tick text font family setting.
            Each string in an array needs to be a font name (e.g., `Times New Roman`).
        tick_text_fill_color : Union[str, String], optional
            A tick text fill color setting.
        tick_text_fill_alpha : Union[float, Number], optional
            A tick text fill alpha setting.
        tick_text_bold : Union[bool, Boolean], optional
            A boolean, whether a tick text is bold style or not.
        tick_text_italic : Union[bool, Boolean], optional
            A boolean, whether a tick text is an italic style or not (normal).
        line_color : Union[str, String], optional
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
        axis_label_fill_color : Union[str, String], optional
            An axis label fill color setting.
        axis_label_fill_alpha : Union[float, Number], optional
            An axis label fill alpha setting.
        axis_label_bold : Union[bool, Boolean], optional
            A boolean, whether an axis label is bold style or not.
        axis_label_italic : Union[bool, Boolean], optional
            A boolean, whether an axis label is an italic style or not (normal).
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        self._set_initial_x_axis_column_name(
            x_axis_column_name=x_axis_column_name,
            variable_name_suffix=variable_name_suffix,
        )
        self._set_initial_tick_culling_max(
            tick_culling_max=tick_culling_max,
            variable_name_suffix=variable_name_suffix,
        )

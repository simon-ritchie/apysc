# mypy: disable-error-code=assignment

"""Class implementation for the vertical bar chart.
"""

from typing import Dict
from typing import List
from typing import Union

from apysc._chart.add_background_mixin import AddBackgroundMixIn
from apysc._chart.add_border_mixin import AddBorderMixIn
from apysc._chart.background_container_mixin import BackgroundContainerMixIn
from apysc._chart.border_container_mixin import BorderContainerMixIn
from apysc._chart.chart_container_mixin import ChartContainerMixIn
from apysc._chart.create_single_column_y_axis_mixin import CreateSingleColumnYAxisMixIn
from apysc._chart.initialize_each_container_mixin import InitializeEachContainerMixIn
from apysc._chart.overall_container_mixin import OverallContainerMixIn
from apysc._chart.set_initial_background_fill_alpha_mixin import (
    SetInitialBackgroundFillAlphaMixIn,
)
from apysc._chart.set_initial_background_fill_color_mixin import (
    SetInitialBackgroundFillColorMixIn,
)
from apysc._chart.set_initial_border_alpha_mixin import SetInitialBorderAlphaMixIn
from apysc._chart.set_initial_border_color_mixin import SetInitialBorderColorMixIn
from apysc._chart.set_initial_border_thickness_mixin import (
    SetInitialBorderThicknessMixIn,
)
from apysc._chart.set_initial_height_mixin import SetInitialHeightMixIn
from apysc._chart.set_initial_horizontal_padding_mixin import (
    SetInitialHorizontalPaddingMixIn,
)
from apysc._chart.set_initial_matrix_data_mixin import SetInitialMatrixDataMixIn
from apysc._chart.set_initial_overall_container_coordinates_mixin import (
    SetInitialOverallContainerCoordinatesMixIn,
)
from apysc._chart.set_initial_vertical_padding_mixin import (
    SetInitialVerticalPaddingMixIn,
)
from apysc._chart.set_initial_width_mixin import SetInitialWidthMixIn
from apysc._chart.set_initial_x_mixin import SetInitialXMixIn
from apysc._chart.set_initial_y_mixin import SetInitialYMixIn
from apysc._chart.x_axis_container_mixin import XAxisContainerMixIn
from apysc._chart.x_axis_settings import XAxisSettings
from apysc._chart.y_axis_container_mixin import YAxisContainerMixIn
from apysc._chart.y_axis_single_column_settings import YAxisSingleColumnSettings
from apysc._color.color import Color
from apysc._color.colorless import COLORLESS
from apysc._color.colors import Colors
from apysc._color.copy_color_if_default_value_specified_mixin import (
    CopyColorIfDefaultValueSpecifiedMixIn,
)
from apysc._type.array import Array
from apysc._type.dictionary import Dictionary
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn

_DataType = Union[
    Array[Dictionary[String, Union[Int, Number, String]]],
    List[Dict[str, Union[int, float, str]]],
]


class VerticalBarChart(
    VariableNameSuffixMixIn,
    SetInitialMatrixDataMixIn,
    SetInitialXMixIn,
    SetInitialYMixIn,
    SetInitialWidthMixIn,
    SetInitialHeightMixIn,
    SetInitialBackgroundFillColorMixIn,
    SetInitialBackgroundFillAlphaMixIn,
    SetInitialBorderColorMixIn,
    SetInitialBorderAlphaMixIn,
    SetInitialBorderThicknessMixIn,
    SetInitialVerticalPaddingMixIn,
    SetInitialHorizontalPaddingMixIn,
    OverallContainerMixIn,
    BackgroundContainerMixIn,
    ChartContainerMixIn,
    XAxisContainerMixIn,
    YAxisContainerMixIn,
    BorderContainerMixIn,
    InitializeEachContainerMixIn,
    AddBackgroundMixIn,
    AddBorderMixIn,
    SetInitialOverallContainerCoordinatesMixIn,
    CreateSingleColumnYAxisMixIn,
    CopyColorIfDefaultValueSpecifiedMixIn,
):
    """
    The class for the vertical bar chart.
    """

    _x_axis_settings: XAxisSettings
    _y_axis_settings: YAxisSingleColumnSettings

    def __init__(
        self,
        *,
        data: _DataType,
        x_axis_settings: XAxisSettings,
        y_axis_settings: YAxisSingleColumnSettings,
        x: Union[float, Number] = 0,
        y: Union[float, Number] = 0,
        width: Union[int, Int] = 640,
        height: Union[int, Int] = 395,
        background_fill_color: Color = Colors.WHITE_FFFFFF,
        background_fill_alpha: Union[float, Number] = 1.0,
        border_color: Color = COLORLESS,
        border_alpha: Union[float, Number] = 1.0,
        border_thickness: Union[int, Int] = 1,
        vertical_padding: Union[int, Int] = 10,
        horizontal_padding: Union[int, Int] = 10,
        variable_name_suffix: str = "",
    ) -> None:
        """
        Create a vertical bar chart instance.

        Parameters
        ----------
        data : Union[Array[Dictionary[String, Union[Int, Number, String]]], List[Dict[str, Union[int, float, str]]]]  # noqa
            A data array, which contains a 1-dimensional string key dictionary.
            A list of dictionaries or an `ap.Array` of `ap.Dictionary` values
            are acceptable.
            E.g., `[{"column_name_1": 10, "column_name_2"}]`
        x_axis_settings : XAxisSettings
            An x-axis setting.
        y_axis_settings : YAxisSingleColumnSettings
            A y-axis setting.
        x : Union[Number]
            A chart's x-coordinate.
        y : Union[float, Number]
            A chart's y-coordinate.
        width : Union[int, Int], default 640
            A chart's width.
        height : Union[int, Int], default 395
            A chart's height.
        background_fill_color : Color, default Colors.WHITE_FFFFFF
            A chart's background fill-color.
        background_fill_alpha : Union[float, Number], default 1.0
            A chart's background fill-alpha.
        border_color : Color, default COLORLESS
            A chart's border color.
        border_alpha : Union[float, Number], default 1.0
            A chart's border alpha.
        border_thickness : Union[int, Int], default 1
            A chart's border thickness.
        vertical_padding : Union[int, Int], default 10
            A chart's vertical padding between borders and contents.
        horizontal_padding : Union[int, Int], default 10
            A chart's horizontal padding between borders and contents.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        self._variable_name_suffix = variable_name_suffix
        self._set_initial_matrix_data(
            data=data, variable_name_suffix=variable_name_suffix
        )
        self._x_axis_settings = x_axis_settings
        self._y_axis_settings = y_axis_settings
        self._set_initial_x(x=x, variable_name_suffix=variable_name_suffix)
        self._set_initial_y(y=y, variable_name_suffix=variable_name_suffix)
        self._set_initial_width(width=width, variable_name_suffix=variable_name_suffix)
        self._set_initial_height(
            height=height, variable_name_suffix=variable_name_suffix
        )
        background_fill_color = self._copy_color_if_default_value_specified(
            color=background_fill_color,
            default_color=Colors.WHITE_FFFFFF,
        )
        self._set_initial_background_fill_color(
            background_fill_color=background_fill_color,
        )
        self._set_initial_background_fill_alpha(
            background_fill_alpha=background_fill_alpha,
            variable_name_suffix=variable_name_suffix,
        )
        self._set_initial_border_color(border_color=border_color)
        self._set_initial_border_alpha(
            border_alpha=border_alpha, variable_name_suffix=variable_name_suffix
        )
        self._set_initial_border_thickness(
            border_thickness=border_thickness, variable_name_suffix=variable_name_suffix
        )
        self._set_initial_vertical_padding(
            vertical_padding=vertical_padding, variable_name_suffix=variable_name_suffix
        )
        self._set_initial_horizontal_padding(
            horizontal_padding=horizontal_padding,
            variable_name_suffix=variable_name_suffix,
        )
        self._initialize_each_container(variable_name_suffix=variable_name_suffix)
        self._add_background(
            background_container=self._background_container,
            width=self._width,
            height=self._height,
            background_fill_color=self._background_fill_color,
            background_fill_alpha=self._background_fill_alpha,
            variable_name_suffix=variable_name_suffix,
        )
        self._add_border(
            border_container=self._border_container,
            width=self._width,
            height=self._height,
            border_color=self._border_color,
            border_alpha=self._border_alpha,
            border_thickness=self._border_thickness,
            variable_name_suffix=variable_name_suffix,
        )
        self._set_initial_overall_container_coordinates(
            overall_container=self._overall_container,
            x=self._x,
            y=self._y,
        )
        self._create_y_axis(
            data=self._matrix_data,
            y_axis_container=self._y_axis_container,
            chart_height=self._height,
            x_axis_settings=self._x_axis_settings,
            y_axis_settings=self._y_axis_settings,
            vertical_padding=self._vertical_padding,
            horizontal_padding=self._horizontal_padding,
            variable_name_suffix=variable_name_suffix,
        )

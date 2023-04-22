"""Class implementation for the vertical bar chart.
"""

from typing import Union, List, Dict

from apysc._chart.x_axis_settings import XAxisSettings
from apysc._chart.y_axis_single_column_settings import YAxisSingleColumnSettings
from apysc._display.sprite import Sprite
from apysc._type.array import Array
from apysc._type.dictionary import Dictionary
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._chart.set_initial_width_mixin import SetInitialWidthMixIn

_DataType = Union[Array[Dictionary[String, Union[Int, Number, String]]], List[Dict[str, Union[int, float, str]]]]


class VerticalBarChart(
    VariableNameSuffixMixIn,
    SetInitialWidthMixIn,
):

    _container: Sprite
    _data: _DataType
    _x_axis_settings: XAxisSettings
    _y_axis_settings: YAxisSingleColumnSettings
    _height: Union[int, Int]
    _background_color: Union[str, String]

    def __init__(
        self,
        *,
        data: _DataType,
        x_axis_settings: XAxisSettings,
        y_axis_settings: YAxisSingleColumnSettings,
        width: Union[int, Int] = 640,
        height: Union[int, Int] = 395,
        background_color: Union[str, String] = "#ffffff",
        variable_name_suffix: str = "",
    ) -> None:
        """
        Create a vertical bar chart instance.

        Parameters
        ----------
        data : Union[Array[Dictionary[String, Union[Int, Number, String]]], List[Dict[str, Union[int, float, str]]]]  # noqa
            A data array, which contains 1-dimentional string key dictionary.
            A list of dictionary or an `ap.Array` of `ap.Dictionary` values
            are acceptable.
            E.g., `[{"column_name_1": 10, "column_name_2"}]`
        x_axis_settings : XAxisSettings
            An x-axis settings.
        y_axis_settings : YAxisSingleColumnSettings
            A y-axis settings.
        width : Union[int, Int], default 640
            A chart's width.
        height : Union[int, Int], default 395
            A chart's height.
        background_color : Union[str, String]
            A chart's background color.
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        self._data = data
        self._x_axis_settings = x_axis_settings
        self._y_axis_settings = y_axis_settings
        self._set_initial_width(width=width, variable_name_suffix=variable_name_suffix)
        self._height = height
        self._background_color = background_color
        self._variable_name_suffix = variable_name_suffix
        self._container = Sprite(variable_name_suffix=variable_name_suffix)

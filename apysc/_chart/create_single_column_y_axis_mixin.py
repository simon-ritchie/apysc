"""The mix-in class implementation for the single column's
`_create_y_axis` method.
"""

from typing import Optional
from typing import Union
from typing import cast

from typing_extensions import final

from apysc._chart import chart_const
from apysc._chart.x_axis_settings import XAxisSettings
from apysc._chart.y_axis_single_column_settings import YAxisSingleColumnSettings
from apysc._display.sprite import Sprite
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.array import Array
from apysc._type.boolean import Boolean
from apysc._type.dictionary import Dictionary
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String


class CreateSingleColumnYAxisMixIn:

    _in_value_y_min: Number
    _in_value_y_max: Number
    _y_axis_height: Int
    _y_axis_ticks_num: Int
    _y_axis_text_container: Sprite
    _y_axis_ticks_y_coordinates: Array[Number]

    @final
    @add_debug_info_setting(module_name=__name__)
    def _create_y_axis(
        self,
        *,
        data: Array[Dictionary[str, Union[Int, Number, String]]],
        y_axis_container: Sprite,
        chart_height: Int,
        x_axis_settings: XAxisSettings,
        y_axis_settings: YAxisSingleColumnSettings,
        vertical_padding: Int,
        horizontal_padding: Int,
        variable_name_suffix: str,
    ) -> None:
        """
        Create a y-axis instance.

        Parameters
        ----------
        data : Array[Dictionary[str, Union[Int, Number, String]]],
            A data array, which contains a 1-dimensional string key dictionary.
        y_axis_container : Sprite
            A y-axis container instance.
        chart_height : Int
            A chart height.
        x_axis_settings : XAxisSettings
            An x-axis settings instance.
        y_axis_settings : YAxisSingleColumnSettings
            A y-axis settings instance.
        vertical_padding : Int
            A chart's vertical padding between borders and contents.
        horizontal_padding : Int
            A chart's horizontal padding between borders and contents.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        self._in_value_y_min = _calculate_y_min_from_data(
            data=data,
            y_axis_column_name=y_axis_settings._y_axis_column_name,
            variable_name_suffix=variable_name_suffix,
        )
        self._in_value_y_max = _calculate_y_max_from_data(
            data=data,
            y_axis_column_name=y_axis_settings._y_axis_column_name,
            variable_name_suffix=variable_name_suffix,
        )
        self._y_axis_height = _calculate_y_axis_height(
            chart_height=chart_height,
            vertical_padding=vertical_padding,
            tick_text_font_size=x_axis_settings._tick_text_font_size,
            axis_label_font_size=x_axis_settings._axis_label_font_size,
            is_display_axis_label=x_axis_settings._is_display_axis_label,
            variable_name_suffix=variable_name_suffix,
        )
        self._y_axis_ticks_num = _calculate_y_axis_ticks_num(
            y_axis_height=self._y_axis_height,
            tick_max_num=y_axis_settings._tick_max_num,
            tick_text_font_size=y_axis_settings._tick_text_font_size,
            variable_name_suffix=variable_name_suffix,
        )
        self._y_axis_ticks_y_coordinates = _calculate_y_axis_ticks_y_coordinates(
            vertical_padding=vertical_padding,
            y_axis_height=self._y_axis_height,
            y_axis_ticks_num=self._y_axis_ticks_num,
            variable_name_suffix=variable_name_suffix,
        )


def _calculate_y_axis_ticks_y_coordinates(
    *,
    vertical_padding: Int,
    y_axis_height: Int,
    y_axis_ticks_num: Int,
    variable_name_suffix: str,
) -> Array[Number]:
    """
    Calculate a y-axis ticks' coordinates.

    Parameters
    ----------
    vertical_padding : Int
        A chart's vertical padding between border and contents.
    y_axis_height : Int
        An axis height.
    y_axis_ticks_num : Int
        Axis tick number.
    variable_name_suffix : str
        A JavaScript variable name suffix string.
        This setting is sometimes useful for JavaScript debugging.

    Returns
    -------
    y_axis_ticks_y_coordinates : Array[Number]
        A y-axis ticks' coordinates. The first index becomes the axis
        starting coordinate (bottom position of a y-axis).
    """
    import apysc as ap

    y_axis_ticks_y_coordinates: Array[Number] = Array(
        [], variable_name_suffix=variable_name_suffix
    )
    y_start_coordinate: Int = Int(
        vertical_padding,
        variable_name_suffix=variable_name_suffix,
    )
    range_arr: Array[Int] = ap.range(y_axis_ticks_num)
    i: Int
    interval: Number = y_axis_height / (y_axis_ticks_num - 1)
    with ap.For(range_arr) as i:
        y_coordinate: Number = y_start_coordinate + i * interval
        y_axis_ticks_y_coordinates.append(y_coordinate)
    y_axis_ticks_y_coordinates.reverse()
    return y_axis_ticks_y_coordinates


def _calculate_y_axis_ticks_num(
    *,
    y_axis_height: Int,
    tick_max_num: Optional[Int],
    tick_text_font_size: Int,
    variable_name_suffix: str,
) -> Int:
    """
    Calculate a y-axis ticks number.

    Parameters
    ----------
    y_axis_height : Int
        A y-axis height.
    tick_max_num : Optional[Int]
        A ticks maximum number.
    tick_text_font_size : Int
        A tick text font size.
    variable_name_suffix : str, optional
        A JavaScript variable name suffix string.
        This setting is sometimes useful for JavaScript debugging.

    Returns
    -------
    y_axis_ticks_num : Int
        A y-axis ticks number.
    """
    import apysc as ap

    interval: Int = tick_text_font_size * 3
    y_axis_ticks_num: Int = y_axis_height // interval
    y_axis_ticks_num += 1
    if tick_max_num is not None:
        min_arr: ap.Array[Int] = ap.Array(
            [y_axis_ticks_num, tick_max_num],
            variable_name_suffix=variable_name_suffix,
        )
        y_axis_ticks_num = Int(
            ap.Math.min(min_arr), variable_name_suffix=variable_name_suffix
        )
    return y_axis_ticks_num


def _calculate_y_axis_height(
    *,
    chart_height: Int,
    vertical_padding: Int,
    tick_text_font_size: Int,
    axis_label_font_size: Int,
    is_display_axis_label: Boolean,
    variable_name_suffix: str,
) -> Int:
    """
    Calculate a y-axis height.

    Parameters
    ----------
    chart_height : Int
        A chart height.
    vertical_padding : Int
        A chart's vertical padding between borders and contents.
    tick_text_font_size : Int
        A tick text font size.
    axis_label_font_size : Int
        An axis label font size.
    is_display_axis_label : Boolean
        A boolean, whether an axis label is visible or not.
    variable_name_suffix : str, optional
        A JavaScript variable name suffix string.
        This setting is sometimes useful for JavaScript debugging.

    Returns
    -------
    y_axis_height : Int
        A calculate height.
    """
    import apysc as ap

    y_axis_height: Int = Int(chart_height, variable_name_suffix=variable_name_suffix)
    y_axis_height -= vertical_padding * 2
    y_axis_height -= axis_label_font_size
    y_axis_height -= chart_const.SMALL_PADDING
    y_axis_height -= chart_const.TICK_SIZE
    with ap.If(is_display_axis_label):
        y_axis_height -= chart_const.SMALL_PADDING * 2
        y_axis_height -= tick_text_font_size
    return y_axis_height


def _calculate_y_max_from_data(
    *,
    data: Array[Dictionary[str, Union[Int, Number, String]]],
    y_axis_column_name: str,
    variable_name_suffix: str,
) -> Number:
    """
    Get a y-axis maximum value from a specified data.

    Parameters
    ----------
    data : Array[Dictionary[str, Union[Int, Number, String]]]
        A data array, which contains a 1-dimensional string key dictionary.
    y_axis_column_name : str
        A y-axis column name.
    variable_name_suffix : str
        A JavaScript variable name suffix string.
        This setting is sometimes useful for JavaScript debugging.

    Returns
    -------
    y_max : Number
        A y-axis maximum value.
    """
    import apysc as ap

    values: Array[Union[Int, Number]] = _extract_column_values_from_data(
        data=data,
        column_name=y_axis_column_name,
        variable_name_suffix=variable_name_suffix,
    )
    y_max: Number = ap.Math.max(values)
    return y_max


def _calculate_y_min_from_data(
    *,
    data: Array[Dictionary[str, Union[Int, Number, String]]],
    y_axis_column_name: str,
    variable_name_suffix: str,
) -> Number:
    """
    Get a y-axis minimum value from specified data.

    Parameters
    ----------
    data : Array[Dictionary[str, Union[Int, Number, String]]]
        A data array, which contains a 1-dimensional string key dictionary.
    y_axis_column_name : str
        A y-axis column name.
    variable_name_suffix : str, optional
        A JavaScript variable name suffix string.
        This setting is sometimes useful for JavaScript debugging.

    Returns
    -------
    y_min : Number
        A y-axis minimum value.
    """
    import apysc as ap

    values: Array[Union[Int, Number]] = _extract_column_values_from_data(
        data=data,
        column_name=y_axis_column_name,
        variable_name_suffix=variable_name_suffix,
    )
    y_min: Number = ap.Math.min(values)
    return y_min


def _extract_column_values_from_data(
    *,
    data: Array[Dictionary[str, Union[Int, Number, String]]],
    column_name: str,
    variable_name_suffix: str,
) -> Array[Union[Int, Number]]:
    """
    Get a specified column values array from a specified data.

    Parameters
    ----------
    data : Array[Dictionary[str, Union[Int, Number, String]]]
        A data array, which contains a 1-dimensional string key dictionary.
    column_name : str
        A y-axis column name.
    variable_name_suffix : str, optional
        A JavaScript variable name suffix string.
        This setting is sometimes useful for JavaScript debugging.

    Returns
    -------
    values : Array[Union[Int, Number]]
        A values array.
    """
    import apysc as ap

    values: Array[Union[Int, Number]] = Array(
        [], variable_name_suffix=variable_name_suffix
    )
    i: Int
    with ap.For(data) as i:
        dict_value: Dictionary[str, Union[Int, Number]] = cast(
            Dictionary[str, Union[Int, Number]], data[i]
        )
        values.append(dict_value[column_name])
    return values

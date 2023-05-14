"""The mix-in class implementation for the single column's
`_create_y_axis` method.
"""

from typing import Union

from typing_extensions import final

from apysc._chart.y_axis_single_column_settings import YAxisSingleColumnSettings
from apysc._display.sprite import Sprite
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.array import Array
from apysc._type.dictionary import Dictionary
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String


class CreateSingleColumnYAxisMixIn:

    _y_axis_text_container: Sprite

    @final
    @add_debug_info_setting(module_name=__name__)
    def _create_y_axis(
        self,
        *,
        data: Array[Dictionary[str, Union[Int, Number, String]]],
        y_axis_container: Sprite,
        y_axis_settings: YAxisSingleColumnSettings,
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
        y_axis_settings : YAxisSingleColumnSettings
            A y-axis settings instance.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        y_min: Number = self._get_y_min(
            data=data,
            y_axis_column_name=y_axis_settings._y_axis_column_name,
            variable_name_suffix=variable_name_suffix,
        )
        pass

    def _get_y_min(
        self,
        *,
        data: Array[Dictionary[str, Union[Int, Number, String]]],
        y_axis_column_name: str,
        variable_name_suffix: str,
    ) -> Number:
        """
        Get a y-axis minimum value.

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

        values: Array[Union[Int, Number]] = Array(
            [], variable_name_suffix=variable_name_suffix
        )
        i: Int
        with ap.For(data) as i:
            dict_value: Dictionary[str, Union[Int, Number]] = data[i]  # type: ignore
            values.append(dict_value[y_axis_column_name])
        y_min: Number = ap.Math.min(values)
        return y_min

"""The mix-in class implementation for the `_create_y_axis` method.
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


class CreateYAxisMixIn:
    @final
    @add_debug_info_setting(module_name=__name__)
    def _create_y_axis(
        self,
        *,
        data: Array[Dictionary[str, Union[Int, Number, String]]],
        y_axis_container: Sprite,
        y_axis_settings: YAxisSingleColumnSettings,
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
        """

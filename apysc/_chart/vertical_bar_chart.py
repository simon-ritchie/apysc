"""Class implementation for the vertical bar chart.
"""

from typing import Union

from apysc._display.sprite import Sprite
from apysc._type.array import Array
from apysc._type.dictionary import Dictionary
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String
from apysc._chart.x_axis_settings import XAxisSettings


class VerticalBarChart:

    _container: Sprite

    def __init__(
        self,
        *,
        data: Array[Dictionary[String, Union[Int, Number, String]]],
        x_axis_settings: XAxisSettings,
    ) -> None:
        pass

"""The mix-in class implementation for the `_add_border` method.
"""

from typing_extensions import final

from apysc._color.color import Color
from apysc._display.rectangle import Rectangle
from apysc._display.sprite import Sprite
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.number import Number


class AddBorderMixIn:
    _border: Rectangle

    @final
    @add_debug_info_setting(module_name=__name__)
    def _add_border(
        self,
        *,
        border_container: Sprite,
        width: Int,
        height: Int,
        border_color: Color,
        border_alpha: Number,
        border_thickness: Int,
        variable_name_suffix: str,
    ) -> None:
        """
        Add a border to a container.

        Parameters
        ----------
        border_container : Sprite
            A border container instance.
        width : Int
            A border width.
        height : Int
            A border height.
        border_color : Color
            A border color.
        border_alpha : Number
            A border alpha.
        border_thickness : Int
            A border thickness (line width).
        variable_name_suffix : str
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        self._border = Rectangle(
            x=0,
            y=0,
            width=width,
            height=height,
            line_color=border_color,
            line_alpha=border_alpha,
            line_thickness=border_thickness,
            variable_name_suffix=variable_name_suffix,
        )
        border_container.add_child(self._border)

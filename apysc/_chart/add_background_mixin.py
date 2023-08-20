"""The mix-in class implementation for the `_add_background` method.
"""

from typing_extensions import final

from apysc._color.color import Color
from apysc._display.rectangle import Rectangle
from apysc._display.sprite import Sprite
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._validation import arg_validation_decos


class AddBackgroundMixIn:
    _background: Rectangle

    @final
    @arg_validation_decos.is_display_object_container(
        arg_position_index=1, optional=False
    )
    @arg_validation_decos.is_apysc_integer(arg_position_index=2)
    @arg_validation_decos.is_apysc_integer(arg_position_index=3)
    @arg_validation_decos.is_color(arg_position_index=4, optional=False)
    @arg_validation_decos.is_apysc_num(arg_position_index=5)
    @add_debug_info_setting(module_name=__name__)
    def _add_background(
        self,
        *,
        background_container: Sprite,
        width: Int,
        height: Int,
        background_fill_color: Color,
        background_fill_alpha: Number,
        variable_name_suffix: str,
    ) -> None:
        """
        Add a background to a container.

        Parameters
        ----------
        background_container : Sprite
            A background container instance.
        width : Int
            A background width.
        height : Int
            A background height.
        background_fill_color : Color
            A background fill-color.
        background_fill_alpha : Number
            A background fill-alpha.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        self._background = Rectangle(
            x=0,
            y=0,
            width=width,
            height=height,
            fill_color=background_fill_color,
            fill_alpha=background_fill_alpha,
            variable_name_suffix=variable_name_suffix,
        )
        background_container.add_child(self._background)

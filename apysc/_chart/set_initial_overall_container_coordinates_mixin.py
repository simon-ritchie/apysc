"""Mix-in class implementation for the `_set_initial_overall_container_coordinates`
method.
"""

from typing_extensions import final

from apysc._display.sprite import Sprite
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number
from apysc._validation import arg_validation_decos


class SetInitialOverallContainerCoordinatesMixIn:
    @final
    @arg_validation_decos.is_display_object_container(
        arg_position_index=1,
        optional=False,
    )
    @arg_validation_decos.is_num(arg_position_index=2, optional=False)
    @arg_validation_decos.is_num(arg_position_index=3, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_overall_container_coordinates(
        self,
        *,
        overall_container: Sprite,
        x: Number,
        y: Number,
    ) -> None:
        """
        Set initial overall container coordinates.

        Parameters
        ----------
        overall_container : Sprite
            An overall container.
        x : Number
            X-coordinate.
        y : Number
            Y-coordinate.
        """
        overall_container.x = x
        overall_container.y = y

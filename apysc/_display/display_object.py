"""Implementations for DisplayObject class.
"""

from apysc._animation.animation_parallel_mixin import AnimationParallelMixIn
from apysc._display.css_interface import CssInterface
from apysc._display.parent_mixin import ParentMixIn
from apysc._display.visible_mixin import VisibleMixIn
from apysc._event.custom_event_mixin import CustomEventMixIn
from apysc._event.mouse_event_mixins import MouseEventMixIns
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos


class DisplayObject(
    ParentMixIn,
    MouseEventMixIns,
    VisibleMixIn,
    CustomEventMixIn,
    CssInterface,
    AnimationParallelMixIn,
):
    """
    Display object (base) class for the common interfaces.

    References
    ----------
    - DisplayObject
        - https://simon-ritchie.github.io/apysc/en/display_object.html
    """

    @arg_validation_decos.not_empty_string(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def __init__(self, *, variable_name: str) -> None:
        """
        Display object (base) class for the common interfaces.

        Parameters
        ----------
        variable_name : str
            Variable name of this instance. A js expression
            uses this setting.

        References
        ----------
        - DisplayObject
            - https://simon-ritchie.github.io/apysc/en/display_object.html
        """
        self._variable_name = variable_name

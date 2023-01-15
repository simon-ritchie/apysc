"""Implementations for DisplayObject class.
"""

from typing import TYPE_CHECKING

from typing_extensions import final

from apysc._animation.animation_parallel_mixin import AnimationParallelMixIn
from apysc._display.css_mixin import CssMixIn
from apysc._display.parent_mixin import ParentMixIn
from apysc._display.visible_mixin import VisibleMixIn
from apysc._display.x_interface import XInterface
from apysc._display.y_interface import YInterface
from apysc._event.custom_event_mixin import CustomEventMixIn
from apysc._event.mouse_event_mixins import MouseEventMixIns
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos

if TYPE_CHECKING:
    from apysc._display.stage import Stage


class DisplayObject(
    XInterface,
    YInterface,
    ParentMixIn,
    MouseEventMixIns,
    VisibleMixIn,
    CustomEventMixIn,
    CssMixIn,
    AnimationParallelMixIn,
):
    """
    Display object (base) class for the common interfaces.

    References
    ----------
    - DisplayObject
        - https://simon-ritchie.github.io/apysc/en/display_object.html
    """

    stage: "Stage"

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
        import apysc as ap

        stage: ap.Stage = ap.get_stage()
        self.stage: ap.Stage = stage
        self._variable_name = variable_name

    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_overflow_visible_setting(self) -> None:
        """
        Set the `visible` value to the `overflow` CSS property.
        """
        self.set_css(name="overflow", value="visible")

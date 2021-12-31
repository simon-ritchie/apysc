"""Implementations for DisplayObject class.
"""

from typing import TYPE_CHECKING

from apysc._animation.animation_parallel_interface import \
    AnimationParallelInterface
from apysc._display.css_interface import CssInterface
from apysc._display.parent_interface import ParentInterface
from apysc._display.visible_interface import VisibleInterface
from apysc._display.x_interface import XInterface
from apysc._display.y_interface import YInterface
from apysc._event.custom_event_interface import CustomEventInterface
from apysc._event.mouse_event_interfaces import MouseEventInterfaces

if TYPE_CHECKING:
    from apysc._display.stage import Stage


class DisplayObject(
        XInterface, YInterface, ParentInterface, MouseEventInterfaces,
        VisibleInterface, CustomEventInterface, CssInterface,
        AnimationParallelInterface):
    """
    Display object (base) class for the common interfaces.

    References
    ----------
    - DisplayObject document
        - https://simon-ritchie.github.io/apysc/display_object.html
    """

    stage: 'Stage'

    def __init__(self, *, variable_name: str) -> None:
        """
        Display object (base) class for the common interfaces.

        Parameters
        ----------
        variable_name : str
            Variable name of this instance. This will be used to
            js expression.

        References
        ----------
        - DisplayObject document
            - https://simon-ritchie.github.io/apysc/display_object.html
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=DisplayObject):
            from apysc._validation import string_validation
            stage: ap.Stage = ap.get_stage()
            self.stage: ap.Stage = stage
            self._variable_name = variable_name
            string_validation.validate_not_empty_string(string=variable_name)

    def _set_overflow_visible_setting(self) -> None:
        """
        Set the `visible` value to the `overflow` CSS property.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._set_overflow_visible_setting, locals_=locals(),
                module_name=__name__, class_=DisplayObject):
            self.set_css(name='overflow', value='visible')

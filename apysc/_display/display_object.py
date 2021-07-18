"""Implementations for DisplayObject class.
"""

from typing import Any
from typing import Type

from apysc._display.css_interface import CssInterface
from apysc._display.parent_interface import ParentInterface
from apysc._display.visible_interface import VisibleInterface
from apysc._display.x_interface import XInterface
from apysc._display.y_interface import YInterface
from apysc._event.custom_event_interface import CustomEventInterface
from apysc._event.mouse_event_interfaces import MouseEventInterfaces


class DisplayObject(
        XInterface, YInterface, ParentInterface, MouseEventInterfaces,
        VisibleInterface, CustomEventInterface, CssInterface):

    def __init__(self, stage: Any, variable_name: str) -> None:
        """
        Display object class for common interface.

        Parameters
        ----------
        stage : Stage
            Stage instance to link this object.
        variable_name : str
            Variable name of this instance. This will be used to
            js expression.
        """
        import apysc as ap
        from apysc._validation import display_validation
        from apysc._validation import string_validation
        self._stage_cls: Type[ap.Stage] = ap.Stage
        self.stage: ap.Stage = stage
        display_validation.validate_stage(stage=stage)
        self._variable_name = variable_name
        string_validation.validate_not_empty_string(string=variable_name)

    def _set_overflow_visible_setting(self) -> None:
        """
        Set the `visible` value to the `overflow` CSS property.
        """
        self.set_css(name='overflow', value='visible')

"""Class implementation for mouse wheel event.
"""

from typing import Generic
from typing import TypeVar

from apysc import Int
from apysc.event.event import Event
from apysc.type.variable_name_interface import VariableNameInterface


class MouseWheelEvent(Event):

    def __init__(self) -> None:
        """
        Mouse wheel event class.

        Notes
        -----
        Not supported each SVG elements' mouse wheel event currently, only
        supported document (overall screen) mouse wheel.
        """
        from apysc.expression import var_names
        super(MouseWheelEvent, self).__init__(
            this=None,
            type_name=var_names.MOUSE_WHEEL_EVENT)

    @property
    def this(self) -> None:
        """
        MouseWheelEvent instance isn't supported this property.
        """
        raise Exception(
            'MouseWheelEvent instance isn\'t supported this property.')

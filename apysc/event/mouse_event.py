"""Class implementation for mouse event.
"""

from typing import Generic
from typing import Optional
from typing import TypeVar

from apysc.event.event import Event
from apysc.type.variable_name_interface import VariableNameInterface

T = TypeVar('T', bound=VariableNameInterface)


class MouseEvent(Generic[T], Event):

    _this: T

    def __init__(self, this: T) -> None:
        """
        Mouse event class.

        Parameters
        ----------
        this : VariableNameInterface
            Instance that listening event (e.g., Sprite).
        """
        from apysc.expression import var_names
        super(MouseEvent, self).__init__(
            this=this, type_name=var_names.MOUSE_EVENT)

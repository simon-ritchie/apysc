"""Class implementation for the inheritance of each mouse
event interface.
"""

from apysc._event.click_interface import ClickInterface
from apysc._event.double_click_interface import DoubleClickInterface
from apysc._event.mouse_down_interface import MouseDownInterface
from apysc._event.mouse_move_interface import MouseMoveInterface
from apysc._event.mouse_out_interface import MouseOutInterface
from apysc._event.mouse_over_interface import MouseOverInterface
from apysc._event.mouse_up_interface import MouseUpInterface


class MouseEventInterfaces(
        ClickInterface, DoubleClickInterface, MouseDownInterface,
        MouseUpInterface, MouseOverInterface, MouseOutInterface,
        MouseMoveInterface):
    """Class implementation for the inheritance of each mouse
    event interface.
    """

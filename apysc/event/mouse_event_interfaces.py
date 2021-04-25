"""Class implementation for inheritance of each mouse event interfaces.
"""

from apysc.event.click_interface import ClickInterface
from apysc.event.double_click_interface import DoubleClickInterface
from apysc.event.mouse_down_interface import MouseDownInterface
from apysc.event.mouse_move_interface import MouseMoveInterface
from apysc.event.mouse_out_interface import MouseOutInterface
from apysc.event.mouse_over_interface import MouseOverInterface
from apysc.event.mouse_up_interface import MouseUpInterface


class MouseEventInterfaces(
        ClickInterface, DoubleClickInterface, MouseDownInterface,
        MouseUpInterface, MouseOverInterface, MouseOutInterface,
        MouseMoveInterface):
    """Class implementation for inheritance of each mouse event interfaces.
    """

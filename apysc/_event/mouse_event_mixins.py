"""Class implementation for the inheritance of each mouse
event mix-ins.
"""

from apysc._event.click_mixin import ClickMixIn
from apysc._event.double_click_mixin import DoubleClickMixIn
from apysc._event.mouse_down_mixin import MouseDownMixIn
from apysc._event.mouse_move_mixin import MouseMoveMixIn
from apysc._event.mouse_out_mixin import MouseOutMixIn
from apysc._event.mouse_over_mixin import MouseOverMixIn
from apysc._event.mouse_up_mixin import MouseUpMixIn


class MouseEventMixIns(
    ClickMixIn,
    DoubleClickMixIn,
    MouseDownMixIn,
    MouseUpMixIn,
    MouseOverMixIn,
    MouseOutMixIn,
    MouseMoveMixIn,
):
    """Class implementation for the inheritance of each mouse
    event mix-ins.
    """

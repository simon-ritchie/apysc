"""Definitions for color constants.
"""

from apysc._color.color import Color
from apysc._color.get_colors_members_mixin import GetColorsMenmbersMixIn

_000000: Color = Color("#000000")
_111111: Color = Color("#111111")
_222222: Color = Color("#222222")
_333333: Color = Color("#333333")
_444444: Color = Color("#444444")
_555555: Color = Color("#555555")
_666666: Color = Color("#666666")
_777777: Color = Color("#777777")
_888888: Color = Color("#888888")
_999999: Color = Color("#999999")
_AAAAAA: Color = Color("#aaaaaa")
_BBBBBB: Color = Color("#bbbbbb")
_CCCCCC: Color = Color("#cccccc")
_DDDDDD: Color = Color("#dddddd")
_EEEEEE: Color = Color("#eeeeee")
_FFFFFF: Color = Color("#ffffff")
_FF0000: Color = Color("#ff0000")
_00FF00: Color = Color("#00ffff")
_0000FF: Color = Color("#0000ff")
_FFFF00: Color = Color("#ffff00")
_00FFFF: Color = Color("#00ffff")
_FF00FF: Color = Color("#ff00ff")


class Colors(GetColorsMenmbersMixIn):
    """
    Color constants class.
    """

    BLACK_000000: Color = _000000
    BLACK_111111: Color = _111111
    BLACK_222222: Color = _222222
    GRAY_333333: Color = _333333
    GRAY_444444: Color = _444444
    GRAY_555555: Color = _555555
    GRAY_666666: Color = _666666
    GRAY_777777: Color = _777777
    GRAY_888888: Color = _888888
    GRAY_999999: Color = _999999
    GRAY_AAAAAA: Color = _AAAAAA
    GRAY_BBBBBB: Color = _BBBBBB
    GRAY_CCCCCC: Color = _CCCCCC
    GRAY_DDDDDD: Color = _DDDDDD
    WHITE_EEEEEE: Color = _EEEEEE
    WHITE_FFFFFF: Color = _FFFFFF
    RED_FF0000: Color = _FF0000
    GREEN_00FF00: Color = _00FF00
    BLUE_0000FF: Color = _0000FF
    YELLOW_FFFF00: Color = _FFFF00
    CYAN_00FFFF: Color = _00FFFF
    MAGENTA_FF00FF: Color = _FF00FF

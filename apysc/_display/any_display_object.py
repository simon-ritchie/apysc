"""This module is for the `DisplayObject` subclass implementation
to avoid an abstract method error.
"""

from apysc._display.display_object import DisplayObject
from apysc._display.x_mixin import XMixIn
from apysc._display.y_mixin import YMixIn


class AnyDisplayObject(DisplayObject, XMixIn, YMixIn):
    """This class is for the `DisplayObject` subclass
    implementation to avoid an abstract method error.
    """

    ...

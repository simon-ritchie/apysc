from apysc._display.display_object import DisplayObject
from apysc._display.x_interface import XInterface
from apysc._display.y_interface import YInterface


class AnyDisplayObject(DisplayObject, XInterface, YInterface):
    ...

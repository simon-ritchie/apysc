"""Implementations for Sprite class.
"""

from apyscript.display.display_object import DisplayObject
from apyscript.display.stage import Stage
from apyscript.display.graphics import Graphics


class Sprite(DisplayObject):

    graphics: Graphics

    def __init__(self, stage: Stage) -> None:
        """
        Basic display object that can be parent.

        Parameters
        ----------
        stage : Stage
            Stage instance to link this object.
        """
        super(Sprite, self).__init__(stage=stage)
        self.graphics = Graphics()

    def add_child(self, child: DisplayObject) -> None:
        """
        Add display object child to this object.

        Parameters
        ----------
        child : DisplayObject
            Child object to add.
        """
        super(Sprite, self).add_child(child)

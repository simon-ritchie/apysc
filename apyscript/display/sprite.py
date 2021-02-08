"""Implementations for Sprite class.
"""

from apyscript.display.display_object import DisplayObject
from apyscript.display.stage import Stage
from apyscript.display.graphics import Graphics
from apyscript.type import type_util
from apyscript.html import html_const
from apyscript.expression import expression_file_util


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
        self.graphics = Graphics(parent=self)
        self._append_constructor_expression()

    def _append_constructor_expression(self) -> None:
        """
        Append Sprite constructor expression to current scope.

        Notes
        -----
        Expression not to be added if instance is Sprite subclass.
        """
        is_same_class_instance: bool = type_util.is_same_class_instance(
            cls=Sprite, instance=self)
        if not is_same_class_instance:
            return
        expression: str = (
            f'{html_const.SCRIPT_START_TAG}'
            f'\nsprite = '
            f'\n{html_const.SCRIPT_END_TAG}'
        )
        # expression_file_util.append_expression_to_current_scope(
        #     expression=)

    def add_child(self, child: DisplayObject) -> None:
        """
        Add display object child to this object.

        Parameters
        ----------
        child : DisplayObject
            Child object to add.
        """
        super(Sprite, self).add_child(child)

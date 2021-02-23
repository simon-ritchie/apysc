"""Implementations for Sprite class.
"""

from typing import Optional

from apyscript.display.child_interface import ChildInterface
from apyscript.display.display_object import DisplayObject
from apyscript.display.graphics import Graphics
from apyscript.display.stage import Stage
from apyscript.display.stage import get_stage_variable_name
from apyscript.expression import expression_file_util
from apyscript.expression import expression_variables_util
from apyscript.html import html_const
from apyscript.type import type_util


class Sprite(DisplayObject, ChildInterface):

    graphics: Graphics

    def __init__(
            self, stage: Stage,
            variable_name: Optional[str] = None) -> None:
        """
        Basic display object that can be parent.

        Parameters
        ----------
        stage : Stage
            Stage instance to link this object.
        variable_name : str or None, default None
            Variable name of this instance. This will be used to
            js expression. It is not necessary to specify any
            string except when Sprite subclass will be instantiated.
        """
        if variable_name is None:
            variable_name = expression_variables_util.\
                get_next_variable_name(type_name='sprite')
        self._childs = []
        super(Sprite, self).__init__(
            stage=stage, variable_name=variable_name)
        self._append_constructor_expression()
        self.graphics = Graphics(parent=self)

    def _append_constructor_expression(self) -> bool:
        """
        Append Sprite constructor expression.

        Notes
        -----
        Expression not to be added if instance is Sprite subclass.

        Returns
        -------
        appended : bool
            If expression appended, then True will be set.
        """
        is_same_class_instance: bool = type_util.is_same_class_instance(
            class_=Sprite, instance=self)
        if not is_same_class_instance:
            return False
        stage_variable_name: str = get_stage_variable_name()
        expression: str = (
            f'{html_const.SCRIPT_START_TAG}'
            f'\nvar {self.variable_name} = {stage_variable_name}.group();'
            f'\n{html_const.SCRIPT_END_TAG}'
        )
        expression_file_util.append_expression(
            expression=expression)
        return True

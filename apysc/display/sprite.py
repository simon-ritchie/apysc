"""Implementations for Sprite class.
"""

from typing import Optional

from apysc.display.child_interface import ChildInterface
from apysc.display.display_object import DisplayObject
from apysc.display.graphics import Graphics
from apysc.display.stage import Stage
from apysc.html import html_const
from apysc.type import Array


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
        from apysc.expression import expression_variables_util
        from apysc.expression import var_names

        # Graphics sprite child cound of 1.
        self._js_child_adjust_num = 1

        if variable_name is None:
            variable_name = expression_variables_util.\
                get_next_variable_name(type_name=var_names.SPRITE)
        self._children = Array([])
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
        from apysc.display.stage import get_stage_variable_name
        from apysc.expression import expression_file_util
        from apysc.type import type_util
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

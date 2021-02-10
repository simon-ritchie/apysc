"""Implementations for DisplayObject class.
"""

from typing import List, Type

from apyscript.display.variable_name_interface import VariableNameInterface


class DisplayObject(VariableNameInterface):

    def __init__(self, stage, variable_name: str) -> None:
        """
        Display object class for common interface.

        Parameters
        ----------
        stage : Stage
            Stage instance to link this object.
        variable_name : str
            Variable name of this instance. This will be used to
            js expression.
        """
        from apyscript.display.stage import Stage
        self._stage_cls: Type[Stage] = Stage
        self.stage: Stage = stage
        self._variable_name = variable_name

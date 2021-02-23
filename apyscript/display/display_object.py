"""Implementations for DisplayObject class.
"""

from typing import Any
from typing import Type

from apyscript.display.parent_interface import ParentInterface
from apyscript.display.x_interface import XInterface
from apyscript.display.y_interface import YInterface
from apyscript.validation import display_validation
from apyscript.validation import string_validation


class DisplayObject(
        XInterface, YInterface, ParentInterface):

    def __init__(self, stage: Any, variable_name: str) -> None:
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
        display_validation.validate_stage(stage=stage)
        self._variable_name = variable_name
        string_validation.validate_not_empty_string(string=variable_name)

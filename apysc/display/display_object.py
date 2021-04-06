"""Implementations for DisplayObject class.
"""

from typing import Any
from typing import Type

from apysc.display.parent_interface import ParentInterface
from apysc.display.x_interface import XInterface
from apysc.display.y_interface import YInterface


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
        from apysc import Stage
        from apysc.validation import display_validation
        from apysc.validation import string_validation
        self._stage_cls: Type[Stage] = Stage
        self.stage: Stage = stage
        display_validation.validate_stage(stage=stage)
        self._variable_name = variable_name
        string_validation.validate_not_empty_string(string=variable_name)

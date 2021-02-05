# -*- coding: future_annotations -*-

"""Implementations for DisplayObject class.
"""

from typing import Type


class DisplayObject:

    def __init__(self, stage) -> None:
        """
        Display object class for common interface.

        Parameters
        ----------
        stage : Stage
            Stage instance to link this object.
        """
        from apyscript.display.stage import Stage
        self._stage_cls: Type[Stage] = Stage
        self.stage: Stage = stage

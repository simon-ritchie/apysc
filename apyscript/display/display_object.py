# -*- coding: future_annotations -*-

"""Implementations for DisplayObject class.
"""

from typing import List, Type
from abc import ABC, abstractmethod


class ChildBase(ABC):

    @abstractmethod
    def add_child(self, child) -> None:
        """
        Add display object child to this object.

        Parameters
        ----------
        child : DisplayObject
            Child object to add.
        """


class DisplayObject(ChildBase):

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
        self._childs: List[DisplayObject] = []

    def add_child(self, child) -> None:
        """
        Add display object child to this object.

        Parameters
        ----------
        child : DisplayObject
            Child object to add.
        """
        self._childs.append(child)

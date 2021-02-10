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

    _variable_name: str

    def __init__(self, stage, variable_name: str) -> None:
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
        self._variable_name = variable_name

    def add_child(self, child) -> None:
        """
        Add display object child to this object.

        Parameters
        ----------
        child : DisplayObject
            Child object to add.
        """
        self._childs.append(child)

    @property
    def variable_name(self) -> str:
        """
        Get a js variable name of this instance.

        Returns
        -------
        variable_name : str
            A js variable name of this instance.
        """
        return self._variable_name

    @variable_name.setter
    def variable_name(self, variable_name: str) -> None:
        """
        Set a js variable name of this instance.

        Parameters
        ----------
        variable_name : str
            Variable name to set.
        """
        self._variable_name = variable_name

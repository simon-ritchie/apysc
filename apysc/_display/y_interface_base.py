"""This module is for the base class of the y-coordinate
interfaces.
"""

from abc import ABC
from abc import abstractmethod

from apysc._type.int import Int


class YInterfaceBase(ABC):

    @property
    @abstractmethod
    def y(self) -> Int:
        """
        Get a y-coordinate.
        """

    @y.setter
    @abstractmethod
    def y(self, value: Int) -> None:
        """
        Update y-coordinate.

        Parameters
        ----------
        value : Int
            y-coordinate value.
        """

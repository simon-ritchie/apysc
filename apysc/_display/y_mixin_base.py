"""This module is for the base class of the y-coordinate
interfaces.
"""

from abc import ABC
from abc import abstractmethod
from typing import Union

from apysc._type.int import Int


class YMixInBase(ABC):

    _y: Int

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

    @abstractmethod
    def _update_y_and_skip_appending_exp(self, *, y: Union[int, Int]) -> None:
        """
        Update y-coordinate and skip appending an expression.

        Parameters
        ----------
        y : int or Int
            Y-coordinate value.
        """

    @abstractmethod
    def _initialize_y_if_not_initialized(self) -> None:
        """
        Initialize the _y attribute if this instance does not
        initialize it yet.
        """

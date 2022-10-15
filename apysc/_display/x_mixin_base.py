"""This module is for the base class of the x-coordinate
mix-in.
"""

from abc import ABC
from abc import abstractmethod
from typing import Union

from apysc._type.int import Int


class XMixInBase(ABC):

    _x: Int

    @property
    @abstractmethod
    def x(self) -> Int:
        """
        Get an x-coordinate.
        """

    @x.setter
    @abstractmethod
    def x(self, value: Int) -> None:
        """
        Update x-coordinate.

        Parameters
        ----------
        value : Int
            X-coordinate value.
        """

    @abstractmethod
    def _update_x_and_skip_appending_exp(self, *, x: Union[int, Int]) -> None:
        """
        Update x-coordinate and skip appending an expression.

        Parameters
        ----------
        x : int or Int
            X-coordinate value.
        """

    @abstractmethod
    def _initialize_x_if_not_initialized(self) -> None:
        """
        Initialize the _x attribute if this instance does not
        initialize it yet.
        """

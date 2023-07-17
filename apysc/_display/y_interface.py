"""The interface implementation for the y-coordinate.
"""

from abc import ABC
from abc import abstractmethod
from typing import Union

from apysc._type.number import Number


class YInterface(ABC):
    _y: Number

    @property
    @abstractmethod
    def y(self) -> Number:
        """
        Get a y-coordinate.
        """

    @y.setter
    @abstractmethod
    def y(self, value: Number) -> None:
        """
        Update y-coordinate.

        Parameters
        ----------
        value : Number
            y-coordinate value.
        """

    @abstractmethod
    def _update_y_and_skip_appending_exp(self, *, y: Union[float, Number]) -> None:
        """
        Update a y-coordinate and skip appending an expression.

        Parameters
        ----------
        y : float or Number
            Y-coordinate value.
        """

    @abstractmethod
    def _initialize_y_if_not_initialized(self) -> None:
        """
        Initialize the _y attribute if this instance does not
        initialize it yet.
        """

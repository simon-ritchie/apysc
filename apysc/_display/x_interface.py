"""The interface implementation for the x-coordinate.
"""

from abc import ABC
from abc import abstractmethod
from typing import Union

from apysc._type.number import Number


class XInterface(ABC):

    _x: Number

    @property
    @abstractmethod
    def x(self) -> Number:
        """
        Get an x-coordinate.
        """

    @x.setter
    @abstractmethod
    def x(self, value: Number) -> None:
        """
        Update x-coordinate.

        Parameters
        ----------
        value : Number
            X-coordinate value.
        """

    @abstractmethod
    def _update_x_and_skip_appending_exp(self, *, x: Union[float, Number]) -> None:
        """
        Update an x-coordinate and skip appending an expression.

        Parameters
        ----------
        x : float or Number
            X-coordinate value.
        """

    @abstractmethod
    def _initialize_x_if_not_initialized(self) -> None:
        """
        Initialize the _x attribute if this instance does not
        initialize it yet.
        """

"""This module is for the interface base class of setting
an x and y coordinate with a minimum point.
"""

from abc import ABC
from abc import abstractmethod


class SetXAndYWithMinimumPointInterfaceBase(ABC):
    @abstractmethod
    def _set_x_and_y_with_minimum_point(self) -> None:
        """
        Set an x and y properties coordinate with a minimum point.
        """

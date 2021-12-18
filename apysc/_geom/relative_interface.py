"""Interface class implementation for the relative value.
"""

from typing import Dict

from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface
from apysc._type.boolean import Boolean


class RelativeInterface:

    _relative: Boolean

    @property
    def relative(self) -> Boolean:
        """
        Get a boolean value indicating whether a path data
        is relative or not.

        Returns
        -------
        relative : Boolean
            A boolean value indicating whether path data
            is relative or not.
        """
        return self._relative._copy()

    @relative.setter
    def relative(self, value: Boolean) -> None:
        """
        Set a boolean value indicating whether path a path data
        is relative or not.

        Parameters
        ----------
        value : Boolean
            A boolean value indicating whether path data
            is relative or not.
        """
        self._relative.value = value

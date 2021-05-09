"""Dot setting class implementation for line.
"""

from typing import Union

from apysc import Int


class LineDotSetting:

    _dot_size: Int

    def __init__(self, dot_size: Union[int, Int]) -> None:
        """
        Dot setting class for line.

        Parameters
        ----------
        dot_size : int or Int
            Dot size.
        """
        from apysc.validation import number_validation
        number_validation.validate_integer(integer=dot_size)
        if isinstance(dot_size, int):
            dot_size_: Int = Int(dot_size)
        else:
            dot_size_ = dot_size._copy()
        self._dot_size = dot_size_

    @property
    def dot_size(self) -> Int:
        """
        Get a dot size setting.

        Returns
        -------
        dot_size : Int
            Dot size setting.
        """
        return self._dot_size._copy()

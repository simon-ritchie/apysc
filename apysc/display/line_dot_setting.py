"""Dot setting class implementation for line.
"""

from typing import Union

from apysc import Dictionary
from apysc import Int


class LineDotSetting(Dictionary):

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
        number_validation.validate_num_is_gt_zero(num=dot_size)
        if isinstance(dot_size, int):
            dot_size_: Int = Int(dot_size)
        else:
            dot_size_ = dot_size._copy()
        super(LineDotSetting, self).__init__({'dot_size': dot_size_})

    @property
    def dot_size(self) -> Int:
        """
        Get a dot size setting.

        Returns
        -------
        dot_size : Int
            Dot size setting.
        """
        return self['dot_size']._copy()

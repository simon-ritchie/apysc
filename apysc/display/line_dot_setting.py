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
        from apysc.converter.to_apysc_val_from_builtin import \
            get_copied_int_from_builtin_val
        from apysc.validation import number_validation
        number_validation.validate_nums_are_int_and_gt_zero(nums=[dot_size])
        dot_size_: Int = get_copied_int_from_builtin_val(integer=dot_size)
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

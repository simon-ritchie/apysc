"""Dash setting class implementation for line.
"""

from typing import Union

from apysc import Dictionary
from apysc import Int


class LineDashSetting(Dictionary):

    def __init__(
            self, dash_size: Union[int, Int],
            space_size: Union[int, Int]) -> None:
        """
        Dash setting class for line.

        Parameters
        ----------
        dash_size : int or Int
            Dash size.
        space_size : int or Int
            Blank space size between dashes.
        """
        from apysc.converter.to_apysc_val_from_builtin import \
            get_copied_int_from_builtin_val
        from apysc.validation import number_validation
        number_validation.validate_nums_are_int_and_gt_zero(
            nums=[dash_size, space_size])
        dash_size_: Int = get_copied_int_from_builtin_val(integer=dash_size)
        space_size_: Int = get_copied_int_from_builtin_val(integer=space_size)
        super(LineDashSetting, self).__init__({
            'dash_size': dash_size_,
            'space_size': space_size_,
        })

    @property
    def dash_size(self) -> Int:
        """
        Get a dash size setting.

        Returns
        -------
        dash_size : Int
            Dash size setting.
        """
        return self['dash_size']

    @property
    def space_size(self) -> Int:
        """
        Get a space size setting.

        Returns
        -------
        space_size : Int
            Space size setting.
        """
        return self['space_size']

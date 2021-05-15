"""Dash dot (1-dot chain) setting for line.
"""

from typing import Union

from apysc import Dictionary
from apysc import Int


class LineDashDotSetting(Dictionary):

    def __init__(
            self, dot_size: Union[int, Int],
            dash_size: Union[int, Int],
            space_size: Union[int, Int]) -> None:
        """
        Dash dot (1-dot chain) setting for line.

        Parameters
        ----------
        dot_size : int or Int
            Dot size.
        dash_size : int or Int
            Dash size.
        space_size : int or Int
            Blank space size between dots and dashes.
        """
        from apysc.validation import number_validation
        from apysc.converter.to_apysc_val_from_builtin import \
            get_copied_int_from_builtin_val
        number_validation.validate_nums_are_int_and_gt_zero(
            nums=[dot_size, dash_size, space_size])
        dot_size_: Int = get_copied_int_from_builtin_val(integer=dot_size)
        dash_size_: Int = get_copied_int_from_builtin_val(integer=dash_size)
        space_size_: Int = get_copied_int_from_builtin_val(integer=space_size)
        super(LineDashDotSetting, self).__init__({
            'dot_size': dot_size_,
            'dash_size': dash_size_,
            'space_size': space_size_,
        })

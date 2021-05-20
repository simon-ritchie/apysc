"""Round dot setting class implementation for line.
"""

from typing import Union

from apysc import Dictionary
from apysc import Int


class LineRoundDotSetting(Dictionary):

    def __init__(
            self, round_size: Union[int, Int],
            space_size: Union[int, Int]) -> None:
        """
        Round dot setting class for line.

        Parameters
        ----------
        round_size : int or Int
            Dot round size.
        space_size : int or Int
            Blank space size between dots.
        """
        from apysc.converter.to_apysc_val_from_builtin import \
            get_copied_int_from_builtin_val
        from apysc.validation import number_validation
        number_validation.validate_nums_are_int_and_gt_zero(
            nums=[round_size, space_size])
        round_size_: Int = get_copied_int_from_builtin_val(integer=round_size)
        space_size_: Int = get_copied_int_from_builtin_val(integer=space_size)
        super(LineRoundDotSetting, self).__init__({
            'round_size': round_size_,
            'space_size': space_size_,
        })

    @property
    def round_size(self) -> Int:
        """
        Get a round size setting.

        Returns
        -------
        round_size : Int
            Round size setting.
        """
        return self['round_size']

    @property
    def space_size(self) -> Int:
        """
        Get a space size setting.

        Returns
        -------
        space_size : Int
            Blank space size between dots.
        """
        return self['space_size']

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
            Dot's round size.
        space_size : int or Int
            Blank space size between dots.
        """
        from apysc.validation import number_validation
        for size in (round_size, space_size):
            number_validation.validate_integer(integer=size)
            number_validation.validate_num_is_gte_zero(num=size)
        if isinstance(round_size, int):
            round_size_: Int = Int(round_size)
        else:
            round_size_ = round_size._copy()
        if isinstance(space_size, int):
            space_size_: Int = Int(space_size)
        else:
            space_size_ = space_size._copy()
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

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
            Blank space size between the dashes.
        """
        from apysc.validation import number_validation
        for size in (dash_size, space_size):
            number_validation.validate_integer(integer=size)
            number_validation.validate_num_is_gte_zero(num=size)
        if isinstance(dash_size, int):
            dash_size_: Int = Int(dash_size)
        else:
            dash_size_ = dash_size._copy()
        if isinstance(space_size, int):
            space_size_: Int = Int(space_size)
        else:
            space_size_ = space_size._copy()
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

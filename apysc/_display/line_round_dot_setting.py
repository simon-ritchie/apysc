"""Round dot setting class implementation for line.
"""

from typing import Union

import apysc as ap


class LineRoundDotSetting(ap.Dictionary[str, ap.Int]):
    """
    Round dot setting class for a line.

    References
    ----------
    - Graphics line_style interface document
        - https://bit.ly/3zauILT
    """

    def __init__(
            self, round_size: Union[int, ap.Int],
            space_size: Union[int, ap.Int]) -> None:
        """
        Round dot setting class for line.

        Parameters
        ----------
        round_size : int or Int
            Dot round size.
        space_size : int or Int
            Blank space size between dots.

        References
        ----------
        - Graphics line_style interface document
            - https://bit.ly/3zauILT
        """
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=LineRoundDotSetting):
            from apysc._converter.to_apysc_val_from_builtin import \
                get_copied_int_from_builtin_val
            from apysc._validation import number_validation
            number_validation.validate_nums_are_int_and_gt_zero(
                nums=[round_size, space_size])
            round_size_: ap.Int = get_copied_int_from_builtin_val(
                integer=round_size)
            space_size_: ap.Int = get_copied_int_from_builtin_val(
                integer=space_size)
            super(LineRoundDotSetting, self).__init__({
                'round_size': round_size_,
                'space_size': space_size_,
            })

    @property
    def round_size(self) -> ap.Int:
        """
        Get a round size setting.

        Returns
        -------
        round_size : Int
            Round size setting.
        """
        with ap.DebugInfo(
                callable_='round_size', locals_=locals(),
                module_name=__name__, class_=LineRoundDotSetting):
            return self['round_size']

    @property
    def space_size(self) -> ap.Int:
        """
        Get a space size setting.

        Returns
        -------
        space_size : Int
            Blank space size between dots.
        """
        with ap.DebugInfo(
                callable_='space_size', locals_=locals(),
                module_name=__name__, class_=LineRoundDotSetting):
            return self['space_size']

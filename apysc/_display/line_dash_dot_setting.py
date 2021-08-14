"""Dash dot (1-dot chain) setting for line.
"""

from typing import Union

import apysc as ap


class LineDashDotSetting(ap.Dictionary[str, ap.Int]):
    """
    Dash dot (1-dot chain) setting for a line.

    References
    ----------
    - Graphics line_style interface document
        - https://bit.ly/3zauILT
    """

    def __init__(
            self, dot_size: Union[int, ap.Int],
            dash_size: Union[int, ap.Int],
            space_size: Union[int, ap.Int]) -> None:
        """
        Dash dot (1-dot chain) setting for a line.

        Parameters
        ----------
        dot_size : int or Int
            Dot size.
        dash_size : int or Int
            Dash size.
        space_size : int or Int
            Blank space size between dots and dashes.

        References
        ----------
        - Graphics line_style interface document
            - https://bit.ly/3zauILT
        """
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=LineDashDotSetting):
            from apysc._converter.to_apysc_val_from_builtin import \
                get_copied_int_from_builtin_val
            from apysc._validation import number_validation
            number_validation.validate_nums_are_int_and_gt_zero(
                nums=[dot_size, dash_size, space_size])
            dot_size_: ap.Int = get_copied_int_from_builtin_val(
                integer=dot_size)
            dash_size_: ap.Int = get_copied_int_from_builtin_val(
                integer=dash_size)
            space_size_: ap.Int = get_copied_int_from_builtin_val(
                integer=space_size)
            super(LineDashDotSetting, self).__init__({
                'dot_size': dot_size_,
                'dash_size': dash_size_,
                'space_size': space_size_,
            })

    @property
    def dot_size(self) -> ap.Int:
        """
        Get a dot size setting.

        Returns
        -------
        dot_size : Int
            Dot size setting.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='dot_size', locals_=locals(),
                module_name=__name__, class_=LineDashDotSetting):
            return self['dot_size']

    @property
    def dash_size(self) -> ap.Int:
        """
        Get a dash size setting.

        Returns
        -------
        dash_size : Int
            Dash size setting.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='dash_size', locals_=locals(),
                module_name=__name__, class_=LineDashDotSetting):
            return self['dash_size']

    @property
    def space_size(self) -> ap.Int:
        """
        Get a space size setting.

        Returns
        -------
        space_size : Int
            Space size setting.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='space_size', locals_=locals(),
                module_name=__name__, class_=LineDashDotSetting):
            return self['space_size']

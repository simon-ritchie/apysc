"""Dot setting class implementation for line.
"""

from typing import Union

import apysc as ap


class LineDotSetting(ap.Dictionary):
    """
    Dot setting class for a line.

    References
    ----------
    - Graphics line_style interface document
        - https://bit.ly/3zauILT
    """

    def __init__(self, dot_size: Union[int, ap.Int]) -> None:
        """
        Dot setting class for a line.

        Parameters
        ----------
        dot_size : int or Int
            Dot size.

        References
        ----------
        - Graphics line_style interface document
            - https://bit.ly/3zauILT
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=LineDotSetting):
            from apysc._converter.to_apysc_val_from_builtin import \
                get_copied_int_from_builtin_val
            from apysc._validation import number_validation
            number_validation.validate_nums_are_int_and_gt_zero(
                nums=[dot_size])
            dot_size_: ap.Int = get_copied_int_from_builtin_val(
                integer=dot_size)
            super(LineDotSetting, self).__init__({'dot_size': dot_size_})

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
                module_name=__name__, class_=LineDotSetting):
            return self['dot_size']._copy()

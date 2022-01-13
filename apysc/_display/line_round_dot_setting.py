"""Round dot setting class implementation for line.
"""

from typing import Union

from apysc._type.dictionary import Dictionary
from apysc._type.int import Int


class LineRoundDotSetting(Dictionary[str, Int]):
    """
    Round dot setting class for a line.

    References
    ----------
    - Graphics line_style interface document
        - https://bit.ly/3zauILT

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.line_style(color='#fff', thickness=10)
    >>> line: ap.Line = sprite.graphics.draw_line(
    ...     x_start=50, y_start=50, x_end=150, y_end=50)
    >>> line.line_round_dot_setting = ap.LineRoundDotSetting(
    ...     round_size=10, space_size=5)
    >>> line.line_round_dot_setting.round_size
    Int(10)

    >>> line.line_round_dot_setting.space_size
    Int(5)
    """

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

        References
        ----------
        - Graphics line_style interface document
            - https://bit.ly/3zauILT

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50)
        >>> line.line_round_dot_setting = ap.LineRoundDotSetting(
        ...     round_size=10, space_size=5)
        >>> line.line_round_dot_setting.round_size
        Int(10)

        >>> line.line_round_dot_setting.space_size
        Int(5)
        """
        import apysc as ap
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
    def round_size(self) -> Int:
        """
        Get a round size setting.

        Returns
        -------
        round_size : Int
            Round size setting.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50)
        >>> line.line_round_dot_setting = ap.LineRoundDotSetting(
        ...     round_size=10, space_size=5)
        >>> line.line_round_dot_setting.round_size
        Int(10)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='round_size', locals_=locals(),
                module_name=__name__, class_=LineRoundDotSetting):
            return self['round_size']

    @property
    def space_size(self) -> Int:
        """
        Get a space size setting.

        Returns
        -------
        space_size : Int
            Blank space size between dots.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50)
        >>> line.line_round_dot_setting = ap.LineRoundDotSetting(
        ...     round_size=10, space_size=5)
        >>> line.line_round_dot_setting.space_size
        Int(5)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='space_size', locals_=locals(),
                module_name=__name__, class_=LineRoundDotSetting):
            return self['space_size']

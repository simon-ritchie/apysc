"""Dash dot (1-dot chain) setting for line.
"""

from typing import Union

from apysc._type.dictionary import Dictionary
from apysc._type.int import Int


class LineDashDotSetting(Dictionary[str, Int]):
    """
    Dash dot (1-dot chain) setting for a line.

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
    >>> line.line_dash_dot_setting = ap.LineDashDotSetting(
    ...     dot_size=2, dash_size=5, space_size=3)
    >>> line.line_dash_dot_setting.dot_size
    Int(2)

    >>> line.line_dash_dot_setting.dash_size
    Int(5)

    >>> line.line_dash_dot_setting.space_size
    Int(3)
    """

    def __init__(
            self, dot_size: Union[int, Int],
            dash_size: Union[int, Int],
            space_size: Union[int, Int]) -> None:
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

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50)
        >>> line.line_dash_dot_setting = ap.LineDashDotSetting(
        ...     dot_size=2, dash_size=5, space_size=3)
        >>> line.line_dash_dot_setting.dot_size
        Int(2)

        >>> line.line_dash_dot_setting.dash_size
        Int(5)

        >>> line.line_dash_dot_setting.space_size
        Int(3)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=LineDashDotSetting):
            from apysc._converter.to_apysc_val_from_builtin import \
                get_copied_int_from_builtin_val
            from apysc._validation import number_validation
            number_validation.validate_nums_are_int_and_gt_zero(
                nums=[dot_size, dash_size, space_size])
            dot_size_: Int = get_copied_int_from_builtin_val(
                integer=dot_size)
            dash_size_: Int = get_copied_int_from_builtin_val(
                integer=dash_size)
            space_size_: Int = get_copied_int_from_builtin_val(
                integer=space_size)
            super(LineDashDotSetting, self).__init__({
                'dot_size': dot_size_,
                'dash_size': dash_size_,
                'space_size': space_size_,
            })

    @property
    def dot_size(self) -> Int:
        """
        Get a dot size setting.

        Returns
        -------
        dot_size : Int
            Dot size setting.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50)
        >>> line.line_dash_dot_setting = ap.LineDashDotSetting(
        ...     dot_size=2, dash_size=5, space_size=3)
        >>> line.line_dash_dot_setting.dot_size
        Int(2)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='dot_size', locals_=locals(),
                module_name=__name__, class_=LineDashDotSetting):
            return self['dot_size']

    @property
    def dash_size(self) -> Int:
        """
        Get a dash size setting.

        Returns
        -------
        dash_size : Int
            Dash size setting.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50)
        >>> line.line_dash_dot_setting = ap.LineDashDotSetting(
        ...     dot_size=2, dash_size=5, space_size=3)
        >>> line.line_dash_dot_setting.dash_size
        Int(5)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='dash_size', locals_=locals(),
                module_name=__name__, class_=LineDashDotSetting):
            return self['dash_size']

    @property
    def space_size(self) -> Int:
        """
        Get a space size setting.

        Returns
        -------
        space_size : Int
            Space size setting.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50)
        >>> line.line_dash_dot_setting = ap.LineDashDotSetting(
        ...     dot_size=2, dash_size=5, space_size=3)
        >>> line.line_dash_dot_setting.space_size
        Int(3)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='space_size', locals_=locals(),
                module_name=__name__, class_=LineDashDotSetting):
            return self['space_size']

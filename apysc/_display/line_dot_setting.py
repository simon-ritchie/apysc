"""Dot setting class implementation for a line.
"""

from typing import Union

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.dictionary import Dictionary
from apysc._type.int import Int


class LineDotSetting(Dictionary[str, Int]):
    """
    Dot setting class for a line.

    References
    ----------
    - Graphics line_style interface document
        - https://simon-ritchie.github.io/apysc/graphics_line_style.html  # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.line_style(color='#fff', thickness=10)
    >>> line: ap.Line = sprite.graphics.draw_line(
    ...     x_start=50, y_start=50, x_end=150, y_end=50)
    >>> line.line_dot_setting = ap.LineDotSetting(dot_size=5)
    >>> line.line_dot_setting.dot_size
    Int(5)
    """

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='LineDotSetting')
    def __init__(self, dot_size: Union[int, Int]) -> None:
        """
        Dot setting class for a line.

        Parameters
        ----------
        dot_size : int or Int
            Dot size.

        References
        ----------
        - Graphics line_style interface document
            - https://simon-ritchie.github.io/apysc/graphics_line_style.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50)
        >>> line.line_dot_setting = ap.LineDotSetting(dot_size=5)
        >>> line.line_dot_setting.dot_size
        Int(5)
        """
        import apysc as ap
        from apysc._converter.to_apysc_val_from_builtin import \
            get_copied_int_from_builtin_val
        from apysc._validation import number_validation
        number_validation.validate_nums_are_int_and_gt_zero(
            nums=[dot_size])
        dot_size_: ap.Int = get_copied_int_from_builtin_val(
            integer=dot_size)
        super(LineDotSetting, self).__init__({'dot_size': dot_size_})

    @property  # type: ignore[misc]
    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='LineDotSetting')
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
        >>> line.line_dot_setting = ap.LineDotSetting(dot_size=5)
        >>> line.line_dot_setting.dot_size
        Int(5)
        """
        return self['dot_size']._copy()

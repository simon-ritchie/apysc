"""Path data class implementation for the svg's `close path` (Z).
"""

from apysc._geom.path_data_base import PathDataBase
from apysc._type.string import String


class PathClose(PathDataBase):
    """
    Path data class for the svg's `close path` (Z).

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.line_style(color='#fff', thickness=3)
    >>> path: ap.Path = sprite.graphics.draw_path(
    ...     path_data_list=[
    ...         ap.PathMoveTo(x=0, y=00),
    ...         ap.PathLineTo(x=50, y=0),
    ...         ap.PathLineTo(x=50, y=50),
    ...         ap.PathClose(),
    ...     ])
    """

    def __init__(self) -> None:
        """
        Path data class for the svg's `close path` (Z).

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=3)
        >>> path: ap.Path = sprite.graphics.draw_path(
        ...     path_data_list=[
        ...         ap.PathMoveTo(x=0, y=00),
        ...         ap.PathLineTo(x=50, y=0),
        ...         ap.PathLineTo(x=50, y=50),
        ...         ap.PathClose(),
        ...     ])
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=PathClose):
            from apysc._geom.path_label import PathLabel
            super(PathClose, self).__init__(
                path_label=PathLabel.CLOSE,
                relative=False)

    def _get_svg_str(self) -> str:
        """
        Get a path's SVG string created with the current setting.

        Returns
        -------
        svg_str : str
            A path's SVG string created with the current setting.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._get_svg_str, locals_=locals(),
                module_name=__name__, class_=PathClose):
            from apysc._type import value_util
            svg_char: String = self._get_svg_char()
            svg_str: str = value_util.get_value_str_for_expression(
                value=svg_char)
            return svg_str

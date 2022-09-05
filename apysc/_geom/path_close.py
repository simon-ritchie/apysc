"""This module is for the SVG's `close path` (Z) path
data class implementation.
"""

from typing_extensions import final

from apysc._geom.path_data_base import PathDataBase
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.string import String


class PathClose(PathDataBase):
    """
    Path data class for the SVG's `close path` (Z).

    References
    ----------
    - Path class
        - https://simon-ritchie.github.io/apysc/en/path.html
    - Graphics draw_path interface
        - https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html
    - PathClose class
        - https://simon-ritchie.github.io/apysc/en/path_close.html

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.line_style(color="#fff", thickness=3)
    >>> path: ap.Path = sprite.graphics.draw_path(
    ...     path_data_list=[
    ...         ap.PathMoveTo(x=0, y=00),
    ...         ap.PathLineTo(x=50, y=0),
    ...         ap.PathLineTo(x=50, y=50),
    ...         ap.PathClose(),
    ...     ]
    ... )
    """

    @final
    @add_debug_info_setting(module_name=__name__)
    def __init__(self) -> None:
        """
        Path data class for the SVG's `close path` (Z).

        References
        ----------
        - Path class
            - https://simon-ritchie.github.io/apysc/en/path.html
        - Graphics draw_path interface
            - https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html
        - PathClose class
            - https://simon-ritchie.github.io/apysc/en/path_close.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color="#fff", thickness=3)
        >>> path: ap.Path = sprite.graphics.draw_path(
        ...     path_data_list=[
        ...         ap.PathMoveTo(x=0, y=00),
        ...         ap.PathLineTo(x=50, y=0),
        ...         ap.PathLineTo(x=50, y=50),
        ...         ap.PathClose(),
        ...     ]
        ... )
        """
        from apysc._geom.path_label import PathLabel

        super(PathClose, self).__init__(path_label=PathLabel.CLOSE, relative=False)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _get_svg_str(self) -> str:
        """
        Get a path's SVG string created with the current setting.

        Returns
        -------
        svg_str : str
            An SVG path string was created with the current
            setting.
        """
        from apysc._type import value_util

        svg_char: String = self._get_svg_char()
        svg_str: str = value_util.get_value_str_for_expression(value=svg_char)
        return svg_str

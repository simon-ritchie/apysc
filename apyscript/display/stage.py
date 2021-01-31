"""Stage (canvas) implementation.
"""

from apyscript.expression import file_util
from apyscript.color import color_util


class Stage:

    _stage_width: int
    _stage_height: int
    _background_color: str

    def __init__(
            self, stage_width: int = 300, stage_height: int = 185,
            background_color: str = '#ffffff') -> None:
        """
        Create Stage (canvas) instance.

        Parameters
        ----------
        stage_width : int, default 300
            Stage width.
        stage_height : int, default 185
            Stage height
        background_color : str, default '#ffffff'
            Hexadecimal background color string.
        """
        file_util.empty_expression_dir()
        self._stage_width = stage_width
        self._stage_height = stage_height
        background_color = color_util.complement_hex_color(
            hex_color_code=background_color)
        self._background_color = background_color

    @property
    def stage_width(self) -> int:
        """
        Get this stage's width.

        Returns
        -------
        stage_width : int
            This stage's width.
        """
        return self._stage_width

    @stage_width.setter
    def stage_width(self, stage_width: int) -> None:
        """
        Set this stage's width.

        Parameters
        ----------
        stage_width : int
            Stage width to set.
        """
        self._stage_width = stage_width

    @property
    def stage_height(self) -> int:
        """
        Get this stage's height.

        Returns
        -------
        stage_height : int
            This stage's height.
        """
        return self._stage_height

    @stage_height.setter
    def stage_height(self, stage_height: int) -> None:
        """
        Set this stage's height.

        Parameters
        ----------
        stage_height : int
            Stage height to set.
        """
        self._stage_height = stage_height

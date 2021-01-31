"""Stage (canvas) implementation.
"""

from apyscript.expression import file_util


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
        self._background_color = background_color

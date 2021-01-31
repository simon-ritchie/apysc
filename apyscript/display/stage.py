"""Stage (canvas) implementation.
"""

from apyscript.expression import file_util
from apyscript.color import color_util
from apyscript.geom import size_util


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


    def _validate_stage_size(self) -> None:
        """
        Check that current stage width and height is valid value.

        Raises
        ------
        ValueError
            - If non-integer value specified.
            - If width or height is less than or equal to zero.
        """
        size_util.validate_size_is_int(
            size=self.stage_width,
            err_msg=(
                f'Stage width is set non-integer value: {self.stage_width}'))
        size_util.validate_size_is_int(
            size=self.stage_height,
            err_msg=(
                'Stage height is set non-integer value: '
                f'{self.stage_height}'))
        pass

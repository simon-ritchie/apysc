"""Stage (canvas) implementation.
"""

from typing import Optional
from datetime import datetime
import random

from apyscript.expression import file_util
from apyscript.color import color_util
from apyscript.geom import size_util
from apyscript.geom import converter
from apyscript.html import html_util


class Stage:

    _stage_width: int
    _stage_height: int
    _background_color: str
    _add_to: str
    _stage_elem_id: str

    def __init__(
            self, stage_width: int = 300, stage_height: int = 185,
            background_color: str = '#ffffff',
            add_to: str = 'body',
            stage_elem_id: Optional[str] = None) -> None:
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
        add_to : str, default 'body'
            Specification of element to add stage.
            Unique tag (e.g., 'body') or ID selector
            (e.g., '#any-unique-elem') is acceptable.
        stage_elem_id : str or None, optional
            ID attribute set to stage html element (e.g., 'line-graph').
            If None is set, random integer will be applied.
        """
        file_util.empty_expression_dir()
        self._stage_width = stage_width
        self._stage_height = stage_height
        self._validate_stage_size()
        background_color = color_util.complement_hex_color(
            hex_color_code=background_color)
        self._background_color = background_color
        self._add_to = add_to
        self._stage_elem_id = self._create_stage_elem_id_if_none(
            stage_elem_id=stage_elem_id)
        self._stage_elem_id = html_util.remove_first_selector_symbol_char(
            str_val=self._stage_elem_id)
        self._append_expression_constructor_expression()

    def _create_stage_elem_id_if_none(
            self, stage_elem_id: Optional[str]) -> str:
        """
        Create random stage element id if specified id is None.

        Parameters
        ----------
        stage_elem_id : str or None
            Specified stage element id.

        Returns
        -------
        result_id : str
            If specified id is not None, then unchanged argument value
            will be returned.
            Otherwise, random integer string will be returned.
        """
        if stage_elem_id is not None:
            return stage_elem_id
        now_timestamp: int = int(datetime.now().timestamp() * 1000)
        random_int: int = random.randint(1000000, 10000000)
        result_id: str = f'{now_timestamp}{random_int}'
        return result_id

    def _append_expression_constructor_expression(self) -> None:
        """
        Append stage constructor expression to file.
        """
        expression: str = self._make_constructor_expression()
        pass

    def _make_constructor_expression(self) -> str:
        """
        Make a stage constructor expression string.

        Returns
        -------
        expression : str
            Result expression.
        """
        style: str = (
            f'width: {self.stage_width}px;'
            f' height: {self.stage_height}px;'
            f' background-color: {self._background_color};'
        )
        expression: str = f"""<script type="text/javascript">
$(document).ready(function() {{
    var html = '<div id="{self._stage_elem_id}" style="{style}"></div>';
    $("{self._add_to}").append(html);
}});"""
        return expression

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
        stage_width = converter.to_int_from_float(int_or_float=stage_width)
        self._stage_width = stage_width
        self._validate_stage_size()

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
        stage_height = converter.to_int_from_float(int_or_float=stage_height)
        self._stage_height = stage_height
        self._validate_stage_size()

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
        size_util.validate_size_is_greater_than_zero(
            size=self.stage_width,
            err_msg=(
                'Stage width can not be set less than or equal to zero: '
                f'{self.stage_width}'))
        size_util.validate_size_is_greater_than_zero(
            size=self.stage_height,
            err_msg=(
                'Stage height can not be set less than or equal to zero: '
                f'{self.stage_height}'))

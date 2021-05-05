"""Stage (canvas) implementation.
"""

import os
import random
from datetime import datetime
from typing import Any
from typing import Optional

from apysc import Int
from apysc.display.child_interface import ChildInterface
from apysc.display.height_interface import HeightInterface
from apysc.display.width_interface import WidthInterface
from apysc.event.mouse_event_interfaces import MouseEventInterfaces
from apysc.expression import expression_file_util
from apysc.type.variable_name_interface import VariableNameInterface

_STAGE_ELEM_ID_FILE_PATH: str = os.path.join(
    expression_file_util.EXPRESSION_ROOT_DIR, 'stage_elem_id.txt',
)


class Stage(
        ChildInterface, WidthInterface, HeightInterface,
        VariableNameInterface, MouseEventInterfaces):

    _background_color: str
    _add_to: str
    _stage_elem_id: str
    stage: Any

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
        from apysc import Array
        from apysc.color import color_util
        from apysc.html import html_util
        from apysc.validation import string_validation
        expression_file_util.empty_expression_dir()
        self.stage = self
        self._stage_elem_id = self._create_stage_elem_id_if_none(
            stage_elem_id=stage_elem_id)
        string_validation.validate_not_empty_string(
            string=self._stage_elem_id)
        self._save_stage_elem_id_to_expression_file()
        self._stage_elem_id = html_util.remove_first_selector_symbol_char(
            str_val=self._stage_elem_id)
        self.variable_name = get_stage_variable_name()
        self._update_width_and_skip_appending_exp(value=Int(stage_width))
        self._update_height_and_skip_appending_exp(value=Int(stage_height))

        background_color = color_util.complement_hex_color(
            hex_color_code=background_color)
        self._background_color = background_color
        string_validation.validate_not_empty_string(string=add_to)
        self._add_to = add_to
        self._append_constructor_expression()
        self._children = Array([])

    def _save_stage_elem_id_to_expression_file(self) -> None:
        """
        Save stage element id to expression directory's file.
        """
        from apysc.file import file_util
        file_util.save_plain_txt(
            txt=self._stage_elem_id,
            file_path=_STAGE_ELEM_ID_FILE_PATH)

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
        result_id: str = f'stage_{now_timestamp}{random_int}'
        return result_id

    def _append_constructor_expression(self) -> None:
        """
        Append stage constructor expression to file.
        """
        expression: str = self._make_constructor_expression()
        expression_file_util.append_js_expression(expression=expression)

    def _make_constructor_expression(self) -> str:
        """
        Make a stage constructor expression string.

        Returns
        -------
        expression : str
            Result expression.
        """
        style: str = self._make_style_str()
        expression: str = (
            f'var stage_html = \'<div id="{self._stage_elem_id}" '
            f'style="{style}"></div>\';'
            f'\n$("{self._add_to}").append(stage_html);'
            f'\n{get_stage_variable_name()} = SVG()'
            f'.addTo("#{self._stage_elem_id}").size('
            f'\n  {self.width}, {self.height});'
        )
        return expression

    def _make_style_str(self) -> str:
        """
        Make a stage's style string.

        Returns
        -------
        style : str
            Result style string (width, height, etc).
        """
        style: str = (
            f'width: {self.width}px;'
            f' height: {self.height}px;'
            f' background-color: {self._background_color};'
        )
        return style

    @property
    def stage_elem_id(self) -> str:
        """
        Get stage's html element id.

        Returns
        -------
        stage_elem_id : str
            Stage's html element id (not including class or id symbol).
            e.g., 'line-graph'
        """
        return self._stage_elem_id


def get_stage_elem_id() -> str:
    """
    Get current stage's element id.

    Returns
    -------
    stage_elem_id : str
        Current stage's element id. If stage is not instantiated yet,
        blank string will be set.
    """
    from apysc.file import file_util
    if not os.path.isfile(_STAGE_ELEM_ID_FILE_PATH):
        return ''
    stage_elem_id: str = file_util.read_txt(
        file_path=_STAGE_ELEM_ID_FILE_PATH)
    return stage_elem_id


def get_stage_variable_name() -> str:
    """
    Get current stage's global variable name.

    Returns
    -------
    stage_variable_name : str
        Current stage's js global variable name. If stage is not
        instantiated yet, blank string will be set.
    """
    stage_elem_id: str = get_stage_elem_id()
    stage_variable_name: str = stage_elem_id.replace('-', '_')
    return stage_variable_name


def get_stage_elem_str() -> str:
    """
    Get current stage's jQuery element string.

    Returns
    -------
    stage_elem_str : str
        Stage's jQuery element string (e.g., '$("#<stage_elem_id>")').
    """
    stage_elem_id: str = get_stage_elem_id()
    stage_elem_str: str = f'$("#{stage_elem_id}")'
    return stage_elem_str

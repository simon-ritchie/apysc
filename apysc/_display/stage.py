"""Stage (canvas) implementation.

References
----------
- Stage document
    - https://simon-ritchie.github.io/apysc/stage.html
"""

import random
from datetime import datetime
from typing import Optional
from typing import Tuple

import apysc as ap
from apysc._display.child_interface import ChildInterface
from apysc._display.height_interface import HeightInterface
from apysc._display.width_interface import WidthInterface
from apysc._event.custom_event_interface import CustomEventInterface
from apysc._event.mouse_event_interfaces import MouseEventInterfaces
from apysc._expression import expression_data_util
from apysc._type.variable_name_interface import VariableNameInterface


class Stage(
        ChildInterface, WidthInterface, HeightInterface,
        VariableNameInterface, MouseEventInterfaces,
        CustomEventInterface):
    """
    The Stage (overall viewport) class.

    References
    ----------
    Stage document
        https://simon-ritchie.github.io/apysc/stage.html
    """

    _background_color: str
    _add_to: str
    _stage_elem_id: str
    stage: 'Stage'

    def __init__(
            self, stage_width: int = 300, stage_height: int = 185,
            background_color: str = '#ffffff',
            add_to: str = 'body',
            stage_elem_id: Optional[str] = None) -> None:
        """
        Create Stage (overall viewport) instance.

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

        References
        ----------
        Stage document
            https://simon-ritchie.github.io/apysc/stage.html
        """
        from apysc._color import color_util
        from apysc._html import html_util
        from apysc._validation import string_validation
        expression_data_util.empty_expression()
        self.stage = self
        self._stage_elem_id = self._create_stage_elem_id_if_none(
            stage_elem_id=stage_elem_id)
        string_validation.validate_not_empty_string(
            string=self._stage_elem_id)
        self._save_stage_elem_id()
        self._stage_elem_id = html_util.remove_first_selector_symbol_char(
            str_val=self._stage_elem_id)
        self.variable_name = get_stage_variable_name()
        self._update_width_and_skip_appending_exp(value=ap.Int(stage_width))
        self._update_height_and_skip_appending_exp(value=ap.Int(stage_height))

        background_color = color_util.complement_hex_color(
            hex_color_code=background_color)
        self._background_color = background_color
        string_validation.validate_not_empty_string(string=add_to)
        self._add_to = add_to
        self._append_constructor_expression()
        self._children = ap.Array([])

    def _save_stage_elem_id(self) -> None:
        """
        Save the stage element id.
        """
        from apysc._expression import expression_data_util
        table_name: str = expression_data_util.TableName.STAGE_ELEM_ID.value
        query: str = f'DELETE FROM {table_name};'
        expression_data_util.exec_query(sql=query, commit=False)
        query = (
            f'INSERT INTO {table_name}(elem_id) '
            f"VALUES ('{self._stage_elem_id}');")
        expression_data_util.exec_query(sql=query)

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
        Append stage constructor expression.
        """
        expression: str = self._make_constructor_expression()
        ap.append_js_expression(expression=expression)

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

    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of
        debugging).

        Returns
        -------
        repr_str : str
            Type name and elem id will be set
            (e.g., `Stage('<stage_elem_id>')`).
        """
        repr_str: str = f"Stage('{self.stage_elem_id}')"
        return repr_str


def get_stage_elem_id() -> str:
    """
    Get current stage's element id.

    Returns
    -------
    stage_elem_id : str
        Current stage's element id. If stage is not instantiated yet,
        blank string will be set.
    """
    from apysc._expression import expression_data_util
    table_name: str = expression_data_util.TableName.STAGE_ELEM_ID.value
    query: str = (
        f'SELECT elem_id FROM {table_name} LIMIT 1;'
    )
    expression_data_util.exec_query(sql=query)
    result: Optional[Tuple[str]] = expression_data_util.cursor.fetchone()
    if result is None:
        return ''
    return result[0]


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

"""Stage-related implementations.

References
----------
- Stage document
    - https://simon-ritchie.github.io/apysc/en/stage.html
"""

import ctypes
import random
from datetime import datetime
from typing import Optional
from typing import Tuple

from typing_extensions import final

from apysc._display.child_mixin import ChildMixIn
from apysc._display.height_mixin import HeightMixIn
from apysc._display.width_mixin import WidthMixIn
from apysc._event.custom_event_mixin import CustomEventMixIn
from apysc._event.enter_frame_mixin import EnterFrameMixIn
from apysc._event.mouse_event_mixins import MouseEventMixIns
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos

# This is used only for avoiding gabage collection.
_current_stage: "Stage"


class Stage(
    ChildMixIn,
    WidthMixIn,
    HeightMixIn,
    EnterFrameMixIn,
    MouseEventMixIns,
    CustomEventMixIn,
    VariableNameSuffixMixIn,
):
    """
    The Stage (overall view-area) class.

    References
    ----------
    - Stage
        - https://simon-ritchie.github.io/apysc/en/stage.html

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage(
    ...     stage_width=500,
    ...     stage_height=300,
    ...     background_color="#333",
    ...     stage_elem_id="sales_chart",
    ... )
    """

    _background_color: str
    _add_to: str
    _stage_elem_id: str
    stage: "Stage"

    @arg_validation_decos.is_builtin_integer(arg_position_index=1)
    @arg_validation_decos.is_builtin_integer(arg_position_index=2)
    @arg_validation_decos.is_hex_color_code_format(arg_position_index=3)
    @arg_validation_decos.is_builtin_string(arg_position_index=4, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=5, optional=True)
    @arg_validation_decos.is_builtin_string(arg_position_index=6, optional=False)
    def __init__(
        self,
        *,
        stage_width: int = 300,
        stage_height: int = 185,
        background_color: str = "#ffffff",
        add_to: str = "body",
        stage_elem_id: Optional[str] = None,
        variable_name_suffix: str = "",
    ) -> None:
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
            ID attribute set to stage HTML element (e.g., 'line-graph').
            If None is set, a random integer will be applied.
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        References
        ----------
        - Stage
            - https://simon-ritchie.github.io/apysc/en/stage.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage(
        ...     stage_width=500,
        ...     stage_height=300,
        ...     background_color="#333",
        ...     stage_elem_id="sales_chart",
        ... )
        """
        import apysc as ap
        from apysc._color import color_util
        from apysc._expression import expression_data_util
        from apysc._html import html_util
        from apysc._validation import string_validation

        global _current_stage
        expression_data_util.empty_expression()
        self._variable_name_suffix = variable_name_suffix
        self.stage = self
        self._stage_elem_id = self._create_stage_elem_id_if_none(
            stage_elem_id=stage_elem_id
        )
        string_validation.validate_not_empty_string(string=self._stage_elem_id)
        self._save_stage_elem_id()
        self._stage_elem_id = html_util.remove_first_selector_symbol_char(
            str_val=self._stage_elem_id
        )
        self.variable_name = self._stage_elem_id.replace("-", "_")
        self._update_width_and_skip_appending_exp(value=ap.Int(stage_width))
        self._update_height_and_skip_appending_exp(value=ap.Int(stage_height))

        background_color = color_util.complement_hex_color(
            hex_color_code=background_color
        )
        self._background_color = background_color
        string_validation.validate_not_empty_string(string=add_to)
        self._add_to = add_to
        self._append_constructor_expression()

        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="children"
        )
        self._children = ap.Array([], variable_name_suffix=suffix)

        _save_stage_id_to_db(stage=self)
        _current_stage = self

    @final
    def _save_stage_elem_id(self) -> None:
        """
        Save the stage element id.
        """
        from apysc._expression import expression_data_util

        table_name: str = expression_data_util.TableName.STAGE_ELEM_ID.value
        query: str = f"DELETE FROM {table_name};"
        expression_data_util.exec_query(sql=query, commit=False)
        query = (
            f"INSERT INTO {table_name}(elem_id) " f"VALUES ('{self._stage_elem_id}');"
        )
        expression_data_util.exec_query(sql=query)

    @final
    def _create_stage_elem_id_if_none(self, *, stage_elem_id: Optional[str]) -> str:
        """
        Create a random stage element id if a specified id is None.

        Parameters
        ----------
        stage_elem_id : str or None
            Specified stage element id.

        Returns
        -------
        result_id : str
            If a specified id isn't None, this interface
            returns an unchanged argument value. Otherwise,
            this interface returns a random integer string.
        """
        if stage_elem_id is not None:
            return stage_elem_id
        now_timestamp: int = int(datetime.now().timestamp() * 1000)
        random_int: int = random.randint(1000000, 10000000)
        result_id: str = f"stage_{now_timestamp}{random_int}"
        return result_id

    @final
    def _append_constructor_expression(self) -> None:
        """
        Append stage constructor expression.
        """
        import apysc as ap

        expression: str = self._make_constructor_expression()
        ap.append_js_expression(expression=expression)

    @final
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
            f"\n{self.variable_name} = SVG()"
            f'.addTo("#{self._stage_elem_id}").size('
            f"\n  {self.width}, {self.height});"
        )
        return expression

    @final
    def _make_style_str(self) -> str:
        """
        Make a stage's style string.

        Returns
        -------
        style : str
            Result style string (width, height, etc.).
        """
        style: str = (
            f"width: {self.width}px;"
            f" height: {self.height}px;"
            f" background-color: {self._background_color};"
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

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage(
        ...     stage_width=500,
        ...     stage_height=300,
        ...     background_color="#333",
        ...     stage_elem_id="sales_chart",
        ... )
        >>> stage.stage_elem_id
        'sales_chart'
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
    Get a current stage's element id.

    Returns
    -------
    stage_elem_id : str
        Current stage's element id. If there is no
        instantiated stage yet, this interface returns
        a blank string.
    """
    from apysc._expression import expression_data_util

    table_name: str = expression_data_util.TableName.STAGE_ELEM_ID.value
    query: str = f"SELECT elem_id FROM {table_name} LIMIT 1;"
    expression_data_util.exec_query(sql=query)
    result: Optional[Tuple[str]] = expression_data_util.cursor.fetchone()
    if result is None:
        return ""
    return result[0]


def get_stage_elem_str() -> str:
    """
    Get a current stage's jQuery element string.

    Returns
    -------
    stage_elem_str : str
        Stage's jQuery element string (e.g., '$("#<stage_elem_id>")').
    """
    stage_elem_id: str = get_stage_elem_id()
    stage_elem_str: str = f'$("#{stage_elem_id}")'
    return stage_elem_str


def _save_stage_id_to_db(*, stage: Stage) -> None:
    """
    Save a stage's memory address (id) to the database.

    Parameters
    ----------
    stage : Stage
        Target stage.
    """
    from apysc._expression import expression_data_util

    table_name: str = expression_data_util.TableName.STAGE_ID.value
    query: str = f"DELETE FROM {table_name};"
    expression_data_util.exec_query(sql=query, commit=False)
    id_: int = id(stage)
    query = f"INSERT INTO {table_name}(stage_id) " f"VALUES ({id_});"
    expression_data_util.exec_query(sql=query)


class _StageNotCreatedError(Exception):
    pass


def get_stage() -> Stage:
    """
    Get an already instantiated stage instance.

    Returns
    -------
    stage : Stage
        Target stage instance.

    Raises
    ------
    _StageNotCreatedError
        If there is no instantiated stage yet.
    """
    from apysc._expression import expression_data_util

    table_name: str = expression_data_util.TableName.STAGE_ID.value
    query: str = f"SELECT stage_id FROM {table_name} LIMIT 1;"
    expression_data_util.exec_query(sql=query)
    result: Optional[Tuple[int]] = expression_data_util.cursor.fetchone()
    if result is None:
        raise _StageNotCreatedError(
            "Stage is not instantiated yet. Please instantiate the "
            "ap.Stage class before calling this function."
        )
    stage: Stage = ctypes.cast(result[0], ctypes.py_object).value
    return stage

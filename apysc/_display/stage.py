# pyright: reportGeneralTypeIssues=false

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
from typing import cast

from typing_extensions import final

from apysc._color.color import Color
from apysc._color.colors import Colors
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
    ...     background_color=ap.Color("#333"),
    ...     stage_elem_id="sales_chart",
    ... )
    """

    _background_color: Color
    _add_to: str
    _stage_elem_id: str
    stage: "Stage"

    @arg_validation_decos.is_builtin_integer(arg_position_index=1)
    @arg_validation_decos.is_builtin_integer(arg_position_index=2)
    @arg_validation_decos.is_color(arg_position_index=3, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=4, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=5, optional=True)
    @arg_validation_decos.is_builtin_string(arg_position_index=6, optional=False)
    def __init__(
        self,
        *,
        stage_width: int = 300,
        stage_height: int = 185,
        background_color: Color = Colors.WHITE_FFFFFF,
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
        background_color : str, default Colors.WHITE_FFFFFF
            Hexadecimal background color string.
        add_to : str, default 'body'
            Specification of element to add stage.
            Unique tag (e.g., 'body') or ID selector
            (e.g., '#any-unique-elem') is acceptable.
        stage_elem_id : str or None, optional
            ID attribute set to stage HTML element (e.g., 'line-graph').
            If None is set, a random integer will be applied.
        variable_name_suffix : str, default ""
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
        ...     background_color=ap.Color("#333"),
        ...     stage_elem_id="sales_chart",
        ... )
        """
        from apysc._expression import expression_data_util
        from apysc._html import html_util
        from apysc._type.array import Array
        from apysc._type.int import Int
        from apysc._validation import string_validation

        global _current_stage
        expression_data_util.empty_expression()
        _save_stage_id_to_db(stage=self)
        expression_data_util.copy_expression_before_stage_instantiation()
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
        self._update_width_and_skip_appending_exp(value=Int(stage_width))
        self._update_height_and_skip_appending_exp(value=Int(stage_height))

        self._background_color = background_color
        string_validation.validate_not_empty_string(string=add_to)
        self._add_to = add_to
        self._append_constructor_expression()

        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="children"
        )
        self._children = Array([], variable_name_suffix=suffix)
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
        from apysc._expression import expression_data_util

        expression: str = self._make_constructor_expression()
        expression_data_util.append_js_expression(expression=expression)

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
            f" background-color: {self._background_color._value};"
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
        ...     background_color=ap.Color("#333"),
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
            (e.g., `Stage("<stage_elem_id>")`).
        """
        repr_str: str = f'{Stage.__name__}("{self.stage_elem_id}")'
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


class StageNotCreatedError(Exception):
    pass


def _read_stage_id_from_db() -> Optional[int]:
    """
    Read a stage id from a database.

    Returns
    -------
    Optional[int]
        A stage id. If a created stage doesn't exist, this interface
        returns None.
    """
    from apysc._expression import expression_data_util

    table_name: str = expression_data_util.TableName.STAGE_ID.value
    query: str = f"SELECT stage_id FROM {table_name} LIMIT 1;"
    expression_data_util.exec_query(sql=query)
    result: Optional[Tuple[int]] = expression_data_util.cursor.fetchone()
    if result is None:
        return None
    return result[0]


def get_stage() -> Stage:
    """
    Get an already instantiated stage instance.

    Returns
    -------
    stage : Stage
        Target stage instance.

    Raises
    ------
    StageNotCreatedError
        If there is no instantiated stage yet.
    """
    stage_id: Optional[int] = _read_stage_id_from_db()
    if stage_id is None:
        raise StageNotCreatedError(
            "Stage is not instantiated yet. Please instantiate the "
            "ap.Stage class before calling this function."
        )
    stage: Stage = cast(Stage, ctypes.cast(stage_id, ctypes.py_object).value)
    return stage


_is_stage_created: bool = False


def is_stage_created() -> bool:
    """
    Get a boolean whether a created stage exists or not.

    Returns
    -------
    result : bool
        If a created stage exists, this interface returns True.
    """
    global _is_stage_created
    if _is_stage_created:
        return True

    stage_id: Optional[int] = _read_stage_id_from_db()
    if stage_id is None:
        return False
    _is_stage_created = True
    return True

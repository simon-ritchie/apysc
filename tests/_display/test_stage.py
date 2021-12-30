from random import randint
from typing import Any, Optional, Tuple
from typing import Dict

from retrying import retry

import apysc as ap
from apysc._display import stage
from apysc._display.display_object import DisplayObject
from apysc._expression import expression_data_util
from tests import testing_helper
from tests.testing_helper import assert_raises


class TestStage:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        stage: ap.Stage = ap.Stage(
            stage_width=500,
            stage_height=300,
            background_color='#000000',
            add_to='#line-graph',
            stage_elem_id='line-graph-stage')
        expected_attrs: Dict[str, Any] = {
            'width': 500,
            'height': 300,
            '_background_color': '#000000',
            '_add_to': '#line-graph',
            '_stage_elem_id': 'line-graph-stage',
            '_children': [],
        }
        testing_helper.assert_attrs(
            expected_attrs=expected_attrs, any_obj=stage)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_constructor_expression(self) -> None:
        stage: ap.Stage = ap.Stage(
            stage_width=100, stage_height=200,
            background_color='#333333',
            add_to='#line-graph',
            stage_elem_id='line-graph-stage')
        expression: str = stage._make_constructor_expression()
        style: str = stage._make_style_str()
        expected_str: str = (
            'var stage_html = \'<div id="line-graph-stage"'
            f' style="{style}"></div>\';'
            '\n$("#line-graph").append(stage_html);'
            '\nline_graph_stage = SVG().addTo("#line-graph-stage").size('
            '\n  100, 200);'
        )
        assert expression == expected_str

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__create_stage_elem_id_if_none(self) -> None:
        stage: ap.Stage = ap.Stage()
        result_id: str = stage._create_stage_elem_id_if_none(
            stage_elem_id='line-graph')
        assert result_id == 'line-graph'

        result_id_1: str = stage._create_stage_elem_id_if_none(
            stage_elem_id=None)
        assert result_id_1.startswith('stage_')
        assert result_id_1.replace('stage_', '').isdigit()
        result_id_2: str = stage._create_stage_elem_id_if_none(
            stage_elem_id=None)
        assert result_id_1 != result_id_2

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_style_str(self) -> None:
        stage: ap.Stage = ap.Stage(
            stage_width=200, stage_height=300, background_color='#333')
        style: str = stage._make_style_str()
        expected_style: str = (
            'width: 200px; height: 300px; background-color: #333333;'
        )
        assert style == expected_style

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_constructor_expression(self) -> None:
        stage: ap.Stage = ap.Stage()
        expected_expression: str = stage._make_constructor_expression()
        expected_expression = expected_expression.strip()
        saved_expression: str = expression_data_util.get_current_expression()
        saved_expression = saved_expression.strip()
        for expected_expression_line in expected_expression.splitlines():
            assert expected_expression_line in saved_expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_stage_elem_id(self) -> None:
        stage: ap.Stage = ap.Stage(stage_elem_id='#line-graph')
        assert stage.stage_elem_id == 'line-graph'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_add_child(self) -> None:
        stage: ap.Stage = ap.Stage()
        display_object: DisplayObject = DisplayObject(
            stage=stage, variable_name='test_display_object_1')
        stage.add_child(child=display_object)
        assert stage._children == ap.Array([display_object])

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__save_stage_elem_id(self) -> None:
        ap.Stage(stage_elem_id='line-graph')
        stage_elem_id: str = stage.get_stage_elem_id()
        assert stage_elem_id == 'line-graph'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___repr__(self) -> None:
        stage_: ap.Stage = ap.Stage(stage_elem_id='stage_1')
        repr_str: str = repr(stage_)
        assert repr_str == "Stage('stage_1')"


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_stage_elem_id() -> None:
    expression_data_util.empty_expression()
    stage_elem_id: str = stage.get_stage_elem_id()
    assert stage_elem_id == ''

    ap.Stage(stage_elem_id='line-graph')
    stage_elem_id = stage.get_stage_elem_id()
    assert stage_elem_id == 'line-graph'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_stage_variable_name() -> None:
    ap.Stage(stage_elem_id='line-graph')
    stage_variable_name: str = stage.get_stage_variable_name()
    assert stage_variable_name == 'line_graph'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_stage_elem_str() -> None:
    stage_: ap.Stage = ap.Stage()
    stage_elem_str: str = stage.get_stage_elem_str()
    expected: str = f'$("#{stage_.stage_elem_id}")'
    assert stage_elem_str == expected


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_stage() -> None:
    stage_: ap.Stage = ap.Stage()
    restored_stage: ap.Stage = stage.get_stage()
    assert stage_ == restored_stage

    table_name: str = expression_data_util.TableName.STAGE_ID.value
    query: str = f'DELETE FROM {table_name};'
    expression_data_util.exec_query(sql=query)
    assert_raises(
        expected_error_class=stage._StageNotCreatedError,
        func_or_method=stage.get_stage)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__save_stage_id_to_db() -> None:
    stage_: ap.Stage = ap.Stage()
    table_name: str = expression_data_util.TableName.STAGE_ID.value
    query: str = f'SELECT stage_id FROM {table_name} LIMIT 1;'
    expression_data_util.exec_query(sql=query)
    result: Optional[Tuple[int]] = expression_data_util.cursor.fetchone()
    if result is None:
        raise AssertionError('result value is None.')
    assert id(stage_) == result[0]

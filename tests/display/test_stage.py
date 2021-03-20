from random import randint
from typing import Any
from typing import Dict

from retrying import retry

from apyscript.display import Stage
from apyscript.display import stage
from apyscript.display.display_object import DisplayObject
from apyscript.display.stage import _STAGE_ELEM_ID_FILE_PATH
from apyscript.expression import expression_file_util
from apyscript.file import file_util
from apyscript.type import Array
from tests import testing_helper


class TestStage:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___init__(self) -> None:
        stage: Stage = Stage(
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
            '_childs': [],
        }
        testing_helper.assert_attrs(
            expected_attrs=expected_attrs, any_obj=stage)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__make_constructor_expression(self) -> None:
        stage: Stage = Stage(
            stage_width=100, stage_height=200,
            background_color='#333333',
            add_to='#line-graph',
            stage_elem_id='line-graph-stage')
        expression: str = stage._make_constructor_expression()
        style: str = stage._make_style_str()
        expected_str: str = (
            '<script type="text/javascript">'
            '\nvar stage_html = \'<div id="line-graph-stage"'
            f' style="{style}"></div>\';'
            '\n$("#line-graph").append(stage_html);'
            '\nline_graph_stage = SVG().addTo("#line-graph-stage").size('
            '\n  100, 200);'
            '\n</script>'
        )
        assert expression == expected_str

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__create_stage_elem_id_if_none(self) -> None:
        stage: Stage = Stage()
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

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__make_style_str(self) -> None:
        stage: Stage = Stage(
            stage_width=200, stage_height=300, background_color='#333')
        style: str = stage._make_style_str()
        expected_style: str = (
            'width: 200px; height: 300px; background-color: #333333;'
        )
        assert style == expected_style

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_constructor_expression(self) -> None:
        stage: Stage = Stage()
        expected_expression: str = stage._make_constructor_expression()
        expected_expression = expected_expression.strip()
        with open(expression_file_util.EXPRESSION_FILE_PATH, 'r') as f:
            saved_expression: str = f.read()
        saved_expression = saved_expression.strip()
        for expected_expression_line in expected_expression.splitlines():
            assert expected_expression_line in saved_expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_stage_elem_id(self) -> None:
        stage: Stage = Stage(stage_elem_id='#line-graph')
        assert stage.stage_elem_id == 'line-graph'

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_add_child(self) -> None:
        stage: Stage = Stage()
        display_object: DisplayObject = DisplayObject(
            stage=stage, variable_name='test_display_object_1')
        stage.add_child(child=display_object)
        assert stage._childs == Array([display_object])

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__save_stage_elem_id_to_expression_file(self) -> None:
        Stage(stage_elem_id='line-graph')
        stage_elem_id: str = file_util.read_txt(
            file_path=_STAGE_ELEM_ID_FILE_PATH)
        assert stage_elem_id == 'line-graph'


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test_get_stage_element_id() -> None:
    file_util.remove_file_if_exists(file_path=_STAGE_ELEM_ID_FILE_PATH)
    stage_elem_id: str = stage.get_stage_element_id()
    assert stage_elem_id == ''

    Stage(stage_elem_id='line-graph')
    stage_elem_id = stage.get_stage_element_id()
    assert stage_elem_id == 'line-graph'


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test_get_stage_variable_name() -> None:
    Stage(stage_elem_id='line-graph')
    stage_variable_name: str = stage.get_stage_variable_name()
    assert stage_variable_name == 'line_graph'

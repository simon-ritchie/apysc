from typing import Any
from typing import Dict
from typing import Optional
from typing import Tuple

import apysc as ap
from apysc._display import stage
from apysc._display.any_display_object import AnyDisplayObject
from apysc._expression import expression_data_util
from apysc._testing import testing_helper
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises


class TestStage:
    @apply_test_settings()
    def test___init__(self) -> None:
        stage: ap.Stage = ap.Stage(
            stage_width=500,
            stage_height=300,
            background_color=ap.Color("#000000"),
            add_to="#line-graph",
            stage_elem_id="line-graph-stage",
            variable_name_suffix="test_stage",
        )
        expected_attrs: Dict[str, Any] = {
            "width": 500,
            "height": 300,
            "_background_color": ap.Color("#000000"),
            "_add_to": "#line-graph",
            "_stage_elem_id": "line-graph-stage",
            "_children": [],
            "_variable_name_suffix": "test_stage",
        }
        testing_helper.assert_attrs(expected_attrs=expected_attrs, any_obj=stage)
        assert stage._children._variable_name_suffix == "test_stage__children"

    @apply_test_settings()
    def test__make_constructor_expression(self) -> None:
        stage: ap.Stage = ap.Stage(
            stage_width=100,
            stage_height=200,
            background_color=ap.Color("#333333"),
            add_to="#line-graph",
            stage_elem_id="line-graph-stage",
        )
        expression: str = stage._make_constructor_expression()
        style: str = stage._make_style_str()
        expected_str: str = (
            'var stage_html = \'<div id="line-graph-stage"'
            f' style="{style}"></div>\';'
            '\n$("#line-graph").append(stage_html);'
            '\nline_graph_stage = SVG().addTo("#line-graph-stage").size('
            "\n  100, 200);"
        )
        assert expression == expected_str

    @apply_test_settings()
    def test__create_stage_elem_id_if_none(self) -> None:
        stage: ap.Stage = ap.Stage()
        result_id: str = stage._create_stage_elem_id_if_none(stage_elem_id="line-graph")
        assert result_id == "line-graph"

        result_id_1: str = stage._create_stage_elem_id_if_none(stage_elem_id=None)
        assert result_id_1.startswith("stage_")
        assert result_id_1.replace("stage_", "").isdigit()
        result_id_2: str = stage._create_stage_elem_id_if_none(stage_elem_id=None)
        assert result_id_1 != result_id_2

    @apply_test_settings()
    def test__make_style_str(self) -> None:
        color: ap.Color = ap.Color("#333")
        stage: ap.Stage = ap.Stage(
            stage_width=200, stage_height=300, background_color=color
        )
        style: str = stage._make_style_str()
        expected_style: str = "width: 200px; height: 300px; background-color: #333333;"
        assert style == expected_style

    @apply_test_settings()
    def test__append_constructor_expression(self) -> None:
        stage: ap.Stage = ap.Stage()
        expected_expression: str = stage._make_constructor_expression()
        expected_expression = expected_expression.strip()
        saved_expression: str = expression_data_util.get_current_expression()
        saved_expression = saved_expression.strip()
        for expected_expression_line in expected_expression.splitlines():
            assert expected_expression_line in saved_expression

    @apply_test_settings()
    def test_stage_elem_id(self) -> None:
        stage: ap.Stage = ap.Stage(stage_elem_id="#line-graph")
        assert stage.stage_elem_id == "line-graph"

    @apply_test_settings()
    def test_add_child(self) -> None:
        stage: ap.Stage = ap.Stage()
        display_object: AnyDisplayObject = AnyDisplayObject()
        stage.add_child(child=display_object)
        assert stage._children == ap.Array([display_object])

    @apply_test_settings()
    def test__save_stage_elem_id(self) -> None:
        ap.Stage(stage_elem_id="line-graph")
        stage_elem_id: str = stage.get_stage_elem_id()
        assert stage_elem_id == "line-graph"

    @apply_test_settings()
    def test___repr__(self) -> None:
        stage_: ap.Stage = ap.Stage(stage_elem_id="stage_1")
        repr_str: str = repr(stage_)
        assert repr_str == 'Stage("stage_1")'


@apply_test_settings()
def test_get_stage_elem_id() -> None:
    expression_data_util.empty_expression()
    stage_elem_id: str = stage.get_stage_elem_id()
    assert stage_elem_id == ""

    ap.Stage(stage_elem_id="line-graph")
    stage_elem_id = stage.get_stage_elem_id()
    assert stage_elem_id == "line-graph"


@apply_test_settings()
def test_get_stage_elem_str() -> None:
    stage_: ap.Stage = ap.Stage()
    stage_elem_str: str = stage.get_stage_elem_str()
    expected: str = f'$("#{stage_.stage_elem_id}")'
    assert stage_elem_str == expected


@apply_test_settings()
def test_get_stage() -> None:
    stage_: ap.Stage = ap.Stage()
    restored_stage: ap.Stage = stage.get_stage()
    assert stage_ == restored_stage

    table_name: str = expression_data_util.TableName.STAGE_ID.value
    query: str = f"DELETE FROM {table_name};"
    expression_data_util.exec_query(sql=query)
    assert_raises(
        expected_error_class=stage.StageNotCreatedError, callable_=stage.get_stage
    )


@apply_test_settings()
def test__save_stage_id_to_db() -> None:
    stage_: ap.Stage = ap.Stage()
    table_name: str = expression_data_util.TableName.STAGE_ID.value
    query: str = f"SELECT stage_id FROM {table_name} LIMIT 1;"
    expression_data_util.exec_query(sql=query)
    result: Optional[Tuple[int]] = expression_data_util.cursor.fetchone()
    if result is None:
        raise AssertionError("result value is None.")
    assert id(stage_) == result[0]


@apply_test_settings()
def test__read_stage_id_from_db() -> None:
    expression_data_util.empty_expression()
    stage_id: Optional[int] = stage._read_stage_id_from_db()
    assert stage_id is None

    ap.Stage(stage_elem_id="test_stage")
    stage_id = stage._read_stage_id_from_db()
    assert stage_id is not None


@apply_test_settings()
def test_is_stage_created() -> None:
    expression_data_util.empty_expression()
    stage._is_stage_created = False
    result: bool = stage.is_stage_created()
    assert not result

    ap.Stage(stage_elem_id="test_stage")
    result = stage.is_stage_created()
    assert result

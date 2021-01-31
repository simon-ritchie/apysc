import os
from typing import Any, Dict

from apyscript.display import stage
from apyscript.display.stage import Stage
from apyscript.expression import file_util
from tests import testing_helper


class TestStage:

    def test___init__(self) -> None:
        test_scope_file_path: str = file_util.get_scope_file_path_from_scope(
            scope='test')
        testing_helper.make_blank_file(file_path=test_scope_file_path)
        stage: Stage = Stage(
            stage_width=500,
            stage_height=300,
            background_color='#000000')
        assert not os.path.exists(test_scope_file_path)

        expected_attrs: Dict[str, Any] = {
            '_stage_width': 500,
            '_stage_height': 300,
            '_background_color': '#000000',
        }
        testing_helper.assert_attrs(
            expected_attrs=expected_attrs, any_obj=stage)

    def test_stage_width(self) -> None:
        stage: Stage = Stage(stage_width=500)
        assert stage.stage_width == 500

        stage.stage_width = 600
        assert stage.stage_width == 600

    def test_stage_height(self) -> None:
        stage: Stage = Stage(stage_height=300)
        assert stage.stage_height == 300

        stage.stage_height = 400
        assert stage.stage_height == 400

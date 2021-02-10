from retrying import retry

from apyscript.display.display_object import DisplayObject
from apyscript.display.stage import Stage
from tests import testing_helper


class TestDisplayObject:

    @retry(stop_max_attempt_number=5, wait_fixed=300)
    def test___init__(self) -> None:
        stage: Stage = Stage()
        display_object: DisplayObject = DisplayObject(
            stage=stage, variable_name='test_display_object')
        testing_helper.assert_attrs(
            expected_attrs={
                'stage': stage,
                '_stage_cls': Stage,
            },
            any_obj=display_object)

    @retry(stop_max_attempt_number=5, wait_fixed=300)
    def test_variable_name(self) -> None:
        stage: Stage = Stage()
        display_object: DisplayObject = DisplayObject(
            stage=stage, variable_name='test_display_object_1')
        display_object.variable_name = 'test_display_object_2'
        assert display_object.variable_name == 'test_display_object_2'

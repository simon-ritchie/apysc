from retrying import retry

from apyscript.display import display_object
from apyscript.display.display_object import DisplayObject
from apyscript.display.stage import Stage
from tests import testing_helper


class TestDisplayObject:

    @retry(stop_max_attempt_number=5, wait_fixed=300)
    def test___init__(self) -> None:
        stage: Stage = Stage()
        display_object: DisplayObject = DisplayObject(stage=stage)
        testing_helper.assert_attrs(
            expected_attrs={
                'stage': stage,
                '_stage_cls': Stage,
            },
            any_obj=display_object)

    @retry(stop_max_attempt_number=5, wait_fixed=300)
    def test_add_child(self) -> None:
        stage: Stage = Stage()
        display_object: DisplayObject = DisplayObject(stage=stage)
        child: DisplayObject = DisplayObject(stage=stage)
        display_object.add_child(child=child)
        assert display_object._childs == [child]

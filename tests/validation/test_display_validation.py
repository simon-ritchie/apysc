from random import randint

from retrying import retry

from apyscript.validation import display_validation
from apyscript.display.stage import Stage
from apyscript.display.sprite import Sprite
from apyscript.display.display_object import DisplayObject
from tests import testing_helper


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test_validate_stage() -> None:
    stage: Stage = Stage()
    display_validation.validate_stage(stage=stage)
    sprite: Sprite = Sprite(stage=stage)
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=display_validation.validate_stage,
        kwargs={'stage': sprite})


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test_validate_display_object() -> None:
    stage: Stage = Stage()
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=display_validation.validate_display_object,
        kwargs={'display_object': stage})

    sprite: Sprite = Sprite(stage=stage)
    display_validation.validate_display_object(display_object=sprite)

    display_object: DisplayObject = DisplayObject(
        stage=stage, variable_name='test_display_object')
    display_validation.validate_display_object(display_object=display_object)

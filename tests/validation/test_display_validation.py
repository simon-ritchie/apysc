from random import randint

from retrying import retry

from apyscript.validation import display_validation
from apyscript.display.stage import Stage
from apyscript.display.sprite import Sprite
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

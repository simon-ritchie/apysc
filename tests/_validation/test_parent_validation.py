from random import randint

from retrying import retry

import apysc as ap
from apysc._testing import testing_helper
from apysc._validation import parent_validation


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_parent_contains_chils() -> None:
    stage: ap.Stage = ap.Stage()
    sprite_1: ap.Sprite = ap.Sprite()
    parent_validation.validate_parent_contains_child(parent=stage, child=sprite_1)

    sprite_2: ap.Sprite = ap.Sprite()
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=parent_validation.validate_parent_contains_child,
        parent=sprite_1,
        child=sprite_2,
    )

    parent_validation.validate_parent_contains_child(parent=None, child=sprite_2)
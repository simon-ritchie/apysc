from random import randint

from retrying import retry

import apysc as ap
from apysc._testing import testing_helper
from apysc._validation import parent_validation
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
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

from random import randint

from retrying import retry

from apyscript.validation import parent_validation
from apyscript.display.stage import Stage
from tests import testing_helper


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test_validate_parent_instance() -> None:
    parent_validation.validate_parent_instance(parent=None)
    stage: Stage = Stage()
    parent_validation.validate_parent_instance(parent=stage)
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=parent_validation.validate_parent_instance,
        kwargs={
            'parent': 100,
        })

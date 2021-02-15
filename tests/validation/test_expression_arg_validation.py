from random import randint
from typing import List, Type

from retrying import retry

from apyscript.validation import expression_arg_validation
from tests import testing_helper
from apyscript.display.sprite import Sprite
from apyscript.display.stage import Stage


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test__validate_args() -> None:
    acceptable_arg_types: List[Type] = [Stage, Sprite]
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=expression_arg_validation._validate_args,
        kwargs={
            'args': [100],
            'acceptable_arg_types': acceptable_arg_types,
        })

    stage: Stage = Stage()
    expression_arg_validation._validate_args(
        args=[stage], acceptable_arg_types=acceptable_arg_types)

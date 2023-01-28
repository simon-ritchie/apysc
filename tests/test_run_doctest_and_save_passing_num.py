from random import randint

from retrying import retry

import scripts.run_doctest_and_save_passing_num as mod
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test__get_passing_test_num_from_stdout() -> None:
    stdout: str = (
        "apysc/_type/int.py::apysc._type.int.Int.__init__ PASSEDPASSED"
        "\napysc/_type/boolean.py::apysc._type.boolean.Boolean."
        "not_ PASSEDPASSED"
        "\napysc/_type/number_value_mixin.py::apysc._type."
        "number_value_mixin.NumberValueMixIn.value PASSEDPASSED"
        "\napysc/_type/number.py::apysc._type.number.Number.__init__ PASSED"
        "\n"
        "\n================================================== 25 "
        "passed in 2.10s ========================================="
        "========="
    )
    passing_test_num: str = mod._get_passing_test_num_from_stdout(stdout=stdout)
    assert passing_test_num == "25"

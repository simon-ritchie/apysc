from random import randint

from retrying import retry

import scripts.run_doctest_and_save_passing_num as \
    run_doctest_and_save_passing_num


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_passing_test_num_from_stdout() -> None:
    stdout: str = (
        'apysc/_type/int.py::apysc._type.int.Int.__init__ PASSEDPASSED'
        '\napysc/_type/boolean.py::apysc._type.boolean.Boolean.'
        'not_ PASSEDPASSED'
        '\napysc/_type/number_value_interface.py::apysc._type.'
        'number_value_interface.NumberValueInterface.value PASSEDPASSED'
        '\napysc/_type/number.py::apysc._type.number.Number.__init__ PASSED'
        '\n'
        '\n================================================== 25 '
        'passed in 2.10s ========================================='
        '========='
    )
    passing_test_num: str = run_doctest_and_save_passing_num.\
        _get_passing_test_num_from_stdout(stdout=stdout)
    assert passing_test_num == '25'

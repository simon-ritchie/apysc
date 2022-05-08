from random import randint
import os

from retrying import retry

from apysc._testing import testing_helper
from apysc._file import file_util


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_make_blank_file() -> None:
    file_path: str = './tmp/tmp_test_testing_helper.txt'
    file_util.remove_file_if_exists(file_path=file_path)

    testing_helper.make_blank_file(file_path=file_path)
    assert os.path.isfile(file_path)
    txt: str = file_util.read_txt(file_path=file_path)
    assert txt == ''

    file_util.remove_file_if_exists(file_path=file_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__assert_has_attr() -> None:

    class _TestClass:

        a: int = 10

    test_instance: _TestClass = _TestClass()
    testing_helper._assert_has_attr(
        any_obj=test_instance, attr_name='a')

    testing_helper.assert_raises(
        expected_error_class=AssertionError,
        func_or_method=testing_helper._assert_has_attr,
        kwargs={'any_obj': test_instance, 'attr_name': 'b'},
        match='Expected attribute does not exists.')

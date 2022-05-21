import os
from random import randint

from retrying import retry

from apysc._file import file_util
from apysc._testing import testing_helper


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
        callable_=testing_helper._assert_has_attr,
        kwargs={'any_obj': test_instance, 'attr_name': 'b'},
        match='Expected attribute does not exists.')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_assert_attrs() -> None:

    class _TestClass:

        a: int = 10
        b: str = ''

    test_instance: _TestClass = _TestClass()
    testing_helper.assert_attrs(
        expected_attrs={'a': 10, 'b': ''},
        any_obj=test_instance)

    testing_helper.assert_raises(
        expected_error_class=AssertionError,
        callable_=testing_helper.assert_attrs,
        kwargs={
            'expected_attrs': {'c': 20},
            'any_obj': test_instance,
        },
        match='Expected attribute does not exists.')

    testing_helper.assert_raises(
        expected_error_class=AssertionError,
        callable_=testing_helper.assert_attrs,
        kwargs={
            'expected_attrs': {'a': 20},
            'any_obj': test_instance,
        },
        match='Attribute value is different from expected value.')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_assert_raises() -> None:

    def _test_func_1() -> None:
        raise ValueError('Test error!')

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func_1,
        match='Test error!')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_assert_attrs_type() -> None:

    class _TestClass:

        a: int = 10
        b: str = ''

    test_instance: _TestClass = _TestClass()
    testing_helper.assert_attrs_type(
        expected_types={
            'a': int,
            'b': str,
        },
        any_obj=test_instance)

    testing_helper.assert_raises(
        expected_error_class=AssertionError,
        callable_=testing_helper.assert_attrs_type,
        kwargs={
            'expected_types': {'a': int, 'b': int},
            'any_obj': test_instance,
        },
        match='Attribute type is different from expected type.')

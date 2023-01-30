import os

from apysc._file import file_util
from apysc._testing import testing_helper
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test_make_blank_file() -> None:
    file_path: str = "./tmp/tmp_test_testing_helper.txt"
    file_util.remove_file_if_exists(file_path=file_path)

    testing_helper.make_blank_file(file_path=file_path)
    assert os.path.isfile(file_path)
    txt: str = file_util.read_txt(file_path=file_path)
    assert txt == ""

    file_util.remove_file_if_exists(file_path=file_path)


@apply_test_settings()
def test__assert_has_attr() -> None:
    class _TestClass:

        a: int = 10

    test_instance: _TestClass = _TestClass()
    testing_helper._assert_has_attr(any_obj=test_instance, attr_name="a")

    testing_helper.assert_raises(
        expected_error_class=AssertionError,
        callable_=testing_helper._assert_has_attr,
        match="Expected attribute does not exists.",
        any_obj=test_instance,
        attr_name="b",
    )


@apply_test_settings()
def test_assert_attrs() -> None:
    class _TestClass:

        a: int = 10
        b: str = ""

    test_instance: _TestClass = _TestClass()
    testing_helper.assert_attrs(
        expected_attrs={"a": 10, "b": ""}, any_obj=test_instance
    )

    testing_helper.assert_raises(
        expected_error_class=AssertionError,
        callable_=testing_helper.assert_attrs,
        expected_attrs={"c": 20},
        any_obj=test_instance,
        match="Expected attribute does not exists.",
    )

    testing_helper.assert_raises(
        expected_error_class=AssertionError,
        callable_=testing_helper.assert_attrs,
        expected_attrs={"a": 20},
        any_obj=test_instance,
        match="Attribute value is different from expected value.",
    )


@apply_test_settings()
def test_assert_raises() -> None:
    def _test_func_1() -> None:
        raise ValueError("Test error!")

    testing_helper.assert_raises(
        expected_error_class=ValueError, callable_=_test_func_1, match="Test error!"
    )


@apply_test_settings()
def test_assert_attrs_type() -> None:
    class _TestClass:

        a: int = 10
        b: str = ""

    test_instance: _TestClass = _TestClass()
    testing_helper.assert_attrs_type(
        expected_types={
            "a": int,
            "b": str,
        },
        any_obj=test_instance,
    )

    testing_helper.assert_raises(
        expected_error_class=AssertionError,
        callable_=testing_helper.assert_attrs_type,
        match="Attribute type is different from expected type.",
        expected_types={"a": int, "b": int},
        any_obj=test_instance,
    )


_count: int = 0


@apply_test_settings()
def test_apply_test_settings() -> None:
    global _count
    _count = 0

    @testing_helper.apply_test_settings(
        retrying_max_attempts_num=2,
        retrying_sleep_seconds=0.001,
    )
    def test_func_1(*, value: int) -> None:
        global _count
        _count += 1

        raise ValueError()

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=test_func_1,
        value=10,
    )
    assert _count == 3

    @testing_helper.apply_test_settings(retrying_max_attempts_num=2)
    def test_func_2(*, value: int) -> int:
        return value

    result: int = test_func_2(value=10)
    assert result == 10


@apply_test_settings()
def test__validate_retrying_sleep_seconds() -> None:
    """_validate_retrying_sleep_seconds 関数のテスト。"""
    testing_helper._validate_retrying_sleep_seconds(retrying_sleep_seconds=10)

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=testing_helper._validate_retrying_sleep_seconds,
        retrying_sleep_seconds=10.1,
    )

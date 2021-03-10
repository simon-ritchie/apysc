from random import randint
from typing import Any, Dict, List

from retrying import retry

from apyscript.type import Array
from tests import testing_helper


class TestArray:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___init__(self) -> None:
        array_1: Array = Array((1, 2, 3))
        expected_attrs: Dict[str, Any] = {
            '_initial_value': (1, 2, 3),
            '_value': [1, 2, 3],
            '_type_name': 'array',
        }
        testing_helper.assert_attrs(
            expected_attrs=expected_attrs,
            any_obj=array_1)
        assert array_1.variable_name.startswith('array_')

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__validate_acceptable_value_type(self) -> None:
        array_1: Array = Array([1, 2, 3])
        _: Array = Array((1, 2, 3))
        _: Array = Array(array_1)

        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=Array,
            kwargs={'value': 100})

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__get_list_value(self) -> None:
        array_1: Array = Array([1, 2, 3])
        list_val: List[Any] = array_1._get_list_value(value=[4, 5, 6])
        assert list_val == [4, 5, 6]

        list_val = array_1._get_list_value(value=(7, 8, 9))
        assert list_val == [7, 8, 9]

        other_array: Array = Array([10, 11, 12])
        list_val = array_1._get_list_value(value=other_array)
        assert list_val == [10, 11, 12]

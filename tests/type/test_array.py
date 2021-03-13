from random import randint
from typing import Any, Dict, List

from retrying import retry

from apyscript.type import Array, Int
from apyscript.expression import expression_file_util
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

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_constructor_expression(self) -> None:
        expression_file_util.remove_expression_file()
        array_1: Array = Array([1, 2, 3])
        expression: str = expression_file_util.get_current_expression()
        expected: str = f'var {array_1.variable_name} = [1, 2, 3];'
        assert expected in expression

        array_2: Array = Array(array_1)
        expression = expression_file_util.get_current_expression()
        expected = f'var {array_2.variable_name} = {array_1.variable_name}'
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_value_setter_expression(self) -> None:
        expression_file_util.remove_expression_file()
        array_1: Array = Array([1, 2, 3])
        array_1.value = [4, 5, 6]
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{array_1.variable_name} = [4, 5, 6];'
        )
        assert expected in expression

        array_2: Array = Array(array_1)
        expression = expression_file_util.get_current_expression()
        expected = f'{array_2.variable_name} = {array_1.variable_name};'
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_value(self) -> None:
        array_1: Array = Array([1, 2, 3])
        array_1.value = [4, 5, 6]
        assert array_1.value == [4, 5, 6]

        array_2: Array = Array([7, 8, 9])
        array_2.value = array_1
        assert array_2.value == [4, 5, 6]

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_append(self) -> None:
        array_1: Array = Array([1, 2, 3])
        array_1.append(value=4)
        assert array_1.value == [1, 2, 3, 4]

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_push(self) -> None:
        array_1: Array = Array([1, 2, 3])
        array_1.push(value=4)
        assert array_1.value == [1, 2, 3, 4]

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_push_and_append_expression(self) -> None:
        expression_file_util.remove_expression_file()
        array_1: Array = Array([1, 2, 3])
        array_1.append(value=4)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{array_1.variable_name}.push(4);'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_extend(self) -> None:
        array_1: Array = Array([1, 2])
        array_1.extend(other_arr=[3, 4])
        assert array_1.value == [1, 2, 3, 4]
        array_2: Array = Array([5, 6])
        array_1.extend(other_arr=array_2)
        assert array_1.value == [1, 2, 3, 4, 5, 6]

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_extend_expression(self) -> None:
        expression_file_util.remove_expression_file()
        array_1: Array = Array([1, 2])
        array_1.extend(other_arr=[3, 4])
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{array_1.variable_name} = '
            f'{array_1.variable_name}.concat([3, 4]);'
        )
        assert expected in expression

        array_2: Array = Array([5, 6])
        array_1.extend(other_arr=array_2)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{array_1.variable_name} = '
            f'{array_1.variable_name}.concat({array_2.variable_name});'
        )
        assert expected in expression

    def test_concat(self) -> None:
        array_1: Array = Array([1, 2])
        array_2: Array = array_1.concat([3, 4])
        assert array_2.value == [1, 2, 3, 4]
        assert array_1.value == [1, 2]

    def test__append_concat_expression(self) -> None:
        expression_file_util.remove_expression_file()
        array_1: Array = Array([1, 2])
        array_2: Array = array_1.concat([3, 4])
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{array_2.variable_name} = '
            f'{array_1.variable_name}.concat([3, 4]);'
        )
        assert expected in expression

        array_3: Array = Array([5, 6])
        array_4: Array = array_1.concat(array_3)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{array_4.variable_name} = '
            f'{array_1.variable_name}.concat({array_3.variable_name});'
        )
        assert expected in expression

    def test_insert(self) -> None:
        array_1: Array = Array([1, 3])
        array_1.insert(index=1, value=2)
        assert array_1.value == [1, 2, 3]

    def test_insert_at(self) -> None:
        array_1: Array = Array([1, 3])
        array_1.insert_at(index=1, value=2)
        assert array_1.value == [1, 2, 3]

    def test__append_insert_expression(self) -> None:
        expression_file_util.remove_expression_file()
        array_1: Array = Array([1, 4])
        array_1.insert(index=1, value=2)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{array_1.variable_name}.splice(1, 0, 2);'
        )
        assert expected in expression

        index_1: Int = Int(2)
        value_1: Int = Int(3)
        array_1.insert(index=index_1, value=value_1)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{array_1.variable_name}.splice'
            f'({index_1.variable_name}, 0, {value_1.variable_name});'
        )
        assert expected in expression


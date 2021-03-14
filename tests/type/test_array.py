from random import randint
from typing import Any
from typing import Dict
from typing import List

import pytest
from retrying import retry

from apyscript.expression import expression_file_util
from apyscript.type import Array
from apyscript.type import Int
from apyscript.type import String
from apyscript.type import Number
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
        _ = Array(array_1)

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
        assert array_2.value == [4, 5, 6]  # type: ignore

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

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_concat(self) -> None:
        array_1: Array = Array([1, 2])
        array_2: Array = array_1.concat([3, 4])
        assert array_2.value == [1, 2, 3, 4]
        assert array_1.value == [1, 2]

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
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

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_insert(self) -> None:
        array_1: Array = Array([1, 3])
        array_1.insert(index=1, value=2)
        assert array_1.value == [1, 2, 3]

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_insert_at(self) -> None:
        array_1: Array = Array([1, 3])
        array_1.insert_at(index=1, value=2)
        assert array_1.value == [1, 2, 3]

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
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

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_pop(self) -> None:
        array_1: Array = Array([1, 2])
        value: int = array_1.pop()
        assert array_1.value == [1]
        assert value == 2

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_pop_expression(self) -> None:
        expression_file_util.remove_expression_file()
        int_1: Int = Int(2)
        array_1: Array = Array([1, int_1, 3])
        _: int = array_1.pop()
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{array_1.variable_name}.pop();'
        )
        assert expected in expression

        value_1: Int = array_1.pop()
        assert value_1.variable_name == int_1.variable_name
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{value_1.variable_name} = '
            f'{array_1.variable_name}.pop();'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_remove(self) -> None:
        array_1: Array = Array([1, 2, 3])
        array_1.remove(value=2)
        assert array_1.value == [1, 3]

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_remove_expression(self) -> None:
        expression_file_util.remove_expression_file()
        array_1: Array = Array([1, 2, 3])
        array_1.remove(2)
        expression: str = expression_file_util.get_current_expression()
        expected_strs: List[str] = [
            'var index_',
            f' = _.indexOf({array_1.variable_name}, 2);'
            f'\n{array_1.variable_name}.splice(',
            ', 1);'
        ]
        for expected_str in expected_strs:
            assert expected_str in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_remove_at(self) -> None:
        array_1: Array = Array([1, 2, 3, 4])
        array_1.remove_at(index=1)
        assert array_1.value == [1, 3, 4]
        array_1.remove_at(index=Int(1))
        assert array_1.value == [1, 4]

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_remove_at_expression(self) -> None:
        expression_file_util.remove_expression_file()
        array_1: Array = Array([1, 2, 3, 4])
        array_1.remove_at(index=1)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{array_1.variable_name}.splice(1, 1);'
        )
        assert expected in expression

        int_1: Int = Int(1)
        array_1.remove_at(index=int_1)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{array_1.variable_name}.splice({int_1.variable_name}, 1);'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_reverse(self) -> None:
        array_1: Array = Array([1, 2, 3])
        array_1.reverse()
        assert array_1.value == [3, 2, 1]

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_reverse_expression(self) -> None:
        expression_file_util.remove_expression_file()
        array_1: Array = Array([1, 2, 3])
        array_1.reverse()
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{array_1.variable_name}.reverse();'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_sort(self) -> None:
        array_1: Array = Array([3, 5, 1, 4, 2])
        array_1.sort()
        assert array_1.value == [1, 2, 3, 4, 5]

        array_2: Array = Array([3, 5, 1, 4, 2])
        array_2.sort(ascending=False)
        assert array_2.value == [5, 4, 3, 2, 1]

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_sort_expression(self) -> None:
        expression_file_util.remove_expression_file()
        array_1: Array = Array([3, 5, 1, 4, 2])
        array_1.sort()
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{array_1.variable_name}.sort();'
        )
        assert expected in expression
        assert 'reverse' not in expression

        expression_file_util.remove_expression_file()
        array_2: Array = Array([3, 5, 1, 4, 2])
        array_2.sort(ascending=False)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{array_2.variable_name}.sort();'
            f'\n{array_2.variable_name}.reverse();'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_slice(self) -> None:
        array_1: Array = Array([1, 2, 3, 4])
        array_2: Array = array_1.slice(start=1, end=3)
        assert array_2.value == [2, 3]

        array_3: Array = array_1.slice(start=1)
        assert array_3.value == [2, 3, 4]

        array_4: Array = array_1.slice(end=2)
        assert array_4.value == [1, 2]

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_slice_expression(self) -> None:
        expression_file_util.remove_expression_file()
        array_1: Array = Array([1, 2, 3, 4])
        array_2: Array = array_1.slice(start=1, end=3)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{array_2.variable_name} = '
            f'{array_1.variable_name}.slice(1, 3);'
        )
        assert expected in expression

        int_1: Int = Int(1)
        int_2: Int = Int(3)
        array_3: Array = array_1.slice(start=int_1, end=int_2)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{array_3.variable_name} = {array_1.variable_name}'
            f'.slice({int_1}, {int_2});'
        )
        assert expected in expression

        array_4: Array = array_1.slice(start=1)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{array_4.variable_name} = {array_1.variable_name}'
            '.slice(1);'
        )
        assert expected in expression

        array_5: Array = array_1.slice(end=2)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{array_5.variable_name} = {array_1.variable_name}'
            '.slice(0, 2);'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___getitem__(self) -> None:
        array_1: Array = Array([1, 2, 3])
        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=array_1.__getitem__,
            kwargs={'index': (0, 1)})

        value_1: int = array_1[1]
        assert value_1 == 2

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_getitem_expression(self) -> None:
        expression_file_util.remove_expression_file()
        int_1: Int = Int(3)
        array_1: Array = Array([1, 2, int_1])
        _: int = array_1[0]

        value_1: Int = array_1[2]
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{value_1.variable_name} = {array_1.variable_name}[2];'
        )
        assert expected in expression

        int_2: Int = Int(2)
        _ = array_1[int_2]
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{value_1.variable_name} = {array_1.variable_name}'
            f'[{int_2.variable_name}];'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__validate_index_type_is_int(self) -> None:
        array_1: Array = Array([1, 2])
        array_1._validate_index_type_is_int(index=1)
        array_1._validate_index_type_is_int(index=Int(1))
        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=array_1._validate_index_type_is_int,
            kwargs={'index': 'Hello!'})

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__get_builtin_int_from_index(self) -> None:
        array_1: Array = Array([1, 2])
        builtin_int_index: int = array_1._get_builtin_int_from_index(index=1)
        assert builtin_int_index == 1
        assert isinstance(builtin_int_index, int)

        builtin_int_index = array_1._get_builtin_int_from_index(index=Int(1))
        assert builtin_int_index == 1
        assert isinstance(builtin_int_index, int)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___setitem__(self) -> None:
        array_1: Array = Array([1, 2, 3])
        array_1[1] = 4
        assert array_1.value[1] == 4

        int_1: Int = Int(1)
        int_2: Int = Int(5)
        array_1[int_1] = int_2
        assert array_1.value[1] == 5
        assert isinstance(array_1.value[1], Int)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_setitem_expression(self) -> None:
        expression_file_util.remove_expression_file()
        array_1: Array = Array([1, 2, 3])
        array_1[1] = 4
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{array_1.variable_name}[1] = 4;'
        )
        assert expected in expression

        array_1[1] = 'Hello!'
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{array_1.variable_name}[1] = "Hello!";'
        )

        int_1: Int = Int(1)
        int_2: Int = Int(5)
        array_1[int_1] = int_2
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{array_1.variable_name}[{int_1.variable_name}] = '
            f'{int_2.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___delitem__(self) -> None:
        array_1: Array = Array([1, 2, 3])
        del array_1[1]
        assert array_1.value == [1, 3]

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_length(self) -> None:
        array_1: Array = Array([1, 2, 3])
        length: Int = array_1.length
        assert length == 3
        assert isinstance(length, Int)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_length_expression(self) -> None:
        expression_file_util.remove_expression_file()
        array_1: Array = Array([1, 2, 3])
        length: Int = array_1.length
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{length.variable_name} = {array_1.variable_name}.length;'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___len__(self) -> None:
        array_1: Array = Array([1, 2, 3])
        with pytest.raises(ValueError):  # type: ignore
            len(array_1)  # type: ignore

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_join(self) -> None:
        array_1: Array = Array(['1', String('2'), 3, Int(4)])
        joined: String = array_1.join(',')
        assert joined == '1,2,3,4'
        joined = array_1.join(String(','))
        assert joined == '1,2,3,4'

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_join_expression(self) -> None:
        expression_file_util.remove_expression_file()
        string_1: String = String('2')
        int_1: Int = Int(4)
        array_1: Array = Array(['1', string_1, 3, int_1])
        string_2: String = String(', ')
        joined: String = array_1.join(sep=string_2)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{joined.variable_name} = '
            f'{array_1.variable_name}.join({string_2.variable_name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___str__(self) -> None:
        array_1: Array = Array(
            ['1', 2, Int(3), Number(10.5)])
        string: str = str(array_1)
        assert string == "['1', 2, Int(3), Number(10.5)]"

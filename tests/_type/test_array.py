import re
from typing import Any
from typing import Dict
from typing import List
from typing import Match
from typing import Optional

import pytest

import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing import testing_helper
from apysc._testing.testing_helper import apply_test_settings


class TestArray:
    @apply_test_settings()
    def test___init__(self) -> None:
        array_1: ap.Array = ap.Array((1, 2, 3), variable_name_suffix="test_array")
        expected_attrs: Dict[str, Any] = {
            "_initial_value": (1, 2, 3),
            "_value": [1, 2, 3],
            "_type_name": var_names.ARRAY,
            "_variable_name_suffix": "test_array",
        }
        testing_helper.assert_attrs(expected_attrs=expected_attrs, any_obj=array_1)
        assert array_1.variable_name.startswith(f"{var_names.ARRAY}_")

    @apply_test_settings()
    def test__get_list_value(self) -> None:
        array_1: ap.Array = ap.Array([1, 2, 3])
        list_val: List[Any] = array_1._get_list_value(value=[4, 5, 6])
        assert list_val == [4, 5, 6]

        list_val = array_1._get_list_value(value=(7, 8, 9))
        assert list_val == [7, 8, 9]

        other_array: ap.Array = ap.Array([10, 11, 12])
        list_val = array_1._get_list_value(value=other_array)
        assert list_val == [10, 11, 12]

    @apply_test_settings()
    def test__append_constructor_expression(self) -> None:
        expression_data_util.empty_expression()
        array_1: ap.Array = ap.Array([1, 2, 3])
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"var {array_1.variable_name} = [1, 2, 3];"
        assert expected in expression

        array_2: ap.Array = ap.Array(array_1)
        expression = expression_data_util.get_current_expression()
        expected = f"var {array_2.variable_name} = {array_1.variable_name}"
        assert expected in expression

    @apply_test_settings()
    def test__append_value_setter_expression(self) -> None:
        expression_data_util.empty_expression()
        array_1: ap.Array = ap.Array([1, 2, 3])
        array_1.value = [4, 5, 6]
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{array_1.variable_name} = [4, 5, 6];"
        assert expected in expression

        array_2: ap.Array = ap.Array(array_1)
        expression = expression_data_util.get_current_expression()
        expected = f"{array_2.variable_name} = {array_1.variable_name};"
        assert expected in expression

    @apply_test_settings()
    def test_value(self) -> None:
        array_1: ap.Array = ap.Array([1, 2, 3])
        array_1.value = [4, 5, 6]
        assert array_1.value == [4, 5, 6]

        array_2: ap.Array = ap.Array([7, 8, 9])
        array_2.value = array_1
        assert array_2.value == [4, 5, 6]  # type: ignore

    @apply_test_settings()
    def test_append(self) -> None:
        array_1: ap.Array = ap.Array([1, 2, 3])
        array_1.append(value=4)
        assert array_1.value == [1, 2, 3, 4]

    @apply_test_settings()
    def test_push(self) -> None:
        array_1: ap.Array = ap.Array([1, 2, 3])
        array_1.push(value=4)
        assert array_1.value == [1, 2, 3, 4]

    @apply_test_settings()
    def test__append_push_and_append_expression(self) -> None:
        expression_data_util.empty_expression()
        array_1: ap.Array = ap.Array([1, 2, 3])
        array_1.append(value=4)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{array_1.variable_name}.push(4);"
        assert expected in expression

    @apply_test_settings()
    def test_extend(self) -> None:
        array_1: ap.Array = ap.Array([1, 2])
        array_1.extend(other_arr=[3, 4])
        assert array_1.value == [1, 2, 3, 4]
        array_2: ap.Array = ap.Array([5, 6])
        array_1.extend(other_arr=array_2)
        assert array_1.value == [1, 2, 3, 4, 5, 6]

    @apply_test_settings()
    def test__append_extend_expression(self) -> None:
        expression_data_util.empty_expression()
        array_1: ap.Array = ap.Array([1, 2])
        array_1.extend(other_arr=[3, 4])
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{array_1.variable_name} = " f"{array_1.variable_name}.concat([3, 4]);"
        )
        assert expected in expression

        array_2: ap.Array = ap.Array([5, 6])
        array_1.extend(other_arr=array_2)
        expression = expression_data_util.get_current_expression()
        expected = (
            f"{array_1.variable_name} = "
            f"{array_1.variable_name}.concat({array_2.variable_name});"
        )
        assert expected in expression

    @apply_test_settings()
    def test_concat(self) -> None:
        array_1: ap.Array = ap.Array([1, 2])
        array_2: ap.Array = array_1.concat([3, 4])
        assert array_2.value == [1, 2, 3, 4]
        assert array_1.value == [1, 2]

    @apply_test_settings()
    def test__append_concat_expression(self) -> None:
        expression_data_util.empty_expression()
        array_1: ap.Array = ap.Array([1, 2])
        array_2: ap.Array = array_1.concat([3, 4])
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{array_2.variable_name} = " f"{array_1.variable_name}.concat([3, 4]);"
        )
        assert expected in expression

        array_3: ap.Array = ap.Array([5, 6])
        array_4: ap.Array = array_1.concat(array_3)
        expression = expression_data_util.get_current_expression()
        expected = (
            f"{array_4.variable_name} = "
            f"{array_1.variable_name}.concat({array_3.variable_name});"
        )
        assert expected in expression

    @apply_test_settings()
    def test_insert(self) -> None:
        array_1: ap.Array = ap.Array([1, 3])
        array_1.insert(index=1, value=2)
        assert array_1.value == [1, 2, 3]

    @apply_test_settings()
    def test_insert_at(self) -> None:
        array_1: ap.Array = ap.Array([1, 3])
        array_1.insert_at(index=1, value=2)
        assert array_1.value == [1, 2, 3]

    @apply_test_settings()
    def test__append_insert_expression(self) -> None:
        expression_data_util.empty_expression()
        array_1: ap.Array[Any] = ap.Array([1, 4])
        array_1.insert(index=1, value=2)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{array_1.variable_name}.splice(1, 0, 2);"
        assert expected in expression

        index_1: ap.Int = ap.Int(2)
        value_1: ap.Int = ap.Int(3)
        array_1.insert(index=index_1, value=value_1)
        expression = expression_data_util.get_current_expression()
        expected = (
            f"{array_1.variable_name}.splice"
            f"({index_1.variable_name}, 0, {value_1.variable_name});"
        )
        assert expected in expression

    @apply_test_settings()
    def test_pop(self) -> None:
        array_1: ap.Array = ap.Array([1, 2])
        value: int = array_1.pop()
        assert array_1.value == [1]
        assert value == 2

    @apply_test_settings()
    def test__append_pop_expression(self) -> None:
        expression_data_util.empty_expression()
        int_1: ap.Int = ap.Int(2)
        array_1: ap.Array[Any] = ap.Array([1, int_1, 3])
        _: int = array_1.pop()
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{array_1.variable_name}.pop();"
        assert expected in expression

        value_1: ap.Int = array_1.pop()
        assert value_1.variable_name == int_1.variable_name
        expression = expression_data_util.get_current_expression()
        expected = f"{value_1.variable_name} = " f"{array_1.variable_name}.pop();"
        assert expected in expression

    @apply_test_settings()
    def test_remove(self) -> None:
        array_1: ap.Array = ap.Array([1, 2, 3])
        array_1.remove(value=2)
        assert array_1.value == [1, 3]

    @apply_test_settings()
    def test__append_remove_expression(self) -> None:
        expression_data_util.empty_expression()
        array_1: ap.Array = ap.Array([1, 2, 3])
        array_1.remove(2)
        expression: str = expression_data_util.get_current_expression()
        expected_strs: List[str] = [
            "var idx_",
            f" = _.indexOf({array_1.variable_name}, 2);"
            f"\n{array_1.variable_name}.splice(",
            ", 1);",
        ]
        for expected_str in expected_strs:
            assert expected_str in expression

    @apply_test_settings()
    def test_remove_at(self) -> None:
        array_1: ap.Array = ap.Array([1, 2, 3, 4])
        array_1.remove_at(index=1)
        assert array_1.value == [1, 3, 4]
        array_1.remove_at(index=ap.Int(1))
        assert array_1.value == [1, 4]

        array_1.remove_at(index=2)
        assert array_1.value == [1, 4]

    @apply_test_settings()
    def test__append_remove_at_expression(self) -> None:
        expression_data_util.empty_expression()
        array_1: ap.Array = ap.Array([1, 2, 3, 4])
        array_1.remove_at(index=1)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{array_1.variable_name}.splice(1, 1);"
        assert expected in expression

        int_1: ap.Int = ap.Int(1)
        array_1.remove_at(index=int_1)
        expression = expression_data_util.get_current_expression()
        expected = f"{array_1.variable_name}.splice({int_1.variable_name}, 1);"
        assert expected in expression

    @apply_test_settings()
    def test_reverse(self) -> None:
        array_1: ap.Array = ap.Array([1, 2, 3])
        array_1.reverse()
        assert array_1.value == [3, 2, 1]

    @apply_test_settings()
    def test__append_reverse_expression(self) -> None:
        expression_data_util.empty_expression()
        array_1: ap.Array = ap.Array([1, 2, 3])
        array_1.reverse()
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{array_1.variable_name}.reverse();"
        assert expected in expression

    @apply_test_settings()
    def test_sort(self) -> None:
        array_1: ap.Array = ap.Array([3, 5, 1, 4, 2])
        array_1.sort()
        assert array_1.value == [1, 2, 3, 4, 5]

        array_2: ap.Array = ap.Array([3, 5, 1, 4, 2])
        array_2.sort(ascending=False)
        assert array_2.value == [5, 4, 3, 2, 1]

    @apply_test_settings()
    def test__append_sort_expression(self) -> None:
        expression_data_util.empty_expression()
        array_1: ap.Array = ap.Array([3, 5, 1, 4, 2])
        array_1.sort()
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{array_1.variable_name}.sort();"
        assert expected in expression
        assert "reverse" not in expression

        expression_data_util.empty_expression()
        array_2: ap.Array = ap.Array([3, 5, 1, 4, 2])
        array_2.sort(ascending=False)
        expression = expression_data_util.get_current_expression()
        expected = (
            f"{array_2.variable_name}.sort();" f"\n{array_2.variable_name}.reverse();"
        )
        assert expected in expression

    @apply_test_settings()
    def test_slice(self) -> None:
        array_1: ap.Array = ap.Array([1, 2, 3, 4])
        array_2: ap.Array = array_1.slice(start=1, end=3)
        assert array_2.value == [2, 3]

        array_3: ap.Array = array_1.slice(start=1)
        assert array_3.value == [2, 3, 4]

        array_4: ap.Array = array_1.slice(end=2)
        assert array_4.value == [1, 2]

    @apply_test_settings()
    def test__append_slice_expression(self) -> None:
        expression_data_util.empty_expression()
        array_1: ap.Array = ap.Array([1, 2, 3, 4])
        array_2: ap.Array = array_1.slice(start=1, end=3)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{array_2.variable_name} = " f"{array_1.variable_name}.slice(1, 3);"
        )
        assert expected in expression

        int_1: ap.Int = ap.Int(1)
        int_2: ap.Int = ap.Int(3)
        array_3: ap.Array = array_1.slice(start=int_1, end=int_2)
        expression = expression_data_util.get_current_expression()
        expected = (
            f"{array_3.variable_name} = {array_1.variable_name}"
            f".slice({int_1}, {int_2});"
        )
        assert expected in expression

        array_4: ap.Array = array_1.slice(start=1)
        expression = expression_data_util.get_current_expression()
        expected = f"{array_4.variable_name} = {array_1.variable_name}" ".slice(1);"
        assert expected in expression

        array_5: ap.Array = array_1.slice(end=2)
        expression = expression_data_util.get_current_expression()
        expected = f"{array_5.variable_name} = {array_1.variable_name}" ".slice(0, 2);"
        assert expected in expression

    @apply_test_settings()
    def test___getitem__(self) -> None:
        array_1: ap.Array[Any] = ap.Array([1, 2, 3])
        testing_helper.assert_raises(
            expected_error_class=ValueError, callable_=array_1.__getitem__, index=(0, 1)
        )

        value_1: int = array_1[2]
        assert value_1 == 3

        value_2: ap.AnyValue = array_1[3]
        assert isinstance(value_2, ap.AnyValue)

    @apply_test_settings()
    def test__append_getitem_expression(self) -> None:
        expression_data_util.empty_expression()
        int_1: ap.Int = ap.Int(3)
        array_1: ap.Array[Any] = ap.Array([1, 2, int_1])
        _: int = array_1[0]
        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=rf"var {var_names.ANY}_.+? = {array_1.variable_name}\[0\]",
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

        value_1: ap.Int = array_1[2]
        expression = expression_data_util.get_current_expression()
        expected: str = f"{value_1.variable_name} = {array_1.variable_name}[2];"
        assert expected in expression

        int_2: ap.Int = ap.Int(2)
        _ = array_1[int_2]
        expression = expression_data_util.get_current_expression()
        expected = (
            f"{value_1.variable_name} = {array_1.variable_name}"
            f"[{int_2.variable_name}];"
        )
        assert expected in expression

        array_2: ap.Array = ap.Array([])
        value_2: ap.AnyValue = array_2[0]
        expression = expression_data_util.get_current_expression()
        expected = f"{value_2.variable_name} = {array_2.variable_name}[0];"
        assert expected in expression

    @apply_test_settings()
    def test__validate_index_type_is_int(self) -> None:
        array_1: ap.Array = ap.Array([1, 2])
        array_1._validate_index_type_is_int(index=1)
        array_1._validate_index_type_is_int(index=ap.Int(1))
        testing_helper.assert_raises(
            expected_error_class=ValueError,
            callable_=array_1._validate_index_type_is_int,
            index="Hello!",
        )

    @apply_test_settings()
    def test__get_builtin_int_from_index(self) -> None:
        array_1: ap.Array = ap.Array([1, 2])
        builtin_int_index: int = array_1._get_builtin_int_from_index(index=1)
        assert builtin_int_index == 1
        assert isinstance(builtin_int_index, int)

        builtin_int_index = array_1._get_builtin_int_from_index(index=ap.Int(1))
        assert builtin_int_index == 1
        assert isinstance(builtin_int_index, int)

    @apply_test_settings()
    def test___setitem__(self) -> None:
        array_1: ap.Array[Any] = ap.Array([1, 2, 3])
        array_1[1] = 4
        assert array_1.value[1] == 4

        int_1: ap.Int = ap.Int(1)
        int_2: ap.Int = ap.Int(5)
        array_1[int_1] = int_2
        assert array_1.value[1] == 5
        assert isinstance(array_1.value[1], ap.Int)

    @apply_test_settings()
    def test__append_setitem_expression(self) -> None:
        expression_data_util.empty_expression()
        array_1: ap.Array[Any] = ap.Array([1, 2, 3])
        array_1[1] = 4
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{array_1.variable_name}[1] = 4;"
        assert expected in expression

        array_1[1] = "Hello!"
        expression = expression_data_util.get_current_expression()
        expected = f'{array_1.variable_name}[1] = "Hello!";'

        int_1: ap.Int = ap.Int(1)
        int_2: ap.Int = ap.Int(5)
        array_1[int_1] = int_2
        expression = expression_data_util.get_current_expression()
        expected = (
            f"{array_1.variable_name}[{int_1.variable_name}] = "
            f"{int_2.variable_name};"
        )
        assert expected in expression

    @apply_test_settings()
    def test___delitem__(self) -> None:
        array_1: ap.Array = ap.Array([1, 2, 3])
        del array_1[1]
        assert array_1.value == [1, 3]

    @apply_test_settings()
    def test_length(self) -> None:
        array_1: ap.Array = ap.Array([1, 2, 3])
        length: ap.Int = array_1.length
        assert length == 3
        assert isinstance(length, ap.Int)

    @apply_test_settings()
    def test__append_length_expression(self) -> None:
        expression_data_util.empty_expression()
        array_1: ap.Array = ap.Array([1, 2, 3])
        length: ap.Int = array_1.length
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{length.variable_name} = {array_1.variable_name}.length;"
        assert expected in expression

    @apply_test_settings()
    def test___len__(self) -> None:
        array_1: ap.Array = ap.Array([1, 2, 3])
        with pytest.raises(Exception):  # type: ignore
            len(array_1)  # type: ignore

    @apply_test_settings()
    def test_join(self) -> None:
        array_1: ap.Array = ap.Array(["1", ap.String("2"), 3, ap.Int(4)])
        joined: ap.String = array_1.join(",")
        assert joined == "1,2,3,4"
        joined = array_1.join(ap.String(","))
        assert joined == "1,2,3,4"

    @apply_test_settings()
    def test__append_join_expression(self) -> None:
        expression_data_util.empty_expression()
        string_1: ap.String = ap.String("2")
        int_1: ap.Int = ap.Int(4)
        array_1: ap.Array = ap.Array(["1", string_1, 3, int_1])
        string_2: ap.String = ap.String(", ")
        joined: ap.String = array_1.join(sep=string_2)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{joined.variable_name} = "
            f"{array_1.variable_name}.join({string_2.variable_name});"
        )
        assert expected in expression

    @apply_test_settings()
    def test___str__(self) -> None:
        array_1: ap.Array = ap.Array(
            [
                "1",
                2,
                ap.Int(3),
                ap.Number(10.5),
                ap.Boolean(True),
                ap.String("Hello!"),
                ap.Array([4, 5]),
            ]
        )
        string: str = str(array_1)
        assert string == (
            "['1', 2, Int(3), Number(10.5), Boolean(True), "
            'String("Hello!"), Array([4, 5])]'
        )

        del array_1._value
        assert str(array_1) == "[]"

    @apply_test_settings()
    def test___repr__(self) -> None:
        array_1: ap.Array = ap.Array([1, 2])
        assert repr(array_1) == "Array([1, 2])"

        del array_1._value
        assert repr(array_1) == "Array([])"

        array_2: ap.Array = ap.Array([ap.Int(10)])
        assert repr(array_2) == "Array([Int(10)])"

    @apply_test_settings()
    def test_index_of(self) -> None:
        array_1: ap.Array = ap.Array([1, 2, 3])
        index_1: ap.Int = array_1.index_of(value=2)
        assert index_1 == 1
        assert isinstance(index_1, ap.Int)

        index_2: ap.Int = array_1.index_of(value=4)
        assert index_2 == -1

    @apply_test_settings()
    def test__append_index_of_expression(self) -> None:
        expression_data_util.empty_expression()
        int_1: ap.Int = ap.Int(2)
        array_1: ap.Array = ap.Array([1, int_1, 3])
        index_1: ap.Int = array_1.index_of(value=int_1)
        expression = expression_data_util.get_current_expression()
        expected: str = (
            f"{index_1.variable_name} = {array_1.variable_name}"
            f".indexOf({int_1.variable_name});"
        )
        assert expected in expression

    @apply_test_settings()
    def test___eq__(self) -> None:
        array_1: ap.Array = ap.Array([1, ap.Int(2)])
        array_2: ap.Array = ap.Array([1, ap.Int(2)])
        result: ap.Boolean = array_1 == array_2
        assert result
        assert isinstance(result, ap.Boolean)

        array_3: ap.Array = ap.Array([ap.Int(1), 2])
        assert array_1 == array_3

        array_4: ap.Array = ap.Array([1, 2, 3])
        assert array_1 != array_4

        result = array_4 == 10
        assert isinstance(result, ap.Boolean)

    @apply_test_settings()
    def test___bool__(self) -> None:
        array_1: ap.Array = ap.Array([])
        assert not array_1

        array_2: ap.Array = ap.Array([1])
        assert array_2

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        array_1: ap.Array = ap.Array([1, 2, 3])
        snapshot_name: str = "snapshot_1"
        array_1._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        if array_1._value_snapshots is None:
            raise AssertionError()
        assert array_1._value_snapshots[snapshot_name] == [1, 2, 3]

        array_1.value = [4, 5, 6]
        array_1._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert array_1._value_snapshots[snapshot_name] == [1, 2, 3]

    @apply_test_settings()
    def test__revert(self) -> None:
        array_1: ap.Array = ap.Array([1, 2, 3])
        snapshot_name: str = "snapshot_1"
        array_1._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        array_1.value = [4, 5, 6]
        array_1._run_all_revert_methods(snapshot_name=snapshot_name)
        assert array_1 == [1, 2, 3]

        array_1.value = [4, 5, 6]
        array_1._run_all_revert_methods(snapshot_name=snapshot_name)
        assert array_1 == [4, 5, 6]

    @apply_test_settings()
    def test__append_eq_expression(self) -> None:
        expression_data_util.empty_expression()
        array_1: ap.Array = ap.Array([1, 2])
        array_2: ap.Array = ap.Array([3, 4])
        result: ap.Boolean = array_1 == array_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = "
            f"_.isEqual({array_1.variable_name}, {array_2.variable_name});"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        result = array_1 == [3, 4]
        expression = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{result.variable_name} = "
                rf"_.isEqual\({array_1.variable_name}, "
                rf"{var_names.ARRAY}\_.+?\);"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @apply_test_settings()
    def test___ne__(self) -> None:
        array_1: ap.Array = ap.Array([1, 2])
        array_2: ap.Array = ap.Array([3, 4])
        result: ap.Boolean = array_1 != array_2
        assert isinstance(result, ap.Boolean)
        assert result

        array_3: ap.Array = ap.Array([1, 2])
        result = array_1 != array_3
        assert not result

    @apply_test_settings()
    def test__append_ne_expression(self) -> None:
        expression_data_util.empty_expression()
        array_1: ap.Array = ap.Array([1, 2])
        array_2: ap.Array = ap.Array([3, 4])
        result: ap.Boolean = array_1 != array_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = "
            f"!_.isEqual({array_1.variable_name}, {array_2.variable_name});"
        )
        assert expected in expression

    @apply_test_settings()
    def test__convert_other_val_to_array(self) -> None:
        array_1: ap.Array = ap.Array([1, 2])
        converted_val: Any = array_1._convert_other_val_to_array(other=[3, 4])
        assert converted_val == [3, 4]
        assert isinstance(converted_val, ap.Array)

        converted_val = array_1._convert_other_val_to_array(other=10)
        assert converted_val == 10

    @apply_test_settings()
    def test__convert_range_to_list(self) -> None:
        array_1: ap.Array = ap.Array(range(3))
        assert array_1._initial_value == [0, 1, 2]

        array_2: ap.Array = ap.Array((0, 1, 2))
        assert array_2._initial_value == (0, 1, 2)

    @apply_test_settings()
    def test__append_clear_expression(self) -> None:
        expression_data_util.empty_expression()
        ap.Stage()
        arr: ap.Array = ap.Array([1, 2, 3])
        arr._append_clear_expression()
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{arr.variable_name}.splice(0);"
        assert expected in expression

    @apply_test_settings()
    def test_clear(self) -> None:
        expression_data_util.empty_expression()
        ap.Stage()
        arr: ap.Array = ap.Array([1, 2, 3])
        arr.clear()
        assert arr._value == []
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{arr.variable_name}.splice(0);"
        assert expected in expression

    @apply_test_settings()
    def test__create_initial_substitution_expression(self) -> None:
        arr_1: ap.Array = ap.Array([1, 2, 3])
        expression: str = arr_1._create_initial_substitution_expression()
        assert expression == f"{arr_1.variable_name} = [1, 2, 3];"

        arr_2: ap.Array = ap.Array([1, 2, 3])
        arr_1 = ap.Array(arr_2)
        expression = arr_1._create_initial_substitution_expression()
        assert expression == f"{arr_1.variable_name} = {arr_2.variable_name};"

    @apply_test_settings()
    def test__initialize_for_loop_key_or_value(self) -> None:
        arr_value: ap.Array = ap.Array._initialize_for_loop_key_or_value()
        assert arr_value == ap.Array([])

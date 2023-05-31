import apysc as ap
from apysc._console import assertion
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings

_EXPECTED_FILE_NAME_STR: str = "file name: test_assertion.py"


@apply_test_settings()
def test_assert_equal() -> None:
    expression_data_util.empty_expression()
    int_1: ap.Int = ap.Int(10)
    int_2: ap.Int = ap.Int(20)
    assertion.assert_equal(left=int_1, right=int_2, msg="Invalid int values.")

    expression: str = expression_data_util.get_current_expression()
    expected: str = (
        f"console.assert({int_1.variable_name} === {int_2.variable_name}, "
        '"Invalid int values.");'
    )
    assert expected in expression
    assert _EXPECTED_FILE_NAME_STR in expression

    expression_data_util.empty_expression()
    assertion.assert_equal(left=[1, 2, 3], right=ap.Array([1, 2, 3]))
    expression = expression_data_util.get_current_expression()
    assert "[assert_arrays_equal]" in expression
    assert "[assert_equal]" not in expression
    assert _EXPECTED_FILE_NAME_STR in expression

    expression_data_util.empty_expression()
    assertion.assert_equal(left=ap.Array([1, 2, 3]), right=[1, 2, 3])
    expression = expression_data_util.get_current_expression()
    assert "[assert_arrays_equal]" in expression
    assert "[assert_equal]" not in expression
    assert _EXPECTED_FILE_NAME_STR in expression

    expression_data_util.empty_expression()
    assertion.assert_equal(left={"a": 10}, right=ap.Dictionary({"a": 10}))
    expression = expression_data_util.get_current_expression()
    assert "[assert_dicts_equal]" in expression
    assert "[assert_equal]" not in expression
    assert _EXPECTED_FILE_NAME_STR in expression

    expression_data_util.empty_expression()
    assertion.assert_equal(left=ap.Dictionary({"a": 10}), right={"a": 10})
    expression = expression_data_util.get_current_expression()
    assert "[assert_dicts_equal]" in expression
    assert "[assert_equal]" not in expression
    assert _EXPECTED_FILE_NAME_STR in expression


@apply_test_settings()
def test__trace_info() -> None:
    expression_data_util.empty_expression()
    int_1: ap.Int = ap.Int(10)
    int_2: ap.Int = ap.Int(20)
    assertion.assert_equal(left=int_1, right=int_2, msg="Invalid int values.")
    expression: str = expression_data_util.get_current_expression()
    expected: str = f"Left-side variable name: {int_1.variable_name}"
    assert expected in expression
    expected = f"Right-side variable name: {int_2.variable_name}"
    assert expected in expression


@apply_test_settings()
def test_assert_not_equal() -> None:
    expression_data_util.empty_expression()
    int_1: ap.Int = ap.Int(10)
    assertion.assert_not_equal(left=11, right=int_1, msg="Invalid condition.")
    expression: str = expression_data_util.get_current_expression()
    expected: str = (
        f'console.assert(11 !== {int_1.variable_name}, "Invalid condition.");'
    )
    assert expected in expression
    assert _EXPECTED_FILE_NAME_STR in expression

    expression_data_util.empty_expression()
    assertion.assert_not_equal(left=[1, 2], right=ap.Array([1, 2, 3]))
    expression = expression_data_util.get_current_expression()
    assert "[assert_arrays_not_equal]" in expression
    assert "[assert_not_equal]" not in expression
    assert _EXPECTED_FILE_NAME_STR in expression

    expression_data_util.empty_expression()
    assertion.assert_not_equal(left=ap.Array([1, 2, 3]), right=[1, 2])
    expression = expression_data_util.get_current_expression()
    assert "[assert_arrays_not_equal]" in expression
    assert "[assert_not_equal]" not in expression
    assert _EXPECTED_FILE_NAME_STR in expression

    expression_data_util.empty_expression()
    assertion.assert_not_equal(left={"a": 10}, right=ap.Dictionary({"a": 10}))
    expression = expression_data_util.get_current_expression()
    assert "[assert_dicts_not_equal]" in expression
    assert "[assert_not_equal]" not in expression
    assert _EXPECTED_FILE_NAME_STR in expression

    expression_data_util.empty_expression()
    assertion.assert_not_equal(left=ap.Dictionary({"a": 10}), right={"a": 10})
    expression = expression_data_util.get_current_expression()
    assert "[assert_dicts_not_equal]" in expression
    assert "[assert_not_equal]" not in expression
    assert _EXPECTED_FILE_NAME_STR in expression


@apply_test_settings()
def test__get_left_and_right_strs() -> None:
    int_1: ap.Int = ap.Int(10)
    int_2: ap.Int = ap.Int(20)
    left_str, right_str = assertion._get_left_and_right_strs(left=int_1, right=int_2)
    assert left_str == int_1.variable_name
    assert right_str == int_2.variable_name

    left_str, right_str = assertion._get_left_and_right_strs(
        left="Hello", right="World!"
    )
    assert left_str == '"Hello"'
    assert right_str == '"World!"'

    left_str, right_str = assertion._get_left_and_right_strs(left="a\nb", right="c\nd")
    assert left_str == '"a\\nb"'
    assert right_str == '"c\\nd"'


@apply_test_settings()
def test_assert_true() -> None:
    expression_data_util.empty_expression()
    boolean_1: ap.Boolean = ap.Boolean(True)
    assertion.assert_true(value=boolean_1, type_strict=True, msg="Value is not true.")
    expression: str = expression_data_util.get_current_expression()
    expected: str = (
        f"console.assert({boolean_1.variable_name} === true, " '"Value is not true.");'
    )
    assert expected in expression
    assert _EXPECTED_FILE_NAME_STR in expression

    assertion.assert_true(value=boolean_1, type_strict=False)
    expression = expression_data_util.get_current_expression()
    expected = f'console.assert({boolean_1.variable_name} == true, "");'
    assert expected in expression
    assert _EXPECTED_FILE_NAME_STR in expression


@apply_test_settings()
def test__add_equal_if_type_strict_setting_is_true() -> None:
    expression: str = assertion._add_equal_if_type_strict_setting_is_true(
        expression="a ==", type_strict=True
    )
    assert expression == "a ==="

    expression = assertion._add_equal_if_type_strict_setting_is_true(
        expression="a ==", type_strict=False
    )
    assert expression == "a =="


@apply_test_settings()
def test_assert_false() -> None:
    expression_data_util.empty_expression()
    boolean_1: ap.Boolean = ap.Boolean(False)
    assertion.assert_false(boolean_1, msg="Value is not false.")
    expression: str = expression_data_util.get_current_expression()
    expected: str = (
        f"console.assert({boolean_1.variable_name} === false, "
        '"Value is not false.");'
    )
    assert expected in expression
    assert _EXPECTED_FILE_NAME_STR in expression


@apply_test_settings()
def test__value_type_is_array() -> None:
    result: bool = assertion._value_type_is_array(value=100)
    assert not result

    result = assertion._value_type_is_array(value=ap.Array([100, 200]))
    assert result


@apply_test_settings()
def test_assert_arrays_equal() -> None:
    expression_data_util.empty_expression()
    array_1: ap.Array = ap.Array([1, 2, 3])
    assertion.assert_arrays_equal(
        left=[1, 2, 3], right=array_1, msg="Array values are not equal."
    )
    expression: str = expression_data_util.get_current_expression()
    expected: str = (
        f"console.assert(_.isEqual([1, 2, 3], {array_1.variable_name}), "
        f'"Array values are not equal.");'
    )
    assert expected in expression
    assert _EXPECTED_FILE_NAME_STR in expression


@apply_test_settings()
def test__trace_arrays_or_dicts_assertion_info() -> None:
    expression_data_util.empty_expression()
    array_1: ap.Array = ap.Array([1, 2, 3])
    assertion._trace_arrays_or_dicts_assertion_info(
        interface_label="assert_arrays_equal",
        left=[1, 2, 3],
        right=array_1,
        outer_frames_index_adjustment=3,
    )
    expression: str = expression_data_util.get_current_expression()
    assert "[assert_arrays_equal]" in expression
    assert '"\\nLeft value:", "[1, 2, 3]"' in expression
    expected = f'"right value:", "{array_1.variable_name}'
    assert expected in expression
    assert _EXPECTED_FILE_NAME_STR in expression

    expression_data_util.empty_expression()
    assertion._trace_arrays_or_dicts_assertion_info(
        interface_label="assert_arrays_not_equal",
        left=array_1,
        right=[1, 2, 3],
        outer_frames_index_adjustment=3,
    )
    expression = expression_data_util.get_current_expression()
    expected = f'"\\nLeft value:", "{array_1.variable_name} ([1, 2, 3])"'
    assert expected in expression
    assert '"right value:", "[1, 2, 3]"' in expression
    assert _EXPECTED_FILE_NAME_STR in expression

    expression_data_util.empty_expression()
    dict_1: ap.Dictionary = ap.Dictionary({"a": 10})
    assertion._trace_arrays_or_dicts_assertion_info(
        interface_label="assert_dicts_equal",
        left=dict_1,
        right={"a": 10},
        outer_frames_index_adjustment=3,
    )
    expression = expression_data_util.get_current_expression()
    expected = f'"\\nLeft value:", "{dict_1.variable_name} ({{a: 10}})"'
    assert expected in expression
    assert '"right value:", "{a: 10}"' in expression
    assert _EXPECTED_FILE_NAME_STR in expression


@apply_test_settings()
def test__make_arrays_or_dicts_comparison_expression() -> None:
    expression_data_util.empty_expression()
    array_1: ap.Array = ap.Array([1, 2, 3])
    expression: str = assertion._make_arrays_or_dicts_comparison_expression(
        left=[1, 2, 3],
        right=array_1,
        msg="Array values is not equal.",
        not_condition=False,
    )
    expected: str = (
        f"console.assert(_.isEqual([1, 2, 3], {array_1.variable_name}), "
        '"Array values is not equal.");'
    )
    assert expression == expected

    expression = assertion._make_arrays_or_dicts_comparison_expression(
        left=[1, 2, 3], right=[1], msg="", not_condition=True
    )
    expected = 'console.assert(!_.isEqual([1, 2, 3], [1]), "");'
    assert expression == expected

    dict_1: ap.Dictionary = ap.Dictionary({"a": 10})
    expression = assertion._make_arrays_or_dicts_comparison_expression(
        left=dict_1, right={"a": 10}, msg="", not_condition=False
    )
    expected = f"console.assert(_.isEqual({dict_1.variable_name}, " '{"a": 10}), "");'
    assert expression == expected


@apply_test_settings()
def test_assert_arrays_not_equal() -> None:
    expression_data_util.empty_expression()
    array_1: ap.Array = ap.Array([1, 2, 3])
    assertion.assert_arrays_not_equal(
        left=[1, 2], right=array_1, msg="Array values are equal."
    )
    expression: str = expression_data_util.get_current_expression()
    expected: str = (
        f"console.assert(!_.isEqual([1, 2], {array_1.variable_name}), "
        f'"Array values are equal.");'
    )
    assert expected in expression
    assert _EXPECTED_FILE_NAME_STR in expression


@apply_test_settings()
def test_assert_defined() -> None:
    expression_data_util.empty_expression()
    int_1: ap.Int = ap.Int(3)
    assertion.assert_defined(value=int_1, msg="value is undefined.")
    expression: str = expression_data_util.get_current_expression()
    expected: str = (
        f"console.assert(!_.isUndefined({int_1.variable_name}), "
        '"value is undefined.");'
    )
    assert expected in expression
    assert _EXPECTED_FILE_NAME_STR in expression


@apply_test_settings()
def test_assert_undefined() -> None:
    expression_data_util.empty_expression()
    int_1: ap.Int = ap.Int(3)
    assertion.assert_undefined(value=int_1, msg="value is not undefined.")
    expression: str = expression_data_util.get_current_expression()
    expected: str = (
        f"console.assert(_.isUndefined({int_1.variable_name}), "
        '"value is not undefined.");'
    )
    assert expected in expression
    assert _EXPECTED_FILE_NAME_STR in expression


@apply_test_settings()
def test_assert_dicts_equal() -> None:
    expression_data_util.empty_expression()
    dict_1: ap.Dictionary = ap.Dictionary({"a": 10})
    assertion.assert_dicts_equal(
        left={"a": 10}, right=dict_1, msg="Dictionary values are not equal."
    )
    expression: str = expression_data_util.get_current_expression()
    expected: str = (
        'console.assert(_.isEqual({"a": 10}, '
        f"{dict_1.variable_name}), "
        '"Dictionary values are not equal.");'
    )
    assert expected in expression
    assert _EXPECTED_FILE_NAME_STR in expression


@apply_test_settings()
def test__value_type_is_dict() -> None:
    dict_1: ap.Dictionary = ap.Dictionary({"a": 10})
    result: bool = assertion._value_type_is_dict(value=dict_1)
    assert result

    result = assertion._value_type_is_dict(value=10)
    assert not result

    point: ap.Point2D = ap.Point2D(x=10, y=20)
    result = assertion._value_type_is_dict(value=point)
    assert result


@apply_test_settings()
def test_assert_dicts_not_equal() -> None:
    expression_data_util.empty_expression()
    dict_1: ap.Dictionary = ap.Dictionary({"a": 10})
    assertion.assert_dicts_not_equal(
        left={"a": 10}, right=dict_1, msg="Dictionary values are equal."
    )
    expression: str = expression_data_util.get_current_expression()
    expected: str = (
        'console.assert(!_.isEqual({"a": 10}, '
        f"{dict_1.variable_name}), "
        '"Dictionary values are equal.");'
    )
    assert expected in expression
    assert _EXPECTED_FILE_NAME_STR in expression


@apply_test_settings()
def test_assert_greater() -> None:
    expression_data_util.empty_expression()
    assertion.assert_greater(left=20, right=10, msg="Value is not greater than 10.")
    expression: str = expression_data_util.get_current_expression()
    expected: str = 'console.assert(20 > 10, "Value is not greater than 10.");'
    assert expected in expression

    expression_data_util.empty_expression()
    left_val: ap.Int = ap.Int(20)
    right_val: ap.Int = ap.Int(10)
    assertion.assert_greater(
        left=left_val,
        right=right_val,
        msg="Value is not greater than 10.",
    )
    expression = expression_data_util.get_current_expression()
    expected = (
        f"console.assert({left_val.variable_name} > {right_val.variable_name}, "
        '"Value is not greater than 10.");'
    )
    assert expected in expression


@apply_test_settings()
def test_assert_greater_equal() -> None:
    expression_data_util.empty_expression()
    assertion.assert_greater_equal(
        left=20,
        right=10,
        msg="Value is not greater than or equal to 10.",
    )
    expression: str = expression_data_util.get_current_expression()
    expected: str = (
        'console.assert(20 >= 10, "Value is not greater than or equal to 10.");'
    )
    assert expected in expression

    expression_data_util.empty_expression()
    left_val: ap.Int = ap.Int(20)
    right_val: ap.Int = ap.Int(10)
    assertion.assert_greater_equal(
        left=left_val,
        right=right_val,
        msg="Value is not greater than or equal to 10.",
    )
    expression = expression_data_util.get_current_expression()
    expected = (
        f"console.assert({left_val.variable_name} >= {right_val.variable_name}, "
        '"Value is not greater than or equal to 10.");'
    )
    assert expected in expression


@apply_test_settings()
def test_assert_less() -> None:
    expression_data_util.empty_expression()
    assertion.assert_less(left=10, right=11, msg="Value is not less than 11.")
    expression: str = expression_data_util.get_current_expression()
    expected: str = 'console.assert(10 < 11, "Value is not less than 11.");'
    assert expected in expression

    expression_data_util.empty_expression()
    left_val: ap.Int = ap.Int(10)
    right_val: ap.Int = ap.Int(11)
    assertion.assert_less(
        left=left_val,
        right=right_val,
        msg="Value is not less than 11.",
    )
    expression = expression_data_util.get_current_expression()
    expected = (
        f"console.assert({left_val.variable_name} < {right_val.variable_name}, "
        '"Value is not less than 11.");'
    )
    assert expected in expression


@apply_test_settings()
def test_assert_less_equal() -> None:
    expression_data_util.empty_expression()
    assertion.assert_less_equal(
        left=10,
        right=11,
        msg="Value is not less than or equal to 11.",
    )
    expression: str = expression_data_util.get_current_expression()
    expected: str = (
        'console.assert(10 <= 11, "Value is not less than or equal to 11.");'
    )
    assert expected in expression

    expression_data_util.empty_expression()
    left_val: ap.Int = ap.Int(10)
    right_val: ap.Int = ap.Int(11)
    assertion.assert_less_equal(
        left=left_val,
        right=right_val,
        msg="Value is not less than or equal to 11.",
    )
    expression = expression_data_util.get_current_expression()
    expected = (
        f"console.assert({left_val.variable_name} <= {right_val.variable_name}, "
        '"Value is not less than or equal to 11.");'
    )
    assert expected in expression

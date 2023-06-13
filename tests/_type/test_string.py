import re
from typing import Any
from typing import Dict
from typing import Match
from typing import Optional

import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing import testing_helper
from apysc._testing.testing_helper import apply_test_settings


class TestString:
    @apply_test_settings()
    def test__get_str_value(self) -> None:
        string_1: ap.String = ap.String("Hello!")
        value: str = string_1._get_str_value(value="World!")
        assert value == "World!"
        value = string_1._get_str_value(value=string_1)
        assert value == "Hello!"

    @apply_test_settings()
    def test___init__(self) -> None:
        testing_helper.assert_raises(
            expected_error_class=ValueError, callable_=ap.String, value=100
        )

        string_1: ap.String = ap.String(
            value="Hello!", variable_name_suffix="test_string"
        )
        expected_attrs: Dict[str, Any] = {
            "_initial_value": "Hello!",
            "_value": "Hello!",
            "_type_name": var_names.STRING,
            "_variable_name_suffix": "test_string",
        }
        testing_helper.assert_attrs(expected_attrs=expected_attrs, any_obj=string_1)
        assert string_1.variable_name.startswith(f"{var_names.STRING}_")

        string_2: ap.String = ap.String(value=string_1)
        assert string_2._value == "Hello!"

    @apply_test_settings()
    def test__append_constructor_expression(self) -> None:
        expression_data_util.empty_expression()
        string_1: ap.String = ap.String(value="Hello!")
        expression: str = expression_data_util.get_current_expression()
        expected: str = f'var {string_1.variable_name} = "Hello!";'
        assert expected in expression

        string_2: ap.String = ap.String(value=string_1)
        expression = expression_data_util.get_current_expression()
        expected = f"var {string_2.variable_name} = {string_1.variable_name};"
        assert expected in expression

    @apply_test_settings()
    def test_value(self) -> None:
        string_1: ap.String = ap.String(value="Hello!")
        string_1.value = "World!"
        assert string_1.value == "World!"

    @apply_test_settings()
    def test__append_value_setter_expression(self) -> None:
        expression_data_util.empty_expression()
        string_1: ap.String = ap.String(value="Hello!")
        string_1.value = "World!"
        expression: str = expression_data_util.get_current_expression()
        expected: str = f'{string_1.variable_name} = "World!";'
        assert expected in expression

        string_2: ap.String = ap.String(value="")
        string_2.value = string_1
        expression = expression_data_util.get_current_expression()
        expected = f"{string_2.variable_name} = {string_1.variable_name};"
        assert expected in expression

    @apply_test_settings()
    def test___add__(self) -> None:
        string_1: ap.String = ap.String(value="Hello")
        string_2: ap.String = string_1 + " World!"
        assert string_2._value == "Hello World!"

        string_3: ap.String = ap.String(value=" apysc!")
        string_4: ap.String = string_1 + string_3
        assert string_4._value == "Hello apysc!"

    @apply_test_settings()
    def test__append_addition_expression(self) -> None:
        expression_data_util.empty_expression()
        string_1: ap.String = ap.String(value="Hello!")
        string_2: ap.String = string_1 + " World!"
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"var {string_2.variable_name} = {string_1.variable_name}" ' + " World!";'
        )
        assert expected in expression

    @apply_test_settings()
    def test___mul__(self) -> None:
        string_1: ap.String = ap.String(value="Hello!")
        string_2: ap.String = string_1 * 3
        assert string_2.value == "Hello!Hello!Hello!"

        string_3: ap.String = string_1 * ap.Int(2)
        assert string_3.value == "Hello!Hello!"

    @apply_test_settings()
    def test__append_multiplication_expression(self) -> None:
        expression_data_util.empty_expression()
        string_1: ap.String = ap.String(value="Hello!")
        string_2: ap.String = string_1 * 3
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'var {string_2.variable_name} = "";'
            "\nfor (var i = 0; i < 3; i++) {"
            f"\n  {string_2.variable_name} += {string_1.variable_name};"
            "\n}"
        )
        assert expected in expression

        int_1: ap.Int = ap.Int(2)
        _: ap.String = string_1 * int_1
        expression = expression_data_util.get_current_expression()
        expected = f"\nfor (var i = 0; i < {int_1.variable_name}; i++) {{"
        assert expected in expression

    @apply_test_settings()
    def test___iadd__(self) -> None:
        expression_data_util.empty_expression()
        string_1: ap.String = ap.String(value="Hello")
        original_variable_name: str = string_1.variable_name
        string_1 += " World!"
        assert string_1.value == "Hello World!"
        assert string_1.variable_name == original_variable_name

        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf's_[0-9]+ = {original_variable_name} \+ " World!";'
                rf"\n{original_variable_name} = s_[0-9]+;"
            ),
            string=expression,
            flags=re.MULTILINE | re.DOTALL,
        )
        assert match is not None

    @apply_test_settings()
    def test___imul__(self) -> None:
        expression_data_util.empty_expression()
        string_1: ap.String = ap.String(value="Hello!")
        original_variable_name: str = string_1.variable_name
        string_1 *= 3
        assert string_1.value == "Hello!Hello!Hello!"
        assert string_1.variable_name == original_variable_name

        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(rf"{original_variable_name} = s_[0-9]+;"),
            string=expression,
            flags=re.MULTILINE | re.DOTALL,
        )
        assert match is not None

    @apply_test_settings()
    def test___str__(self) -> None:
        string_1: ap.String = ap.String(value="Hello!")
        result: str = str(string_1)
        assert result == "Hello!"
        assert isinstance(result, str)

        del string_1._value
        assert str(string_1) == ""

    @apply_test_settings()
    def test___eq__(self) -> None:
        string_1: ap.String = ap.String(value="Hello!")
        assert string_1 == "Hello!"
        string_2: ap.String = ap.String(value="Hello!")
        assert string_1 == string_2
        assert not string_1 == "World!"
        assert not string_1 == 100

        assert isinstance(string_1 == "Hello!", ap.Boolean)
        assert isinstance(string_1 == string_2, ap.Boolean)
        assert isinstance(string_1 == 100, ap.Boolean)

    @apply_test_settings()
    def test___ne__(self) -> None:
        string_1: ap.String = ap.String(value="Hello!")
        assert string_1 != "World"
        assert string_1 != ap.String("World!")
        assert string_1 != 100

        assert isinstance(string_1 != "World", ap.Boolean)
        assert isinstance(string_1 != ap.String("World"), ap.Boolean)
        assert isinstance(string_1 != 100, ap.Boolean)

    @apply_test_settings()
    def test___lt__(self) -> None:
        string_1: ap.String = ap.String(value="1970-01-02")
        assert string_1 < "1970-01-03"
        string_2: ap.String = ap.String(value="1970-01-03")
        assert string_1 < string_2
        assert not string_1 < "1970-01-02"

        assert isinstance(string_1 < "1970-01-03", ap.Boolean)

    @apply_test_settings()
    def test___le__(self) -> None:
        string_1: ap.String = ap.String(value="1970-01-02")
        assert string_1 <= "1970-01-02"
        assert string_1 <= "1970-01-03"
        string_2: ap.String = ap.String(value="1970-01-02")
        assert string_1 <= string_2
        assert not string_1 <= "1970-01-01"

        assert isinstance(string_1 <= "1970-01-02", ap.Boolean)

    @apply_test_settings()
    def test___gt__(self) -> None:
        string_1: ap.String = ap.String(value="1970-01-02")
        assert string_1 > "1970-01-01"
        string_2: ap.String = ap.String(value="1970-01-01")
        assert string_1 > string_2
        assert not string_1 > "1970-01-02"

        assert isinstance(string_1 > "1970-01-01", ap.Boolean)

    @apply_test_settings()
    def test___ge__(self) -> None:
        string_1: ap.String = ap.String(value="1970-01-02")
        assert string_1 >= "1970-01-02"
        assert string_1 >= "1970-01-01"
        string_2: ap.String = ap.String(value="1970-01-02")
        assert string_1 >= string_2
        assert not string_1 >= "1970-01-03"

        assert isinstance(string_1 >= "1970-01-02", ap.Boolean)

    @apply_test_settings()
    def test___int__(self) -> None:
        string_1: ap.String = ap.String(value="100")
        assert int(string_1) == 100

    @apply_test_settings()
    def test___float__(self) -> None:
        string_1: ap.String = ap.String(value="100.5")
        assert float(string_1) == 100.5

    @apply_test_settings()
    def test___repr__(self) -> None:
        string_1: ap.String = ap.String(value="Hello!")
        assert repr(string_1) == 'String("Hello!")'

        del string_1._value
        assert repr(string_1) == 'String("")'

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        string_1: ap.String = ap.String(value="Hello!")
        snapshot_name: str = "snapshot_1"
        string_1._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        if string_1._value_snapshots is None:
            raise AssertionError()
        assert string_1._value_snapshots[snapshot_name] == "Hello!"

        string_1.value = "World!"
        string_1._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert string_1._value_snapshots[snapshot_name] == "Hello!"

    @apply_test_settings()
    def test__revert(self) -> None:
        string_1: ap.String = ap.String(value="Hello!")
        snapshot_name: str = "snapshot_1"
        string_1._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        string_1.value = "World!"
        string_1._run_all_revert_methods(snapshot_name=snapshot_name)
        assert string_1.value == "Hello!"

        string_1.value = "World!"
        string_1._run_all_revert_methods(snapshot_name=snapshot_name)
        assert string_1.value == "World!"

    @apply_test_settings()
    def test__append_eq_expression(self) -> None:
        expression_data_util.empty_expression()
        string_1: ap.String = ap.String(value="Hello!")
        string_2: ap.String = ap.String(value="World!")
        result: ap.Boolean = string_1 == string_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = "
            f"{string_1.variable_name} === {string_2.variable_name};"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        result = string_1 == "Hello!"
        expression = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{result.variable_name} = "
                rf"{string_1.variable_name} === "
                rf"{var_names.STRING}\_.+?;"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @apply_test_settings()
    def test__append_ne_expression(self) -> None:
        expression_data_util.empty_expression()
        string_1: ap.String = ap.String(value="Hello!")
        string_2: ap.String = ap.String(value="World!")
        result: ap.Boolean = string_1 != string_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = "
            f"{string_1.variable_name} !== {string_2.variable_name};"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        result = string_1 != "World!"
        expression = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{result.variable_name} = "
                rf"{string_1.variable_name} !== "
                rf"{var_names.STRING}\_.+?;"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @apply_test_settings()
    def test__append_lt_expression(self) -> None:
        expression_data_util.empty_expression()
        string_1: ap.String = ap.String(value="Hello!")
        string_2: ap.String = ap.String(value="World!")
        result: ap.Boolean = string_1 < string_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = "
            f"{string_1.variable_name} < {string_2.variable_name};"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        result = string_1 < "World!"
        expression = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{result.variable_name} = "
                rf"{string_1.variable_name} < "
                rf"{var_names.STRING}\_.+?;"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @apply_test_settings()
    def test__append_le_expression(self) -> None:
        expression_data_util.empty_expression()
        string_1: ap.String = ap.String(value="Hello!")
        string_2: ap.String = ap.String(value="World!")
        result: ap.Boolean = string_1 <= string_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = "
            f"{string_1.variable_name} <= {string_2.variable_name};"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        result = string_1 <= "World!"
        expression = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{result.variable_name} = "
                rf"{string_1.variable_name} <= "
                rf"{var_names.STRING}\_.+?;"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @apply_test_settings()
    def test__append_gt_expression(self) -> None:
        expression_data_util.empty_expression()
        string_1: ap.String = ap.String(value="Hello!")
        string_2: ap.String = ap.String(value="World!")
        result: ap.Boolean = string_1 > string_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = "
            f"{string_1.variable_name} > {string_2.variable_name};"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        result = string_1 > "World!"
        expression = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{result.variable_name} = "
                rf"{string_1.variable_name} > "
                rf"{var_names.STRING}\_.+?;"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @apply_test_settings()
    def test__append_ge_expression(self) -> None:
        expression_data_util.empty_expression()
        string_1: ap.String = ap.String(value="Hello!")
        string_2: ap.String = ap.String(value="World!")
        result: ap.Boolean = string_1 >= string_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = "
            f"{string_1.variable_name} >= {string_2.variable_name};"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        result = string_1 >= "World!"
        expression = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{result.variable_name} = "
                rf"{string_1.variable_name} >= "
                rf"{var_names.STRING}\_.+?;"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @apply_test_settings()
    def test__convert_other_val_to_string(self) -> None:
        string_1: ap.String = ap.String(value="Hello!")
        converted_val: Any = string_1._convert_other_val_to_string(other="world")
        assert isinstance(converted_val, ap.String)
        assert converted_val == "world"

        converted_val = string_1._convert_other_val_to_string(other=100)
        assert converted_val == 100

    @apply_test_settings()
    def test__create_initial_substitution_expression(self) -> None:
        string: ap.String = ap.String(value="Hello!")
        expression: str = string._create_initial_substitution_expression()
        expected_str: str = f'{string.variable_name} = "Hello!";'
        assert expression == expected_str

        other_string: ap.String = ap.String("Hello!")
        string = ap.String(value=other_string)
        expression = string._create_initial_substitution_expression()
        expected_str = f"{string.variable_name} = {other_string.variable_name};"
        assert expression == expected_str

    @apply_test_settings()
    def test__initialize_for_loop_value(self) -> None:
        str_value: ap.String = ap.String._initialize_for_loop_value()
        assert str_value == ap.String("")

    @apply_test_settings()
    def test___hash__(self) -> None:
        str_value: ap.String = ap.String("test")
        assert str_value.__hash__() == "test"

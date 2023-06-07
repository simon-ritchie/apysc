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


class TestBoolean:
    @apply_test_settings()
    def test___init__(self) -> None:
        boolean_1: ap.Boolean = ap.Boolean(
            value=ap.Int(1), variable_name_suffix="test_boolean"
        )
        expected_attrs: Dict[str, Any] = {
            "_initial_value": ap.Int(1),
            "_value": True,
            "_type_name": var_names.BOOLEAN,
            "_variable_name_suffix": "test_boolean",
        }
        testing_helper.assert_attrs(expected_attrs=expected_attrs, any_obj=boolean_1)
        assert boolean_1.variable_name.startswith(f"{var_names.BOOLEAN}_")

        boolean_2: ap.Boolean = ap.Boolean(value=boolean_1)
        expected_attrs = {
            "_initial_value": boolean_1,
            "_value": True,
        }
        testing_helper.assert_attrs(expected_attrs=expected_attrs, any_obj=boolean_2)

        boolean_3: ap.Boolean = ap.Boolean(value=False)
        assert not boolean_3._value

    @apply_test_settings()
    def test__append_constructor_expression(self) -> None:
        expression_data_util.empty_expression()
        int_1: ap.Int = ap.Int(1)
        boolean_1: ap.Boolean = ap.Boolean(value=int_1)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{boolean_1.variable_name} = Boolean({int_1.variable_name});"
        assert expected in expression

        boolean_2: ap.Boolean = ap.Boolean(value=True)
        expression = expression_data_util.get_current_expression()
        expected = f"{boolean_2.variable_name} = true;"
        assert expected in expression

        boolean_3: ap.Boolean = ap.Boolean(value=False)
        expression = expression_data_util.get_current_expression()
        expected = f"{boolean_3.variable_name} = false;"
        assert expected in expression

    @apply_test_settings()
    def test__get_bool_from_arg_value(self) -> None:
        boolean_1: ap.Boolean = ap.Boolean(value=1)
        result: bool = boolean_1._get_bool_from_arg_value(value=1)
        assert result
        result = boolean_1._get_bool_from_arg_value(value=0)
        assert not result
        boolean_2: ap.Boolean = ap.Boolean(value=0)
        result = boolean_1._get_bool_from_arg_value(value=boolean_2)
        assert not result
        result = boolean_1._get_bool_from_arg_value(value=True)
        assert result

        testing_helper.assert_raises(
            expected_error_class=ValueError,
            callable_=boolean_1._get_bool_from_arg_value,
            value="Hello!",
        )

    @apply_test_settings()
    def test__set_value_and_skip_expression_appending(self) -> None:
        expression_data_util.empty_expression()
        boolean_1: ap.Boolean = ap.Boolean(value=1)
        boolean_1._set_value_and_skip_expression_appending(value=False)
        assert not boolean_1._value
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{boolean_1.variable_name} = false;"
        assert expected not in expression

    @apply_test_settings()
    def test__append_value_setter_expression(self) -> None:
        expression_data_util.empty_expression()
        boolean_1: ap.Boolean = ap.Boolean(value=1)
        boolean_1.variable_name = "test_boolean_1"
        int_1: ap.Int = ap.Int(1)
        boolean_1.value = int_1
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{boolean_1.variable_name} = Boolean({int_1.variable_name});"
        assert expected in expression

        boolean_1.value = 1
        expression = expression_data_util.get_current_expression()
        expected = f"{boolean_1.variable_name} = true;"
        assert expected in expression

        boolean_1.value = 0
        expression = expression_data_util.get_current_expression()
        expected = f"{boolean_1.variable_name} = false;"
        assert expected in expression

    @apply_test_settings()
    def test_value(self) -> None:
        boolean_1: ap.Boolean = ap.Boolean(value=1)
        int_1: ap.Int = ap.Int(0)
        boolean_1.value = int_1
        assert not boolean_1.value

        boolean_1.value = 1
        assert boolean_1.value

    @apply_test_settings()
    def test___bool__(self) -> None:
        boolean_1: ap.Boolean = ap.Boolean(1)
        assert boolean_1
        boolean_1.value = 0
        assert not boolean_1

    @apply_test_settings()
    def test___repr__(self) -> None:
        boolean: ap.Boolean = ap.Boolean(True)
        assert repr(boolean) == "Boolean(True)"

        del boolean._value
        assert repr(boolean) == "Boolean(False)"

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        boolean: ap.Boolean = ap.Boolean(True)
        snapshot_name: str = "snapshot_1"
        boolean._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        if boolean._value_snapshots is None:
            raise AssertionError()
        assert boolean._value_snapshots[snapshot_name]

        boolean.value = False
        boolean._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert boolean._value_snapshots[snapshot_name]

    @apply_test_settings()
    def test__revert(self) -> None:
        boolean: ap.Boolean = ap.Boolean(True)
        snapshot_name: str = "snapshot_1"
        boolean._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        boolean.value = False
        boolean._run_all_revert_methods(snapshot_name=snapshot_name)
        assert boolean.value

        boolean.value = False
        boolean._run_all_revert_methods(snapshot_name=snapshot_name)
        assert not boolean.value

    @apply_test_settings()
    def test___eq__(self) -> None:
        boolean_1: ap.Boolean = ap.Boolean(True, variable_name_suffix="test_boolean_1")
        boolean_2: ap.Boolean = ap.Boolean(True)
        result: ap.Boolean = boolean_1 == boolean_2
        assert result
        assert isinstance(result, ap.Boolean)
        assert result._variable_name_suffix == "test_boolean_1"

        assert boolean_1

        result = boolean_1 == 1
        assert result
        assert isinstance(result, ap.Boolean)
        assert result._variable_name_suffix == "test_boolean_1"

        result = boolean_1 == ap.Int(1)
        assert result
        assert isinstance(result, ap.Boolean)
        assert result._variable_name_suffix == "test_boolean_1"

        result = boolean_1 == False  # noqa
        assert not result
        assert isinstance(result, ap.Boolean)

    @apply_test_settings()
    def test_not_(self) -> None:
        boolean_1: ap.Boolean = ap.Boolean(True, variable_name_suffix="test_boolean_1")
        boolean_2: ap.Boolean = boolean_1.not_
        assert not boolean_2
        assert boolean_1._variable_name_suffix == "test_boolean_1"

        boolean_3: ap.Boolean = boolean_2.not_
        assert boolean_3

    @apply_test_settings()
    def test__append_not_prop_expression(self) -> None:
        expression_data_util.empty_expression()
        boolean_1: ap.Boolean = ap.Boolean(True)
        boolean_2: ap.Boolean = boolean_1.not_
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{boolean_2.variable_name} = " f"!{boolean_1.variable_name};"
        assert expected in expression

    @apply_test_settings()
    def test__append_eq_expression(self) -> None:
        expression_data_util.empty_expression()
        boolean_1: ap.Boolean = ap.Boolean(True)
        boolean_2: ap.Boolean = ap.Boolean(True)
        result: ap.Boolean = boolean_1 == boolean_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = "
            f"{boolean_1.variable_name} === {boolean_2.variable_name};"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        int_1: ap.Int = ap.Int(1)
        result = boolean_1 == int_1
        expression = expression_data_util.get_current_expression()
        expected = (
            f"{result.variable_name} = "
            f"{boolean_1.variable_name} === "
            f"Boolean({int_1.variable_name});"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        result = boolean_1 == 1
        expression = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{result.variable_name} = "
                rf"{boolean_1.variable_name} === "
                rf"{var_names.BOOLEAN}\_.+?;"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @apply_test_settings()
    def test___ne__(self) -> None:
        boolean_1: ap.Boolean = ap.Boolean(True)
        boolean_2: ap.Boolean = ap.Boolean(False)
        result: ap.Boolean = boolean_1 != boolean_2
        assert result
        assert isinstance(result, ap.Boolean)

    @apply_test_settings()
    def test__append_ne_expression(self) -> None:
        expression_data_util.empty_expression()
        boolean_1: ap.Boolean = ap.Boolean(True)
        boolean_2: ap.Boolean = ap.Boolean(False)
        result: ap.Boolean = boolean_1 != boolean_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = "
            f"{boolean_1.variable_name} !== {boolean_2.variable_name};"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        int_1: ap.Int = ap.Int(1)
        result = boolean_1 != int_1
        expression = expression_data_util.get_current_expression()
        expected = (
            f"{result.variable_name} = "
            f"{boolean_1.variable_name} !== "
            f"Boolean({int_1.variable_name});"
        )
        assert expected in expression

    @apply_test_settings()
    def test__validate_comparison_other_type(self) -> None:
        bool_1: ap.Boolean = ap.Boolean(True)
        acceptable_values: tuple = (ap.Boolean(False), True, ap.Int(1), 0)
        for acceptable_value in acceptable_values:
            bool_1._validate_comparison_other_type(other=acceptable_value)

        testing_helper.assert_raises(
            expected_error_class=ValueError,
            callable_=bool_1._validate_comparison_other_type,
            other="Hello!",
        )

    @apply_test_settings()
    def test__create_initial_substitution_expression(self) -> None:
        bool_1: ap.Boolean = ap.Boolean(True)
        expression: str = bool_1._create_initial_substitution_expression()
        assert expression == f"{bool_1.variable_name} = true;"

        bool_1 = ap.Boolean(False)
        expression = bool_1._create_initial_substitution_expression()
        assert expression == f"{bool_1.variable_name} = false;"

        bool_2: ap.Boolean = ap.Boolean(True)
        bool_1 = ap.Boolean(bool_2)
        expression = bool_1._create_initial_substitution_expression()
        assert expression == (
            f"{bool_1.variable_name} = Boolean({bool_2.variable_name});"
        )

    @apply_test_settings()
    def test__initialize_for_loop_value(self) -> None:
        bool_value: ap.Boolean = ap.Boolean._initialize_for_loop_value()
        assert bool_value == ap.Boolean(False)


class TestBool:
    @apply_test_settings()
    def test_alias(self) -> None:
        assert ap.Boolean == ap.Bool

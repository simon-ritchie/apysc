import re
from random import randint
from typing import Any
from typing import Dict
from typing import Match
from typing import Optional

from retrying import retry

from apysc import Boolean
from apysc import Int
from apysc._expression import expression_file_util
from apysc._expression import var_names
from tests import testing_helper


class TestBoolean:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        boolean_1: Boolean = Boolean(value=Int(1))
        expected_attrs: Dict[str, Any] = {
            '_initial_value': Int(1),
            '_value': True,
            '_type_name': var_names.BOOLEAN,
        }
        testing_helper.assert_attrs(
            expected_attrs=expected_attrs, any_obj=boolean_1)
        assert boolean_1.variable_name.startswith(
            f'{var_names.BOOLEAN}_')

        boolean_2: Boolean = Boolean(value=boolean_1)
        expected_attrs = {
            '_initial_value': boolean_1,
            '_value': True,
        }
        testing_helper.assert_attrs(
            expected_attrs=expected_attrs, any_obj=boolean_2)

        boolean_3: Boolean = Boolean(value=False)
        assert not boolean_3._value

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_constructor_expression(self) -> None:
        expression_file_util.remove_expression_file()
        int_1: Int = Int(1)
        boolean_1: Boolean = Boolean(value=int_1)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{boolean_1.variable_name} = Boolean({int_1.variable_name});'
        )
        assert expected in expression

        boolean_2: Boolean = Boolean(value=True)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{boolean_2.variable_name} = true;'
        )
        assert expected in expression

        boolean_3: Boolean = Boolean(value=False)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{boolean_3.variable_name} = false;'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_bool_from_arg_value(self) -> None:
        boolean_1: Boolean = Boolean(value=1)
        result: bool = boolean_1._get_bool_from_arg_value(value=1)
        assert result
        result = boolean_1._get_bool_from_arg_value(value=0)
        assert not result
        boolean_2: Boolean = Boolean(value=0)
        result = boolean_1._get_bool_from_arg_value(value=boolean_2)
        assert not result
        result = boolean_1._get_bool_from_arg_value(value=True)
        assert result

        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=boolean_1._get_bool_from_arg_value,
            kwargs={'value': 'Hello!'})

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_value_and_skip_expression_appending(self) -> None:
        expression_file_util.remove_expression_file()
        boolean_1: Boolean = Boolean(value=1)
        boolean_1._set_value_and_skip_expression_appending(value=False)
        assert not boolean_1._value
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{boolean_1.variable_name} = false;'
        )
        assert expected not in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_value_setter_expression(self) -> None:
        expression_file_util.remove_expression_file()
        boolean_1: Boolean = Boolean(value=1)
        boolean_1.variable_name = 'test_boolean_1'
        int_1: Int = Int(1)
        boolean_1.value = int_1
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{boolean_1.variable_name} = Boolean({int_1.variable_name});'
        )
        assert expected in expression

        boolean_1.value = 1
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{boolean_1.variable_name} = true;'
        )
        assert expected in expression

        boolean_1.value = 0
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{boolean_1.variable_name} = false;'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_value(self) -> None:
        boolean_1: Boolean = Boolean(value=1)
        int_1: Int = Int(0)
        boolean_1.value = int_1
        assert not boolean_1.value

        boolean_1.value = 1
        assert boolean_1.value

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___bool__(self) -> None:
        boolean_1: Boolean = Boolean(1)
        assert boolean_1
        boolean_1.value = 0
        assert not boolean_1

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___repr__(self) -> None:
        boolean: Boolean = Boolean(True)
        assert repr(boolean) == 'Boolean(True)'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        boolean: Boolean = Boolean(True)
        snapshot_name: str = 'snapshot_1'
        boolean._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert boolean._value_snapshots[snapshot_name]

        boolean.value = False
        boolean._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert boolean._value_snapshots[snapshot_name]

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        boolean: Boolean = Boolean(True)
        snapshot_name: str = 'snapshot_1'
        boolean._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        boolean.value = False
        boolean._run_all_revert_methods(snapshot_name=snapshot_name)
        assert boolean.value

        boolean.value = False
        boolean._run_all_revert_methods(snapshot_name=snapshot_name)
        assert not boolean.value

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___eq__(self) -> None:
        boolean_1: Boolean = Boolean(True)
        boolean_2: Boolean = Boolean(True)
        result: Boolean = boolean_1 == boolean_2
        assert result
        assert isinstance(result, Boolean)

        assert boolean_1

        result = boolean_1 == 1
        assert result
        assert isinstance(result, Boolean)

        result = boolean_1 == Int(1)
        assert result
        assert isinstance(result, Boolean)

        result = boolean_1 == False  # noqa
        assert not result
        assert isinstance(result, Boolean)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_not_(self) -> None:
        boolean_1: Boolean = Boolean(True)
        boolean_2: Boolean = boolean_1.not_
        assert not boolean_2

        boolean_3: Boolean = boolean_2.not_
        assert boolean_3

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_not_prop_expression(self) -> None:
        expression_file_util.remove_expression_file()
        boolean_1: Boolean = Boolean(True)
        boolean_2: Boolean = boolean_1.not_
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{boolean_2.variable_name} = '
            f'!{boolean_1.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_eq_expression(self) -> None:
        expression_file_util.remove_expression_file()
        boolean_1: Boolean = Boolean(True)
        boolean_2: Boolean = Boolean(True)
        result: Boolean = boolean_1 == boolean_2
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{result.variable_name} = '
            f'{boolean_1.variable_name} === {boolean_2.variable_name};'
        )
        assert expected in expression

        expression_file_util.remove_expression_file()
        int_1: Int = Int(1)
        result = boolean_1 == int_1
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{result.variable_name} = '
            f'{boolean_1.variable_name} === '
            f'Boolean({int_1.variable_name});'
        )
        assert expected in expression

        expression_file_util.remove_expression_file()
        result = boolean_1 == 1
        expression = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'{result.variable_name} = '
                rf'{boolean_1.variable_name} === '
                rf'{var_names.BOOLEAN}\_.+?;'
            ),
            string=expression,
            flags=re.MULTILINE)
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___ne__(self) -> None:
        boolean_1: Boolean = Boolean(True)
        boolean_2: Boolean = Boolean(False)
        result: Boolean = boolean_1 != boolean_2
        assert result
        assert isinstance(result, Boolean)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_ne_expression(self) -> None:
        expression_file_util.remove_expression_file()
        boolean_1: Boolean = Boolean(True)
        boolean_2: Boolean = Boolean(False)
        result: Boolean = boolean_1 != boolean_2
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{result.variable_name} = '
            f'{boolean_1.variable_name} !== {boolean_2.variable_name};'
        )
        assert expected in expression

        expression_file_util.remove_expression_file()
        int_1: Int = Int(1)
        result = boolean_1 != int_1
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{result.variable_name} = '
            f'{boolean_1.variable_name} !== '
            f'Boolean({int_1.variable_name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__validate_comparison_other_type(self) -> None:
        bool_1: Boolean = Boolean(True)
        acceptable_values: tuple = (Boolean(False), True, Int(1), 0)
        for acceptable_value in acceptable_values:
            bool_1._validate_comparison_other_type(
                other=acceptable_value)

        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=bool_1._validate_comparison_other_type,
            kwargs={'other': 'Hello!'})

from apysc.expression import expression_file_util
from random import randint
from typing import Any, Dict

from retrying import retry

from apysc import Dictionary
from tests.testing_helper import assert_raises
from apysc.expression import expression_variables_util
from apysc.expression import var_names


class TestDictionary:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__validate_acceptable_value_type(self) -> None:
        dict_1: Dictionary = Dictionary(value={})
        _: Dictionary = Dictionary(value=dict_1)

        assert_raises(
            expected_error_class=TypeError,
            func_or_method=Dictionary,
            kwargs={'value': 10},
            match='Not acceptable value type is specified')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_dict_value(self) -> None:
        dict_1: Dictionary = Dictionary(value={'a': 10})
        dict_val: Dict[Any, Any] = dict_1._get_dict_value(value={'a': 20})
        assert dict_val == {'a': 20}
        assert isinstance(dict_val, dict)

        dict_val = dict_1._get_dict_value(value=dict_1)
        assert dict_val == {'a': 10}
        assert isinstance(dict_val, dict)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_constructor_expression(self) -> None:
        expression_file_util.remove_expression_file()
        dict_1: Dictionary = Dictionary(value={'a': 10})
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'var {dict_1.variable_name} = {{"a": 10}};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        dict_1: Dictionary = Dictionary(value={'a': 10})
        dict_2: Dictionary = Dictionary(value=dict_1)
        assert dict_2._initial_value == dict_1
        assert dict_2.type_name == var_names.DICTIONARY
        assert dict_2.variable_name.startswith(f'{var_names.DICTIONARY}_')
        assert dict_2._value == {'a': 10}

        assert_raises(
            expected_error_class=TypeError,
            func_or_method=Dictionary,
            kwargs={'value': 10},
            match='Not acceptable value type is specified.')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_value(self) -> None:
        dict_1: Dictionary = Dictionary(value={'a': 10})
        assert dict_1.value == {'a': 10}

        dict_1.value = {'b': 20}
        assert dict_1.value == {'b': 20}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_value_setter_expression(self) -> None:
        expression_file_util.remove_expression_file()
        dict_1: Dictionary = Dictionary(value={'a': 10})
        dict_1.value = {'b': 20}
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{dict_1.variable_name} = {{"b": 20}};'
        )
        assert expected in expression

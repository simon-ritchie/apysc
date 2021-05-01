from apysc.expression import expression_file_util
from random import randint
from typing import Any, Dict, List, Match, Optional, Union
import re

from retrying import retry

from apysc import Dictionary, Int, String, Number, Boolean
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

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        dict_1: Dictionary = Dictionary(value={'a': 10})
        snapshot_name: str = dict_1._get_next_snapshot_name()
        dict_1._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert dict_1._value_snapshot == {snapshot_name: {'a': 10}}

        dict_1.value = {'b': 20}
        dict_1._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert dict_1._value_snapshot == {snapshot_name: {'a': 10}}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        dict_1: Dictionary = Dictionary(value={'a': 10})
        snapshot_name: str = dict_1._get_next_snapshot_name()
        dict_1._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert dict_1.value == {'a': 10}

        dict_1._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        dict_1.value = {'b': 20}
        dict_1._run_all_revert_methods(snapshot_name=snapshot_name)
        assert dict_1.value == {'a': 10}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___str__(self) -> None:
        dict_1: Dictionary = Dictionary(value={'a': 10})
        assert str(dict_1) == "{'a': 10}"

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___repr__(self) -> None:
        dict_1: Dictionary = Dictionary(value={'a': 10})
        assert repr(dict_1) == "Dictionary({'a': 10})"

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_length(self) -> None:
        dict_1: Dictionary = Dictionary(value={'a': 10, 'b': 20})
        length: Int = dict_1.length
        assert length == 2
        assert isinstance(length, Int)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_length_expression(self) -> None:
        expression_file_util.remove_expression_file()
        dict_1: Dictionary = Dictionary(value={'a': 10, 'b': 20})
        length: Int = dict_1.length
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{length.variable_name} = '
            f'Object.keys({dict_1.variable_name}).length;'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___len__(self) -> None:
        dict_1: Dictionary = Dictionary(value={'a': 10, 'b': 20})
        assert_raises(
            expected_error_class=Exception,
            func_or_method=dict_1.__len__,
            match='Dictionary instance can\'t apply len function.')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__validate_key_type_is_str_or_numeric(self) -> None:
        dict_1: Dictionary = Dictionary(value={'a': 10})
        acceptables: List[Any] = [
            'Hello', String('Hello'), 10, Int(10), 20.5, Number(20.5)]
        for acceptable in acceptables:
            dict_1._validate_key_type_is_str_or_numeric(key=acceptable)
        assert_raises(
            expected_error_class=ValueError,
            func_or_method=dict_1._validate_key_type_is_str_or_numeric,
            kwargs={'key': Boolean(True)},
            match='Unsupported key type is specified')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___getitem__(self) -> None:
        string_1: String = String('b')
        dict_1: Dictionary = Dictionary(
            value={'a': 10, 'b': 20, 3: 30, 4.5: 40})
        value: Any = dict_1['a']
        assert value == 10
        value = dict_1[string_1]
        assert value == 20
        value = dict_1[3]
        assert value == 30
        value = dict_1[4.5]

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_getitem_expression(self) -> None:
        expression_file_util.remove_expression_file()
        int_1: Int = Int(20)
        dict_1: Dictionary = Dictionary({'a': 10, 'b': int_1})
        _: Any = dict_1['a']
        expression: str = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'var {var_names.ANY}_.+? = '
                rf'{dict_1.variable_name}\["a"\];'
            ),
            string=expression, flags=re.MULTILINE)
        assert match is not None

        str_1: String = String('b')
        value: Any = dict_1[str_1]
        expression = expression_file_util.get_current_expression()
        expected: str = (
            f'var {value.variable_name} = '
            f'{dict_1.variable_name}[{str_1.variable_name}];'
        )
        assert expected in expression

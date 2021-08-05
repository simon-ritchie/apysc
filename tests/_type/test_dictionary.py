import re
from random import randint
from typing import Any
from typing import Dict
from typing import List
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._expression import expression_file_util
from apysc._expression import var_names
from apysc._type.any_value import AnyValue
from tests.testing_helper import assert_raises


class TestDictionary:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__validate_acceptable_value_type(self) -> None:
        dict_1: ap.Dictionary = ap.Dictionary(value={})
        _: ap.Dictionary = ap.Dictionary(value=dict_1)

        assert_raises(
            expected_error_class=TypeError,
            func_or_method=ap.Dictionary,
            kwargs={'value': 10},
            match='Not acceptable value type is specified')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_dict_value(self) -> None:
        dict_1: ap.Dictionary = ap.Dictionary(value={'a': 10})
        dict_val: Dict[Any, Any] = dict_1._get_dict_value(value={'a': 20})
        assert dict_val == {'a': 20}
        assert isinstance(dict_val, dict)

        dict_val = dict_1._get_dict_value(value=dict_1)
        assert dict_val == {'a': 10}
        assert isinstance(dict_val, dict)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_constructor_expression(self) -> None:
        expression_file_util.empty_expression_dir()
        dict_1: ap.Dictionary = ap.Dictionary(value={'a': 10})
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'var {dict_1.variable_name} = {{"a": 10}};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        dict_1: ap.Dictionary = ap.Dictionary(value={'a': 10})
        dict_2: ap.Dictionary = ap.Dictionary(value=dict_1)
        assert dict_2._initial_value == dict_1
        assert dict_2.type_name == var_names.DICTIONARY
        assert dict_2.variable_name.startswith(f'{var_names.DICTIONARY}_')
        assert dict_2._value == {'a': 10}

        assert_raises(
            expected_error_class=TypeError,
            func_or_method=ap.Dictionary,
            kwargs={'value': 10},
            match='Not acceptable value type is specified.')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_value(self) -> None:
        dict_1: ap.Dictionary = ap.Dictionary(value={'a': 10})
        assert dict_1.value == {'a': 10}

        dict_1.value = {'b': 20}
        assert dict_1.value == {'b': 20}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_value_setter_expression(self) -> None:
        expression_file_util.empty_expression_dir()
        dict_1: ap.Dictionary = ap.Dictionary(value={'a': 10})
        dict_1.value = {'b': 20}
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{dict_1.variable_name} = {{"b": 20}};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        dict_1: ap.Dictionary = ap.Dictionary(value={'a': 10})
        snapshot_name: str = dict_1._get_next_snapshot_name()
        dict_1._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert dict_1._value_snapshot == {snapshot_name: {'a': 10}}

        dict_1.value = {'b': 20}
        dict_1._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert dict_1._value_snapshot == {snapshot_name: {'a': 10}}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        dict_1: ap.Dictionary = ap.Dictionary(value={'a': 10})
        snapshot_name: str = dict_1._get_next_snapshot_name()
        dict_1._run_all_revert_methods(snapshot_name=snapshot_name)
        dict_1._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert dict_1.value == {'a': 10}

        dict_1._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        dict_1.value = {'b': 20}
        dict_1._run_all_revert_methods(snapshot_name=snapshot_name)
        assert dict_1.value == {'a': 10}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___str__(self) -> None:
        dict_1: ap.Dictionary = ap.Dictionary(value={'a': 10})
        assert str(dict_1) == "{'a': 10}"

        del dict_1._value
        assert str(dict_1) == '{}'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___repr__(self) -> None:
        dict_1: ap.Dictionary = ap.Dictionary(value={'a': 10})
        assert repr(dict_1) == "Dictionary({'a': 10})"

        del dict_1._value
        assert repr(dict_1) == 'Dictionary({})'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_length(self) -> None:
        dict_1: ap.Dictionary = ap.Dictionary(value={'a': 10, 'b': 20})
        length: ap.Int = dict_1.length
        assert length == 2
        assert isinstance(length, ap.Int)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_length_expression(self) -> None:
        expression_file_util.empty_expression_dir()
        dict_1: ap.Dictionary = ap.Dictionary(value={'a': 10, 'b': 20})
        length: ap.Int = dict_1.length
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{length.variable_name} = '
            f'Object.keys({dict_1.variable_name}).length;'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___len__(self) -> None:
        dict_1: ap.Dictionary = ap.Dictionary(value={'a': 10, 'b': 20})
        assert_raises(
            expected_error_class=Exception,
            func_or_method=dict_1.__len__,
            match='Dictionary instance can\'t apply len function.')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__validate_key_type_is_str_or_numeric(self) -> None:
        dict_1: ap.Dictionary = ap.Dictionary(value={'a': 10})
        acceptables: List[Any] = [
            'Hello', ap.String('Hello'), 10, ap.Int(10), 20.5, ap.Number(20.5)]
        for acceptable in acceptables:
            dict_1._validate_key_type_is_str_or_numeric(key=acceptable)
        assert_raises(
            expected_error_class=ValueError,
            func_or_method=dict_1._validate_key_type_is_str_or_numeric,
            kwargs={'key': ap.Boolean(True)},
            match='Unsupported key type is specified')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___getitem__(self) -> None:
        string_1: ap.String = ap.String('b')
        dict_1: ap.Dictionary = ap.Dictionary(
            value={'a': 10, 'b': 20, 3: 30, 4.5: 40})
        value: Any = dict_1['a']
        assert value == 10
        value = dict_1[string_1]
        assert value == 20
        value = dict_1[3]
        assert value == 30
        value = dict_1[4.5]

        value = dict_1['c']
        assert isinstance(value, AnyValue)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_getitem_expression(self) -> None:
        expression_file_util.empty_expression_dir()
        int_1: ap.Int = ap.Int(20)
        dict_1: ap.Dictionary = ap.Dictionary({'a': 10, 'b': int_1})
        _: Any = dict_1['a']
        expression: str = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'var {var_names.ANY}_.+? = '
                rf'{dict_1.variable_name}\["a"\];'
            ),
            string=expression, flags=re.MULTILINE)
        assert match is not None

        str_1: ap.String = ap.String('b')
        value: Any = dict_1[str_1]
        expression = expression_file_util.get_current_expression()
        expected: str = (
            f'var {value.variable_name} = '
            f'{dict_1.variable_name}[{str_1.variable_name}];'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___setitem__(self) -> None:
        dict_1: ap.Dictionary = ap.Dictionary({'a': 10})
        dict_1['b'] = 20
        assert dict_1['b'] == 20

        string_1: ap.String = ap.String('a')
        dict_1[string_1] = 30
        assert dict_1[string_1] == 30

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_setitem_expression(self) -> None:
        expression_file_util.empty_expression_dir()
        dict_1: ap.Dictionary = ap.Dictionary({'a': 10})
        string_1: ap.String = ap.String('b')
        dict_1[string_1] = 20
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{dict_1.variable_name}[{string_1.variable_name}] = 20;'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_builtin_type_key(self) -> None:
        dict_1: ap.Dictionary = ap.Dictionary({})
        key: Any = dict_1._get_builtin_type_key(key=ap.Int(10))
        assert isinstance(key, int)
        assert key == 10

        key = dict_1._get_builtin_type_key(key=20)
        assert isinstance(key, int)
        assert key == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___delitem__(self) -> None:
        dict_1: ap.Dictionary = ap.Dictionary({'a': 10})
        string_1: ap.String = ap.String('a')
        del dict_1[string_1]
        assert dict_1.value == {}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_delitem_expression(self) -> None:
        expression_file_util.empty_expression_dir()
        dict_1: ap.Dictionary = ap.Dictionary({'a': 10})
        string_1: ap.String = ap.String('a')
        del dict_1[string_1]
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'delete {dict_1.variable_name}[{string_1.variable_name}];'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_eq_expression(self) -> None:
        expression_file_util.empty_expression_dir()
        dict_1: ap.Dictionary = ap.Dictionary({'a': 10})
        dict_2: ap.Dictionary = ap.Dictionary({'a': 10})
        result: ap.Boolean = dict_1 == dict_2
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{result.variable_name} = '
            f'_.isEqual({dict_1.variable_name}, {dict_2.variable_name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___eq__(self) -> None:
        dict_1: ap.Dictionary = ap.Dictionary({'a': 10})
        dict_2: ap.Dictionary = ap.Dictionary({'a': 10})
        result: ap.Boolean = dict_1 == dict_2
        assert isinstance(result, ap.Boolean)
        assert result

        dict_3: ap.Dictionary = ap.Dictionary({'a': 20})
        result = dict_1 == dict_3
        assert not result

        result = dict_1 == {'a': 10}
        assert isinstance(result, ap.Boolean)
        assert result

        result = dict_1 == {'a': 20}
        assert not result

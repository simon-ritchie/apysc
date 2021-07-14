from random import randint

from retrying import retry

import apysc as ap
from apysc._type import value_util
from tests.testing_helper import assert_raises


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_value_str_for_expression() -> None:
    int_val: ap.Int = ap.Int(value=10)
    value_str: str = value_util.get_value_str_for_expression(
        value=int_val)
    assert value_str == int_val.variable_name

    value_str = value_util.get_value_str_for_expression(value=10)
    assert value_str == '10'

    value_str = value_util.get_value_str_for_expression(value=True)
    assert value_str == 'true'

    value_str = value_util.get_value_str_for_expression(value=False)
    assert value_str == 'false'

    value_str = value_util.get_value_str_for_expression(value='Hello!')
    assert value_str == '"Hello!"'

    value_str = value_util.get_value_str_for_expression(value=[10, 20])
    assert value_str == '[10, 20]'

    value_str = value_util.get_value_str_for_expression(value=(30, 40))
    assert value_str == '[30, 40]'

    value_str = value_util.get_value_str_for_expression(value={'key_1': 10})
    assert value_str == '{"key_1": 10}'

    value_str = value_util.get_value_str_for_expression(value=None)
    assert value_str == 'NaN'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_copy() -> None:
    int_val: ap.Int = ap.Int(value=10)
    copied_val_1: ap.Int = value_util.get_copy(value=int_val)
    assert int_val == copied_val_1
    assert int_val.variable_name != copied_val_1.variable_name

    copied_val_2: int = value_util.get_copy(value=100)
    assert copied_val_2 == 100


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_value_str_from_iterable() -> None:
    int_1: ap.Int = ap.Int(value=10)
    value_str: str = value_util._get_value_str_from_iterable(
        value=[100, True, int_1, (1000, 2000), 'Hello!'])
    expected: str = (
        f'[100, true, {int_1.variable_name}, [1000, 2000], "Hello!"]'
    )
    assert value_str == expected

    value_str = value_util._get_value_str_from_iterable(value=(10, 20))
    assert value_str == '[10, 20]'

    array_1: ap.Array = ap.Array([30, 40])
    value_str = value_util._get_value_str_from_iterable(value=array_1)
    assert value_str == '[30, 40]'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__validate_dict_key_type() -> None:
    value_util._validate_dict_key_type(key=10)
    value_util._validate_dict_key_type(key=10.5)
    value_util._validate_dict_key_type(key='Hello')
    assert_raises(
        expected_error_class=TypeError,
        func_or_method=value_util._validate_dict_key_type,
        kwargs={'key': ap.Int(10)},
        match='Dictionary key type only supports str and int')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_value_str_from_dict() -> None:
    value_str: str = value_util._get_value_str_from_dict(
        value={'key_1': 10, 20: 'Hello', 'key_3': [1, 2, 3]})
    assert value_str == '{"key_1": 10, "20": "Hello", "key_3": [1, 2, 3]}'

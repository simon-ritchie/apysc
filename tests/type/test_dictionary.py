from apysc.expression import expression_file_util
from random import randint
from typing import Any, Dict

from retrying import retry

from apysc import Dictionary
from tests.testing_helper import assert_raises


class TestDictionary:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__validate_acceptable_value_type(self) -> None:
        dict_1: Dictionary = Dictionary(value={})
        _: Dictionary = Dictionary(value=dict_1)

        assert_raises(
            expected_error_class=ValueError,
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

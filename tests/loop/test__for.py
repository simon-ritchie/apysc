from random import randint

from retrying import retry

from apysc import For, Array, Int
from apysc.expression import expression_file_util
from apysc.expression import indent_num
from tests import testing_helper


class TestFor:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___init__(self) -> None:
        arr: Array = Array([1, 2, 3])
        for_: For = For(
            arr=arr, locals_={'value_1': 1},
            globals_={'value_2': 2})
        testing_helper.assert_attrs(
            expected_attrs={
                '_arr': arr,
                '_locals': {'value_1': 1},
                '_globals': {'value_2': 2},
            },
            any_obj=for_)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_enter_expression(self) -> None:
        expression_file_util.remove_expression_file()
        arr: Array = Array([1, 2, 3])
        with For(arr, locals(), globals()) as i:
            pass
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'var length = {arr.variable_name}.length;'
        )
        assert expected in expression
        i_name: str = i.variable_name
        expected = (
            f'for ({i_name} = 0; {i_name} < length; {i_name}++) {{'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___enter__(self) -> None:
        indent_num.reset()
        arr: Array = Array([1, 2, 3])
        with For(arr, locals(), globals()) as i:
            current_indent_num: int = indent_num.get_current_indent_num()
            assert current_indent_num == 1
        assert isinstance(i, Int)

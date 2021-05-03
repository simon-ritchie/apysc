from random import randint

from retrying import retry

from apysc import Array
from apysc import For
from apysc import Int
from apysc.expression import expression_file_util
from apysc.expression import indent_num
from apysc.expression import last_scope
from apysc.expression.indent_num import Indent
from apysc.expression.last_scope import LastScope
from tests import testing_helper


class TestFor:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
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
        assert isinstance(for_._indent, Indent)

        for_ = For(arr=arr)
        testing_helper.assert_attrs(
            expected_attrs={
                '_locals': {},
                '_globals': {},
            },
            any_obj=for_)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
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

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___enter__(self) -> None:
        indent_num.reset()
        arr: Array = Array([1, 2, 3])
        with For(arr, locals(), globals()) as i:
            current_indent_num: int = indent_num.get_current_indent_num()
            assert current_indent_num == 1
        assert isinstance(i, Int)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___exit__(self) -> None:
        indent_num.reset()
        int_1: Int = Int(10)
        arr: Array = Array([1, 2, 3])
        with For(arr, locals(), globals()) as i:
            int_1.value = 20
        assert int_1.value == 10
        current_indent_num: int = indent_num.get_current_indent_num()
        assert current_indent_num == 0
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'  {int_1.variable_name} = 20;'
            '\n}'
        )
        assert expected in expression
        assert last_scope.get_last_scope() == LastScope.FOR

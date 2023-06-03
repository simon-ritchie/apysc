from typing import Any, Dict
import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import indent_num
from apysc._expression import last_scope
from apysc._expression.indent_num import Indent
from apysc._expression.last_scope import LastScope
from apysc._loop import loop_count
from apysc._testing import testing_helper
from apysc._testing.testing_helper import apply_test_settings, assert_attrs


class TestForArrayIndices:
    @apply_test_settings()
    def test___init__(self) -> None:
        arr: ap.Array[int] = ap.Array([10, 20])
        locals_: Dict[str, Any] = locals()
        globals_: Dict[str, Any] = globals()
        for_array_indices: ap.ForArrayIndices = ap.ForArrayIndices(
            arr=arr,
            locals_=locals_,
            globals_=globals_,
            variable_name_suffix="test_suffix",
        )
        assert_attrs(
            expected_attrs={
                "_arr": arr,
                "_locals": locals_,
                "_globals": globals_,
                "_variable_name_suffix": "test_suffix",
            },
            any_obj=for_array_indices,
        )

    @apply_test_settings()
    def test__append_enter_expression(self) -> None:
        expression_data_util.empty_expression()
        arr: ap.Array[int] = ap.Array([10, 20])
        i: ap.Int = ap.Int(0)
        for_array_indices: ap.ForArrayIndices = ap.ForArrayIndices(arr=arr)
        for_array_indices._append_enter_expression(i=i)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"for ({i.variable_name} = 0; {i.variable_name} < "
            f"{arr.variable_name}.length; {i.variable_name}++) {{"
        )
        assert expected in expression

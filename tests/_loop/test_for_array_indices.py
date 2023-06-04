from typing import Any
from typing import Dict

import apysc as ap
from apysc._expression import expression_data_util
from apysc._loop import loop_count
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs


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

    @apply_test_settings()
    def test___enter__(self) -> None:
        expression_data_util.empty_expression()
        arr: ap.Array[int] = ap.Array([10, 20])
        with ap.ForArrayIndices(arr=arr) as i:
            ap.append_js_expression("var test = 10;")
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"for ({i.variable_name} = 0; {i.variable_name} < "
            f"{arr.variable_name}.length;"
        )
        assert expected in expression

        expected = "  var test = 10;"
        assert expected in expression

    @apply_test_settings()
    def test___exit__(self) -> None:
        expression_data_util.empty_expression()
        arr: ap.Array[int] = ap.Array([10, 20])
        with ap.ForArrayIndices(arr=arr) as i:
            assert loop_count.get_current_loop_count() == 1
            ap.append_js_expression("var test = 10;")
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"for ({i.variable_name} = 0; {i.variable_name} < "
            f"{arr.variable_name}.length; {i.variable_name}++) {{"
            "\n  var test = 10;"
            "\n}"
        )
        assert expected in expression
        assert loop_count.get_current_loop_count() == 0

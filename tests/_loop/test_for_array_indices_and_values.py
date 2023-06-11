import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression.last_scope import LastScope
from apysc._loop import loop_count
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs


class TestForArrayIndicesAndValues:
    @apply_test_settings()
    def test___init__(self) -> None:
        arr: ap.Array[ap.Int] = ap.Array([ap.Int(10)])
        for_array_indices_and_values: ap.ForArrayIndicesAndValues = (
            ap.ForArrayIndicesAndValues(
                arr=arr,
                arr_value_type=ap.Int,
                locals_={"a": ap.Int(10)},
                globals_={"b": ap.Int(20)},
                variable_name_suffix="test_suffix",
            )
        )
        assert_attrs(
            expected_attrs={
                "_arr": arr,
                "_arr_value_type": ap.Int,
                "_locals": {"a": ap.Int(10)},
                "_globals": {"b": ap.Int(20)},
                "_variable_name_suffix": "test_suffix",
            },
            any_obj=for_array_indices_and_values,
        )

    @apply_test_settings()
    def test__get_last_scope(self) -> None:
        arr: ap.Array[ap.Int] = ap.Array([ap.Int(10)])
        for_array_indices_and_values: ap.ForArrayIndicesAndValues = (
            ap.ForArrayIndicesAndValues(
                arr=arr,
                arr_value_type=ap.Int,
            )
        )
        last_scope: LastScope = for_array_indices_and_values._get_last_scope()
        assert last_scope == LastScope.FOR_ARRAY_INDICES_AND_VALUES

    @apply_test_settings()
    def test___enter__(self) -> None:
        expression_data_util.empty_expression()
        arr: ap.Array[ap.String] = ap.Array([ap.String("a"), ap.String("b")])
        with ap.ForArrayIndicesAndValues(
            arr=arr, arr_value_type=ap.String
        ) as (i, value):
            ap.append_js_expression("console.log(10);")
            assert loop_count.get_current_loop_count() == 1
        assert isinstance(i, ap.Int)
        assert isinstance(value, ap.String)
        assert loop_count.get_current_loop_count() == 0
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"for ({i.variable_name} = 0; {i.variable_name} < "
            f"{arr.variable_name}.length; {i.variable_name}++) {{"
        )
        assert expected in expression

        expected = (
            f"  {value.variable_name} = {arr.variable_name}[{i.variable_name}];"
        )
        assert expected in expression


from typing import Any
from typing import Dict

import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression.last_scope import LastScope
from apysc._loop import loop_count
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs


class TestForArrayValues:
    @apply_test_settings()
    def test___init__(self) -> None:
        arr: ap.Array[ap.Int] = ap.Array([ap.Int(10), ap.Int(20)])
        for_array_values: ap.ForArrayValues = ap.ForArrayValues(
            arr=arr,
            locals_={"a": ap.Int(30)},
            globals_={"b": ap.Int(40)},
            variable_name_suffix="test_suffix",
        )
        assert_attrs(
            expected_attrs={
                "_arr": arr,
                "_variable_name_suffix": "test_suffix",
                "_locals": {"a": ap.Int(30)},
                "_globals": {"b": ap.Int(40)},
            },
            any_obj=for_array_values,
        )

    @apply_test_settings()
    def test__get_last_scope(self) -> None:
        arr: ap.Array[ap.Int] = ap.Array([ap.Int(10), ap.Int(20)])
        for_array_values: ap.ForArrayValues = ap.ForArrayValues(
            arr=arr,
        )
        last_scope: LastScope = for_array_values._get_last_scope()
        assert last_scope == LastScope.FOR_ARRAY_VALUES

import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression.indent_num import Indent
from apysc._expression.last_scope import LastScope
from apysc._loop import loop_count
from apysc._testing.testing_helper import apply_test_settings


class TestForDictValues:
    @apply_test_settings()
    def test___init__(self) -> None:
        dict_: ap.Dictionary[str, ap.Int] = ap.Dictionary(
            {
                "a": ap.Int(10),
                "b": ap.Int(20),
            },
        )
        for_dict_values: ap.ForDictValues = ap.ForDictValues(
            dict_=dict_,
            dict_value_type=ap.Int,
            locals_={"c": 10},
            globals_={"d": 20},
            variable_name_suffix="test_suffix",
        )
        assert for_dict_values._dict == dict_
        assert for_dict_values._dict_value_type == ap.Int
        assert for_dict_values._locals == {"c": 10}
        assert for_dict_values._globals == {"d": 20}
        assert for_dict_values._variable_name_suffix == "test_suffix"

    @apply_test_settings()
    def test__get_last_scope(self) -> None:
        dict_: ap.Dictionary[str, ap.Int] = ap.Dictionary(
            {
                "a": ap.Int(10),
                "b": ap.Int(20),
            },
        )
        for_dict_values: ap.ForDictValues = ap.ForDictValues(
            dict_=dict_,
            dict_value_type=ap.Int,
        )
        last_scope: LastScope = for_dict_values._get_last_scope()
        assert last_scope == LastScope.FOR_DICT_VALUES

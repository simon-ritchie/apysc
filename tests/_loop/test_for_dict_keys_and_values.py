import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression.last_scope import LastScope
from apysc._loop import loop_count
from apysc._testing.testing_helper import apply_test_settings


class TestForDictKeysAndValues:
    @apply_test_settings()
    def test___init__(self) -> None:
        dict_: ap.Dictionary[ap.String, ap.Int] = ap.Dictionary(
            {
                ap.String("a"): ap.Int(10),
                ap.String("b"): ap.Int(20),
            }
        )
        for_dict_keys_and_valus: ap.ForDictKeysAndValues = ap.ForDictKeysAndValues(
            dict_=dict_,
            dict_key_type=ap.String,
            dict_value_type=ap.Int,
            locals_={"c": 30},
            globals_={"d": 40},
            variable_name_suffix="test_suffix",
        )
        assert for_dict_keys_and_valus._locals == {"c": 30}
        assert for_dict_keys_and_valus._globals == {"d": 40}
        assert for_dict_keys_and_valus._dict_key_type == ap.String
        assert for_dict_keys_and_valus._dict_value_type == ap.Int
        assert for_dict_keys_and_valus._variable_name_suffix == "test_suffix"

    @apply_test_settings()
    def test__get_last_scope(self) -> None:
        dict_: ap.Dictionary[ap.String, ap.Int] = ap.Dictionary(
            {
                ap.String("a"): ap.Int(10),
            }
        )
        for_dict_keys_and_valus: ap.ForDictKeysAndValues = ap.ForDictKeysAndValues(
            dict_=dict_,
            dict_key_type=ap.String,
            dict_value_type=ap.Int,
        )
        last_scope: LastScope = for_dict_keys_and_valus._get_last_scope()
        assert last_scope == LastScope.FOR_DICT_KEYS_AND_VALUES

    @apply_test_settings()
    def test___enter__(self) -> None:
        dict_: ap.Dictionary[ap.String, ap.Int] = ap.Dictionary(
            {
                ap.String("a"): ap.Int(10),
                ap.String("b"): ap.Int(20),
            }
        )
        with ap.ForDictKeysAndValues(
            dict_=dict_,
            dict_key_type=ap.String,
            dict_value_type=ap.Int,
        ) as (key, value):
            assert isinstance(key, ap.String)
            assert isinstance(value, ap.Int)
            assert key == ap.String("")
            assert value == ap.Int(0)
            loop_count_: int = loop_count.get_current_loop_count()
            assert loop_count_ == 1
            ap.append_js_expression("console.log(10);")
        loop_count_ = loop_count.get_current_loop_count()
        assert loop_count_ == 0
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"for ({key.variable_name} in {dict_.variable_name}) {{"
            f"\n  {value.variable_name} = {dict_.variable_name}"
            f"[{key.variable_name}];"
        )
        assert expected in expression
        assert "\n  console.log(10);" in expression

import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression.indent_num import Indent
from apysc._expression.last_scope import LastScope
from apysc._loop import loop_count
from apysc._testing.testing_helper import apply_test_settings


class TestForDictKeys:
    @apply_test_settings()
    def test___init__(self) -> None:
        dict_: ap.Dictionary[ap.Int, str] = ap.Dictionary({ap.Int(10): "test"})
        for_dict_keys: ap.ForDictKeys = ap.ForDictKeys(
            dict_=dict_,
            dict_key_type=ap.Int,
            locals_={"a": 10},
            globals_={"b": 20},
            variable_name_suffix="test_suffix",
        )
        assert for_dict_keys._locals == {"a": 10}
        assert for_dict_keys._globals == {"b": 20}
        assert for_dict_keys._dict == dict_
        assert for_dict_keys._variable_name_suffix == "test_suffix"
        assert isinstance(for_dict_keys._indent, Indent)

    @apply_test_settings()
    def test__get_last_scope(self) -> None:
        dict_: ap.Dictionary[ap.Int, str] = ap.Dictionary({ap.Int(10): "test"})
        for_dict_keys: ap.ForDictKeys = ap.ForDictKeys(
            dict_=dict_,
            dict_key_type=ap.Int,
        )
        last_scope: LastScope = for_dict_keys._get_last_scope()
        assert last_scope == LastScope.FOR_DICT_KEYS

    @apply_test_settings()
    def test___enter__(self) -> None:
        ap.Stage()
        dict_: ap.Dictionary[ap.String, int] = ap.Dictionary(
            {
                ap.String("a"): 10,
                ap.String("b"): 20,
            }
        )
        with ap.ForDictKeys(dict_=dict_, dict_key_type=ap.String) as key:
            assert isinstance(key, ap.String)
            assert key == ap.String("")
            loop_count_: int = loop_count.get_current_loop_count()
            assert loop_count_ == 1
            ap.append_js_expression("console.log(10);")
        loop_count_ = loop_count.get_current_loop_count()
        assert loop_count_ == 0
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"for ({key.variable_name} in {dict_.variable_name}) {{"
        assert expected in expression
        assert "\n  console.log(10);" in expression

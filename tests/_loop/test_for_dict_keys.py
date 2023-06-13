import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._expression.indent_num import Indent
from apysc._expression.last_scope import LastScope


class TestForDictKeys:
    @apply_test_settings()
    def test___init__(self) -> None:
        dict_: ap.Dictionary[int, str] = ap.Dictionary({10: "test"})
        for_dict_keys: ap.ForDictKeys = ap.ForDictKeys(
            dict_=dict_,
            dict_key_type=int,
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
        dict_: ap.Dictionary[int, str] = ap.Dictionary({10: "test"})
        for_dict_keys: ap.ForDictKeys = ap.ForDictKeys(
            dict_=dict_,
            dict_key_type=int,
        )
        last_scope: LastScope = for_dict_keys._get_last_scope()
        assert last_scope == LastScope.FOR_DICT_KEYS

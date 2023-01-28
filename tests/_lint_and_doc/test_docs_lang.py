from random import randint

from retrying import retry

from apysc._lint_and_doc import docs_lang
from apysc._lint_and_doc.docs_lang import Lang
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test_langs_are_not_duplicated() -> None:
    values_set: set = set([lang.value for lang in Lang])
    assert len(values_set) == len(Lang)


@apply_test_settings()
def test_langs_values_are_str_type() -> None:
    for lang in Lang:
        assert isinstance(lang.value, str)


@apply_test_settings()
def test_get_lang_from_str_value() -> None:
    lang: Lang = docs_lang.get_lang_from_str_value(str_value=Lang.JP.value)
    assert lang == Lang.JP

from random import randint

from retrying import retry

from apysc._lint_and_doc.docs_lang import Lang
from apysc._lint_and_doc import docs_lang


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_langs_are_not_duplicated() -> None:
    values_set: set = set([lang.value for lang in Lang])
    assert len(values_set) == len(Lang)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_langs_values_are_str_type() -> None:
    for lang in Lang:
        assert isinstance(lang.value, str)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_lang_from_str_value() -> None:
    lang: Lang = docs_lang.get_lang_from_str_value(
        str_value=Lang.JP.value)
    assert lang == Lang.JP

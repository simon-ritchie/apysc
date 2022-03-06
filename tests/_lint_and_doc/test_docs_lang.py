from random import randint

from retrying import retry

from apysc._lint_and_doc.docs_lang import Lang


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_langs_are_not_duplicated() -> None:
    values_set: set = set([lang.value for lang in Lang])
    assert len(values_set) == len(Lang)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_langs_values_are_str_type() -> None:
    for lang in Lang:
        assert isinstance(lang.value, str)

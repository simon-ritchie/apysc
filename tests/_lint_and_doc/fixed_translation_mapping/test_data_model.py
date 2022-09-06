import os
from enum import Enum
from random import randint
from typing import List
from typing import Optional

from retrying import retry

from apysc._file import file_util
from apysc._lint_and_doc.docs_lang import Lang
from apysc._lint_and_doc.fixed_translation_mapping import data_model
from apysc._lint_and_doc.fixed_translation_mapping.data_model import (
    _UnsupportedLanguageException
)
from apysc._lint_and_doc.fixed_translation_mapping import jp
from apysc._lint_and_doc.fixed_translation_mapping.data_model import Mapping
from apysc._lint_and_doc.fixed_translation_mapping.data_model import Mappings
from apysc._testing.testing_helper import assert_attrs, assert_raises
from apysc._lint_and_doc import lint_and_doc_hash_util
from apysc._lint_and_doc.lint_and_doc_hash_util import HashType


class TestMapping:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        base: Mapping = Mapping(key="Lorem", val="ipsum")
        assert_attrs(
            expected_attrs={
                "_key": "Lorem",
                "_val": "ipsum",
            },
            any_obj=base,
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_key(self) -> None:
        base: Mapping = Mapping(key="Lorem", val="ipsum")
        assert base.key == "Lorem"

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_value(self) -> None:
        base: Mapping = Mapping(key="Lorem", val="ipsum")
        assert base.val == "ipsum"


class TestMappings:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__init__(self) -> None:
        mappings_list: List[Mapping] = [
            Mapping(key="Lorem", val="ipsum"),
        ]
        mappings: Mappings = Mappings(mappings=mappings_list)
        assert_attrs(
            expected_attrs={
                "mappings": mappings_list,
            },
            any_obj=mappings,
        )


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_mappings_module_path_from_lang() -> None:
    module_path: str = data_model._get_mappings_module_path_from_lang(lang=Lang.JP)
    assert module_path.endswith("jp.py")
    assert os.path.isfile(module_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__read_mappings() -> None:
    class _MockLang(Enum):
        NOT_EXISTING_LANG = "not_existing_lang"

    test_module_path: str = data_model._get_mappings_module_path_from_lang(
        lang=_MockLang.NOT_EXISTING_LANG  # type: ignore
    )
    file_util.remove_file_if_exists(file_path=test_module_path)

    mappings: Optional[Mappings] = data_model._read_mappings(
        lang=_MockLang.NOT_EXISTING_LANG
    )
    assert mappings is None

    file_util.save_plain_txt(txt="", file_path=test_module_path)
    mappings = data_model._read_mappings(lang=_MockLang.NOT_EXISTING_LANG)
    assert mappings is None

    mappings = data_model._read_mappings(lang=Lang.JP)
    assert mappings == jp.MAPPINGS

    file_util.remove_file_if_exists(file_path=test_module_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_fixed_translation_str_if_exists() -> None:
    class _MockLang(Enum):
        NOT_EXISTING_LANG = "not_existing_lang"

    translation_str: str = data_model.get_fixed_translation_str_if_exists(
        key="**[Parameters]**", lang=_MockLang.NOT_EXISTING_LANG  # type: ignore
    )
    assert translation_str == ""

    translation_str = data_model.get_fixed_translation_str_if_exists(
        key="not existing key", lang=Lang.JP
    )
    assert translation_str == ""

    translation_str = data_model.get_fixed_translation_str_if_exists(
        key="**[Parameters]**", lang=Lang.JP
    )
    assert translation_str == "**[引数]**"


@retry(stop_max_attempt_number=1, wait_fixed=randint(10, 3000))
def test_check_mapping_keys_not_duplicated() -> None:
    for lang in Lang:
        mappings: Optional[Mappings] = data_model._read_mappings(lang=lang)
        if mappings is None:
            continue
        keys: List[str] = []
        for mapping in mappings.mappings:
            if mapping.key in keys:
                raise AssertionError(
                    "There is a duplicated mapping's key."
                    f"\nLanguage: {lang}"
                    f"\nTarget key: {mapping.key}"
                )
            keys.append(mapping.key)


@retry(stop_max_attempt_number=1, wait_fixed=randint(10, 3000))
def test__get_fixed_mapping_hash_type() -> None:
    hash_type: HashType = data_model._get_fixed_mapping_hash_type(lang=Lang.JP)
    assert hash_type == HashType.TRANSLATION_FIXED_MAPPING_JP

    assert_raises(
        expected_error_class=_UnsupportedLanguageException,
        callable_=data_model._get_fixed_mapping_hash_type,
        lang=Lang.EN,
    )

    for lang in Lang:
        if lang == Lang.EN:
            continue
        _ = data_model._get_fixed_mapping_hash_type(lang=Lang.JP)


@retry(stop_max_attempt_number=1, wait_fixed=randint(10, 3000))
def test_is_fixed_mapping_updated() -> None:
    module_path: str = data_model._get_mappings_module_path_from_lang(lang=Lang.JP)
    os.system(f"git checkout {module_path}")

    lint_and_doc_hash_util.delete_target_file_hash(
        file_path=module_path, hash_type=HashType.TRANSLATION_FIXED_MAPPING_JP
    )
    result: bool = data_model.is_fixed_mapping_updated(lang=Lang.JP)
    assert result

    lint_and_doc_hash_util.save_target_file_hash(
        file_path=module_path,
        hash_type=HashType.TRANSLATION_FIXED_MAPPING_JP,
    )
    result = data_model.is_fixed_mapping_updated(lang=Lang.JP)
    assert not result

    os.system(f"git checkout {module_path}")

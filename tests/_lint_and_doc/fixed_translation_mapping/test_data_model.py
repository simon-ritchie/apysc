import os
from enum import Enum
from random import randint
from typing import List
from typing import Optional

from retrying import retry

from apysc._file import file_util
from apysc._lint_and_doc.docs_lang import Lang
from apysc._lint_and_doc.fixed_translation_mapping import data_model
from apysc._lint_and_doc.fixed_translation_mapping import jp
from apysc._lint_and_doc.fixed_translation_mapping.data_model import Mapping
from apysc._lint_and_doc.fixed_translation_mapping.data_model import Mappings
from tests.testing_helper import assert_attrs


class TestMapping:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        base: Mapping = Mapping(key='Lorem', val='ipsum')
        assert_attrs(
            expected_attrs={
                '_key': 'Lorem',
                '_val': 'ipsum',
            },
            any_obj=base)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_key(self) -> None:
        base: Mapping = Mapping(key='Lorem', val='ipsum')
        assert base.key == 'Lorem'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_value(self) -> None:
        base: Mapping = Mapping(key='Lorem', val='ipsum')
        assert base.val == 'ipsum'


class TestMappings:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__init__(self) -> None:
        mappings_list: List[Mapping] = [
            Mapping(key='Lorem', val='ipsum'),
        ]
        mappings: Mappings = Mappings(
            mappings=mappings_list)
        assert_attrs(
            expected_attrs={
                'mappings': mappings_list,
            },
            any_obj=mappings,
        )


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_mappings_module_path_from_lang() -> None:
    module_path: str = data_model._get_mappings_module_path_from_lang(
        lang=Lang.JP)
    assert module_path.endswith('jp.py')
    assert os.path.isfile(module_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__read_mappings() -> None:

    class _MockLang(Enum):
        NOT_EXISTING_LANG = 'not_existing_lang'

    test_module_path: str = data_model._get_mappings_module_path_from_lang(
        lang=_MockLang.NOT_EXISTING_LANG)  # type: ignore
    file_util.remove_file_if_exists(file_path=test_module_path)

    mappings: Optional[Mappings] = data_model._read_mappings(
        lang=_MockLang.NOT_EXISTING_LANG)  # type: ignore
    assert mappings is None

    file_util.save_plain_txt(
        txt='', file_path=test_module_path)
    mappings = data_model._read_mappings(
        lang=_MockLang.NOT_EXISTING_LANG)  # type: ignore
    assert mappings is None

    mappings = data_model._read_mappings(lang=Lang.JP)
    assert mappings == jp.MAPPINGS

    file_util.remove_file_if_exists(file_path=test_module_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_fixed_translation_str_if_exists() -> None:

    class _MockLang(Enum):
        NOT_EXISTING_LANG = 'not_existing_lang'

    translation_str: str = data_model.get_fixed_translation_str_if_exists(
        key='**[Parameters]**',
        lang=_MockLang.NOT_EXISTING_LANG)  # type: ignore
    assert translation_str == ''

    translation_str = data_model.get_fixed_translation_str_if_exists(
        key='not existing key', lang=Lang.JP)
    assert translation_str == ''

    translation_str = data_model.get_fixed_translation_str_if_exists(
        key='**[Parameters]**', lang=Lang.JP)
    assert translation_str == '**[引数]**'

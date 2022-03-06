import os
from random import randint

from retrying import retry

from apysc._file import file_util
from apysc._lint_and_doc import docs_translation_converter
from apysc._lint_and_doc import translation_mapping_utils
from apysc._lint_and_doc.docs_lang import Lang
from apysc._lint_and_doc.docs_translation_converter import \
    _TranslationMappingNotFound
from tests.testing_helper import assert_raises


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__validate_translated_str_is_not_blank() -> None:
    docs_translation_converter._validate_translated_str_is_not_blank(
        translated_str='Lorem  ipsum dolor sit.',
        key='Test key.',
        md_file_path='./test/file/path.md')

    assert_raises(
        expected_error_class=_TranslationMappingNotFound,
        func_or_method=docs_translation_converter.
        _validate_translated_str_is_not_blank,
        kwargs={
            'translated_str': '',
            'key': 'Test key.',
            'md_file_path': './test/file/path.md',
        },
        match='There is no translation mapping.')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_apply_translation_to_doc() -> None:
    md_file_path: str = './docs_src/source/sprite.md'
    expected_translated_file_path: str = translation_mapping_utils.\
        get_translated_file_path_from_src_path(
            source_doc_path=md_file_path, lang=Lang.JP)
    file_util.remove_file_if_exists(
        file_path=expected_translated_file_path)

    translated_file_path: str = docs_translation_converter.\
        apply_translation_to_doc(
            md_file_path='./docs_src/source/sprite.md',
            lang=Lang.JP)
    assert translated_file_path == expected_translated_file_path
    assert os.path.isfile(translated_file_path)
    assert translated_file_path == './docs_src/source/jp_sprite.md'
    translated_doc_str: str = file_util.read_txt(
        file_path=translated_file_path)
    assert 'このページでは、`Sprite`クラスについて説明します。' \
        in translated_doc_str


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__add_heading_info_if_exists() -> None:
    translated_doc: str = docs_translation_converter.\
        _add_heading_info_if_exists(
            translated_doc='',
            lang='Invalid lang',  # type: ignore
            md_file_path='./docs_src/source/test_doc.md')
    assert translated_doc == ''

    translated_doc = docs_translation_converter.\
        _add_heading_info_if_exists(
            translated_doc='',
            lang=Lang.JP,
            md_file_path='./docs_src/source/test_doc.md')
    assert '※この翻訳ドキュメントは' in translated_doc
    assert '[英語の原文](./docs_src/source/test_doc.md)' \
        in translated_doc

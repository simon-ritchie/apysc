import os
from random import randint

from retrying import retry

from apysc._file import file_util
from apysc._lint_and_doc import docs_translation_converter
from apysc._lint_and_doc import translation_mapping_utils
from apysc._lint_and_doc.docs_lang import Lang
from apysc._lint_and_doc.docs_translation_converter import \
    _InvalidHeadingSharpSymbolNumber
from apysc._lint_and_doc.docs_translation_converter import \
    _TranslationMappingNotFound, _HeadingSuffixIsNotLanguage
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


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__apply_mapping_if_translated_str_is_api_sig() -> None:
    src_translated_str: str = (
        '**[Interface signature]** `__init__(self, *, '
        'variable_name:Union[str, NoneType]=None) -> None`<hr>'
    )
    translated_str: str = docs_translation_converter.\
        _apply_mapping_if_translated_str_is_api_sig(
            translated_str=src_translated_str,
            lang='Invalid lang')  # type: ignore
    assert translated_str == src_translated_str

    translated_str = docs_translation_converter.\
        _apply_mapping_if_translated_str_is_api_sig(
            translated_str='Lorem ipsum',
            lang=Lang.JP)
    assert translated_str == 'Lorem ipsum'

    translated_str = docs_translation_converter.\
        _apply_mapping_if_translated_str_is_api_sig(
            translated_str=src_translated_str,
            lang=Lang.JP)
    assert translated_str == (
        '**[インターフェイスの構造]** `__init__(self, *, '
        'variable_name:Union[str, NoneType]=None) -> None`<hr>'
    )


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_sharp_heading_symbol_num() -> None:
    sharp_symbol_num: int = docs_translation_converter.\
        _get_sharp_heading_symbol_num(target_str='Lorem ipsum')
    assert sharp_symbol_num == 0

    sharp_symbol_num = docs_translation_converter.\
        _get_sharp_heading_symbol_num(target_str='## Lorem ipsum')
    assert sharp_symbol_num == 2


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__validate_sharp_heading_symbol_num_are_same() -> None:
    docs_translation_converter._validate_sharp_heading_symbol_num_are_same(
        translated_str='## テストテキスト',
        key='## Lorem ipsum',
        md_file_path='./test/source/path.md')

    assert_raises(
        expected_error_class=_InvalidHeadingSharpSymbolNumber,
        func_or_method=docs_translation_converter.
        _validate_sharp_heading_symbol_num_are_same,
        kwargs={
            'translated_str': 'テストテキスト',
            'key': '## Lorem ipsum',
            'md_file_path': './test/source/path.md',
        },
        match='There is a difference between source document')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__validate_heading_tail_is_language() -> None:
    docs_translation_converter._validate_heading_tail_is_language(
        translated_str='テストテキスト',
        key='Lorem ipsum',
        md_file_path='./test/source/path.md')

    docs_translation_converter._validate_heading_tail_is_language(
        translated_str='テストテキスト (Japanese)',
        key='Lorem ipsum (English)',
        md_file_path='./test/source/path.md')

    assert_raises(
        expected_error_class=_HeadingSuffixIsNotLanguage,
        func_or_method=docs_translation_converter.
        _validate_heading_tail_is_language,
        kwargs={
            'translated_str': '# テストテキスト',
            'key': 'Lorem ipsum (English)',
            'md_file_path': './test/source/path.md',
        },
        match='A source document or translated string\'s '
              'heading tail is not a language')
    assert_raises(
        expected_error_class=_HeadingSuffixIsNotLanguage,
        func_or_method=docs_translation_converter.
        _validate_heading_tail_is_language,
        kwargs={
            'translated_str': '# テストテキスト (Japanese)',
            'key': 'Lorem ipsum',
            'md_file_path': './test/source/path.md',
        },
        match='A source document or translated string\'s '
              'heading tail is not a language')

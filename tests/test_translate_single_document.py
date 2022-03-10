import os
from random import randint

from retrying import retry

from scripts import translate_single_document
from scripts.translate_single_document import _SourceFileNotFound, _SourceFileIsNotEnglish, _UndefinedLanguage
from tests.testing_helper import assert_raises
from apysc._lint_and_doc import lint_and_doc_hash_util
from apysc._lint_and_doc.lint_and_doc_hash_util import HashType
from apysc._lint_and_doc.docs_lang import Lang

_TEST_DOC_SRC_PATH: str = './docs_src/source/sprite.md'
_TEST_HASH_FILE_PATH: str = lint_and_doc_hash_util.\
    get_target_file_hash_file_path(
        file_path=_TEST_DOC_SRC_PATH,
        hash_type=HashType.TRANSLATION_MAPPING_JP)


def teardown() -> None:
    """
    The function would be called when the test ended.
    """
    os.system(f'git checkout {_TEST_HASH_FILE_PATH}')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__validate_src_option() -> None:
    assert_raises(
        expected_error_class=_SourceFileNotFound,
        func_or_method=translate_single_document._validate_src_option,
        kwargs={'src': 'docs_src/source/not_existing_doc.md'},
        match=(
            'There is no such source file: '
            'docs_src/source/not_existing_doc.md'
        ))

    assert_raises(
        expected_error_class=_SourceFileIsNotEnglish,
        func_or_method=translate_single_document._validate_src_option,
        kwargs={'src': 'docs_src/source/jp_sprite.md'},
        match=(
            f'not an English document: docs_src/source/jp_sprite.md'
        ))

    translate_single_document._validate_src_option(
        src='docs_src/source/sprite.md')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__validate_lang_option() -> None:
    translate_single_document._validate_lang_option(lang='jp')

    assert_raises(
        expected_error_class=_UndefinedLanguage,
        func_or_method=translate_single_document._validate_lang_option,
        kwargs={'lang': 'invalid_lang'},
        match='A specified language string is undefined')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__delete_translation_mapping_hash() -> None:
    lint_and_doc_hash_util.save_target_file_hash(
        file_path=_TEST_DOC_SRC_PATH,
        hash_type=HashType.TRANSLATION_MAPPING_JP)
    translate_single_document._delete_translation_mapping_hash(
        lang=Lang.JP, src_file_path=_TEST_DOC_SRC_PATH)
    assert not os.path.exists(_TEST_HASH_FILE_PATH)

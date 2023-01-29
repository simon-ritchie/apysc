import os

from apysc._lint_and_doc import lint_and_doc_hash_util
from apysc._lint_and_doc.docs_lang import Lang
from apysc._lint_and_doc.lint_and_doc_hash_util import HashType
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises
from scripts import translate_single_document
from scripts.translate_single_document import _InvalidDocBuildStatusCode
from scripts.translate_single_document import _SourceFileIsNotEnglish
from scripts.translate_single_document import _SourceFileNotFound
from scripts.translate_single_document import _UndefinedLanguage

_TEST_DOC_SRC_PATH: str = "./docs_src/source/sprite.md"
_TEST_HASH_FILE_PATH_1: str = lint_and_doc_hash_util.get_target_file_hash_file_path(
    file_path=_TEST_DOC_SRC_PATH, hash_type=HashType.TRANSLATION_MAPPING_JP
)
_TEST_HASH_FILE_PATH_2: str = lint_and_doc_hash_util.get_target_file_hash_file_path(
    file_path=_TEST_DOC_SRC_PATH, hash_type=HashType.APPLYING_TRANSLATION_MAPPING
)


def teardown() -> None:
    os.system(f"git checkout {_TEST_HASH_FILE_PATH_1}")
    os.system(f"git checkout {_TEST_HASH_FILE_PATH_2}")


@apply_test_settings()
def test__validate_src_option() -> None:
    assert_raises(
        expected_error_class=_SourceFileNotFound,
        callable_=translate_single_document._validate_src_option,
        match=("There is no such source file: " "docs_src/source/not_existing_doc.md"),
        src="docs_src/source/not_existing_doc.md",
    )

    assert_raises(
        expected_error_class=_SourceFileIsNotEnglish,
        callable_=translate_single_document._validate_src_option,
        match=("not an English document: docs_src/source/jp_sprite.md"),
        src="docs_src/source/jp_sprite.md",
    )

    translate_single_document._validate_src_option(src="docs_src/source/sprite.md")


@apply_test_settings()
def test__validate_lang_option() -> None:
    translate_single_document._validate_lang_option(lang="jp")

    assert_raises(
        expected_error_class=_UndefinedLanguage,
        callable_=translate_single_document._validate_lang_option,
        match="A specified language string is undefined",
        lang="invalid_lang",
    )


@apply_test_settings()
def test__delete_translation_mapping_hash() -> None:
    lint_and_doc_hash_util.save_target_file_hash(
        file_path=_TEST_DOC_SRC_PATH, hash_type=HashType.TRANSLATION_MAPPING_JP
    )
    lint_and_doc_hash_util.save_target_file_hash(
        file_path=_TEST_DOC_SRC_PATH, hash_type=HashType.APPLYING_TRANSLATION_MAPPING
    )
    translate_single_document._delete_translation_mapping_hash(
        lang=Lang.JP, src_file_path=_TEST_DOC_SRC_PATH
    )
    assert not os.path.exists(_TEST_HASH_FILE_PATH_1)
    assert not os.path.exists(_TEST_HASH_FILE_PATH_2)

    os.system(f"git checkout {_TEST_HASH_FILE_PATH_1}")
    os.system(f"git checkout {_TEST_HASH_FILE_PATH_2}")


@apply_test_settings()
def test__validate_build_doc_command_status_code() -> None:
    translate_single_document._validate_build_doc_command_status_code(status_code=0)

    assert_raises(
        expected_error_class=_InvalidDocBuildStatusCode,
        callable_=translate_single_document._validate_build_doc_command_status_code,
        match="A document's build command status code is not zero: 1",
        status_code=1,
    )

    os.system(f"git checkout {_TEST_HASH_FILE_PATH_1}")
    os.system(f"git checkout {_TEST_HASH_FILE_PATH_2}")

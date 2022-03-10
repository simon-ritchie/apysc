from random import randint

from retrying import retry

from scripts import translate_single_document
from scripts.translate_single_document import _SourceFileNotFound, _SourceFileIsNotEnglish, _UndefinedLanguage
from tests.testing_helper import assert_raises


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

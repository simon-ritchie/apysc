from random import randint

from retrying import retry

from apysc._lint_and_doc import docs_translation_converter
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

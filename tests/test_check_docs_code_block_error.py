from random import randint
from typing import List

from retrying import retry

from apysc._file import file_util
from apysc._testing.testing_helper import assert_raises
from scripts import check_docs_code_block_error
from scripts.check_docs_code_block_error import _CodeBlockError


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__target_file_is_translated_document() -> None:
    result: bool = check_docs_code_block_error.\
        _target_file_is_translated_document(file_name='jp_sprite.md')
    assert result

    result = check_docs_code_block_error.\
        _target_file_is_translated_document(file_name='sprite.md')
    assert not result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_target_document_file_paths() -> None:
    document_file_paths: List[str] = check_docs_code_block_error.\
        _get_target_document_file_paths(alphabets_group=['i', 'j'])
    assert './docs_src/source/import_conventions.md' in document_file_paths
    assert './docs_src/source/jp_sprite.md' not in document_file_paths
    assert './docs_src/source/sprite.md' not in document_file_paths
    assert './docs_src/source/_static/' not in document_file_paths


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__run_document_code_blocks() -> None:
    test_md_file_path: str = './tmp/test_check_docs_code_block_error_1.md'
    file_util.save_plain_txt(
        txt=(
            '```py'
            '\n# runnable'
            "\nraise Exception('Test error!')"
            '\n```'
        ),
        file_path=test_md_file_path)
    assert_raises(
        expected_error_class=_CodeBlockError,
        callable_=check_docs_code_block_error._run_document_code_blocks,
        match='There is an exception in the code block execution.',
        document_file_path=test_md_file_path,)
    file_util.remove_file_if_exists(file_path=test_md_file_path)

    check_docs_code_block_error._run_document_code_blocks(
        document_file_path='./docs_src/source/sprite.md')

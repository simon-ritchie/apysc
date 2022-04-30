from random import randint
from typing import List

from retrying import retry

from apysc._lint_and_doc import document_util


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_docs_md_file_paths() -> None:
    file_paths: List[str] = document_util.get_docs_md_file_paths()
    expected_file_paths: List[str] = [
        './docs_src/source/index.md',
        './docs_src/source/sprite.md',
        './docs_src/source/jp_index.md',
    ]
    for expected_file_path in expected_file_paths:
        assert expected_file_path in file_paths

    assert './docs_src/source/conf_en' not in file_paths

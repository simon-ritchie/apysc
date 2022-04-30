from random import randint
from typing import List

from retrying import retry

from apysc._lint_and_doc import document_util
from apysc._lint_and_doc.docs_lang import Lang


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_docs_md_file_paths() -> None:
    file_paths: List[str] = document_util.get_docs_md_file_paths()
    expected_file_paths: List[str] = [
        '/mnt/apysc/docs_src/source/index.md',
        '/mnt/apysc/docs_src/source/sprite.md',
        '/mnt/apysc/docs_src/source/jp_index.md',
    ]
    for expected_file_path in expected_file_paths:
        assert expected_file_path in file_paths

    assert '/mnt/apysc/docs_src/source/conf_en' not in file_paths


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_exclude_patterns() -> None:
    patterns: List[str] = document_util.get_exclude_patterns(lang=Lang.EN)
    assert 'jp_*.md' in patterns

    patterns = document_util.get_exclude_patterns(lang=Lang.JP)
    assert 'sprite.md' in patterns
    assert 'jp_sprite.md' not in patterns

from typing import List

from apysc._lint_and_doc import document_util
from apysc._lint_and_doc.docs_lang import Lang
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test_get_docs_md_file_paths() -> None:
    file_paths: List[str] = document_util.get_docs_md_file_paths()
    expected_file_paths: List[str] = [
        "docs_src/source/index.md",
        "docs_src/source/sprite.md",
        "docs_src/source/jp_index.md",
    ]
    for expected_file_path in expected_file_paths:
        expected_path_exists: bool = False
        for file_path in file_paths:
            if file_path.endswith(expected_file_path):
                expected_path_exists = True
                break
        assert expected_path_exists, expected_file_path


@apply_test_settings()
def test_get_exclude_patterns() -> None:
    patterns: List[str] = document_util.get_exclude_patterns(lang=Lang.EN)
    assert "jp_*.md" in patterns

    patterns = document_util.get_exclude_patterns(lang=Lang.JP)
    assert "sprite.md" in patterns
    assert "jp_sprite.md" not in patterns


@apply_test_settings()
def test__get_src_dir_path() -> None:
    src_dir_path: str = document_util._get_src_dir_path()
    assert src_dir_path.endswith("/docs_src/source/")

import os
from random import randint
from typing import List

from retrying import retry

from apysc._lint_and_doc.docs_keyword_link_mapping import MAPPINGS
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test_check_mappings_are_not_duplicated() -> None:
    keys: List[str] = list(MAPPINGS.keys())
    for key in keys:
        assert keys.count(key) == 1, key


@apply_test_settings()
def test_check_keys_not_contain_spaces() -> None:
    keys: List[str] = list(MAPPINGS.keys())
    for key in keys:
        assert key == key.strip()


@apply_test_settings()
def test_check_doc_files_exist() -> None:
    for doc_file_name in MAPPINGS.values():
        assert os.path.exists(f"./docs_src/source/{doc_file_name}.md"), doc_file_name

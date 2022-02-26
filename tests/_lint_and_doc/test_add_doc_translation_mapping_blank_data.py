from random import randint
from typing import List

from retrying import retry

from apysc._lint_and_doc import add_doc_translation_mapping_blank_data


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_src_docs_file_paths() -> None:
    src_docs_file_paths: List[str] = add_doc_translation_mapping_blank_data.\
        _get_src_docs_file_paths()
    assert './docs_src/source/sprite.md' in src_docs_file_paths
    assert './docs_src/source/_static/' not in src_docs_file_paths
    assert './docs_src/source/jp_sprite.md' not in src_docs_file_paths
    assert './docs_src/source/conf.py' not in src_docs_file_paths

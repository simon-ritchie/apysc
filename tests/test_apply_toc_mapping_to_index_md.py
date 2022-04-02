from random import randint
from typing import List
import os

from retrying import retry

from scripts import apply_toc_mapping_to_index_md


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_target_module_paths() -> None:
    module_paths: List[str] = apply_toc_mapping_to_index_md.\
        _get_target_module_paths()
    assert './docs_src/source/index.md' in module_paths
    if os.path.exists('./docs_src/source/jp_index.md'):
        assert './docs_src/source/jp_index.md' in module_paths

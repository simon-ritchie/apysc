from random import randint
from typing import List
import os

from retrying import retry

from scripts import apply_toc_mapping_to_index_md


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_target_html_paths() -> None:
    html_paths: List[str] = apply_toc_mapping_to_index_md.\
        _get_target_html_paths()
    assert './docs/index.html' in html_paths
    if os.path.exists('./docs/jp_index.html'):
        assert './docs/jp_index.html' in html_paths

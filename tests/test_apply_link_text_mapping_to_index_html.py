import os
from random import randint
from typing import List

from retrying import retry

from scripts import apply_link_text_mapping_to_index_html


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_target_html_paths() -> None:
    html_paths: List[str] = apply_link_text_mapping_to_index_html.\
        _get_target_html_paths()
    assert './docs/index.html' in html_paths
    if os.path.exists('./docs/jp_index.html'):
        assert './docs/jp_index.html' in html_paths

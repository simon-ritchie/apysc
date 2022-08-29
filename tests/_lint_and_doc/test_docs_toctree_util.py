import os
from random import randint
from typing import List

from retrying import retry

from apysc._lint_and_doc import docs_toctree_util


# @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__extract_toctree_file_names_from_file() -> None:
    toctree_file_names: List[str] = (
        docs_toctree_util._extract_toctree_file_names_from_file(
            toctree_defined_en_file_name="index",
        )
    )
    assert "what_apysc_can_do.md" in toctree_file_names
    assert "recommended_type_checker_settings.md" in toctree_file_names
    assert "stage.md" in toctree_file_names
    for toctree_file_name in toctree_file_names:
        assert os.path.exists(f"./docs_src/source/{toctree_file_name}")

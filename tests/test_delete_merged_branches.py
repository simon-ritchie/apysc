from random import randint
from typing import List

from retrying import retry

from scripts import delete_merged_branches


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_merged_branch_names() -> None:
    merged_branch_names: List[str] = delete_merged_branches._get_merged_branch_names()
    for merged_branch_name in merged_branch_names:
        assert merged_branch_name.startswith("#")

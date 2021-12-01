from random import randint
from typing import List

from retrying import retry

import apysc as ap


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_path_labels_type() -> None:
    for path_label in ap.PathLabel:
        assert isinstance(path_label.value, str)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_path_labels_not_duplicated() -> None:
    labels: List[str] = [
        path_label.value for path_label in ap.PathLabel]
    assert len(labels) == len(set(set(labels)))

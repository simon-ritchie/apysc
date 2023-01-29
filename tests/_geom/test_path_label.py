from typing import List

import apysc as ap
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test_path_labels_type() -> None:
    for path_label in ap.PathLabel:
        assert isinstance(path_label.value, str)


@apply_test_settings()
def test_path_labels_not_duplicated() -> None:
    labels: List[str] = [path_label.value for path_label in ap.PathLabel]
    assert len(labels) == len(set(set(labels)))

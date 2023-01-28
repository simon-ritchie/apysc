from random import randint
from typing import List
from typing import Optional

from retrying import retry

from apysc._lint_and_doc.docs_lang import Lang
from apysc._testing.e2e_testing_helper import LocalFileData
from scripts import run_docs_e2e_tests
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test__get_file_names() -> None:
    file_names: List[str] = run_docs_e2e_tests._get_file_names(lang=Lang.EN)
    expected_file_names: List[str] = [
        "index",
        "sprite",
    ]
    for expected_file_name in expected_file_names:
        assert expected_file_name in file_names
    unexpected_file_names: List[str] = [
        "jp_index",
        "jp_sprite",
    ]
    for unexpected_file_name in unexpected_file_names:
        assert unexpected_file_name not in file_names

    file_names = run_docs_e2e_tests._get_file_names(lang=Lang.JP)
    expected_file_names = [
        "jp_index",
        "jp_sprite",
    ]
    for expected_file_name in expected_file_names:
        assert expected_file_name in file_names
    unexpected_file_names = [
        "index",
        "sprite",
    ]
    for unexpected_file_name in unexpected_file_names:
        assert unexpected_file_name not in file_names


@apply_test_settings()
def test__get_expected_assertion_failed_msgs() -> None:
    expected_assertion_failed_msgs: Optional[
        List[str]
    ] = run_docs_e2e_tests._get_expected_assertion_failed_msgs(
        file_name="jp_assert_equal_and_not_equal"
    )
    assert expected_assertion_failed_msgs == [
        "Values are equal!",
        "Values are not equal!",
    ]

    expected_assertion_failed_msgs = (
        run_docs_e2e_tests._get_expected_assertion_failed_msgs(file_name="sprite")
    )
    assert expected_assertion_failed_msgs is None


@apply_test_settings()
def test__create_local_file_data_2dim_list() -> None:
    local_file_data_2dim_list: List[
        List[LocalFileData]
    ] = run_docs_e2e_tests._create_local_file_data_2dim_list(
        file_names=["index", "jp_index", "assert_equal_and_not_equal"],
        single_list_max_len=2,
    )
    assert len(local_file_data_2dim_list), 2
    assert len(local_file_data_2dim_list[0]), 2
    assert len(local_file_data_2dim_list[1]), 1
    assert local_file_data_2dim_list[0][0]["file_path"].endswith("/en/index.html")
    assert local_file_data_2dim_list[0][1]["file_path"].endswith("/jp/jp_index.html")
    assert local_file_data_2dim_list[1][0]["expected_assertion_failed_msgs"] == [
        "Values are equal!",
        "Values are not equal!",
    ]

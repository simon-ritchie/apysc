import os
from typing import List

from apysc._lint_and_doc import docs_toctree_util
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test__extract_toctree_file_names_from_file() -> None:
    toctree_file_names: List[
        str
    ] = docs_toctree_util._extract_toctree_file_names_from_file(
        toctree_defined_en_file_name="index",
    )
    assert "what_apysc_can_do.md" in toctree_file_names
    assert "recommended_type_checker_settings.md" in toctree_file_names
    assert "stage.md" in toctree_file_names
    for toctree_file_name in toctree_file_names:
        assert os.path.exists(f"./docs_src/source/{toctree_file_name}")


@apply_test_settings()
def test_get_toctree_file_names() -> None:
    toctree_file_names: List[str] = docs_toctree_util.get_toctree_file_names()
    assert "what_apysc_can_do.md" in toctree_file_names
    assert "stage.md" in toctree_file_names
    for toctree_file_name in toctree_file_names:
        assert os.path.exists(f"./docs_src/source/{toctree_file_name}")


@apply_test_settings()
def test_get_doc_prev_and_next_md_file_names() -> None:
    prev_md_doc_file_name: str
    next_md_doc_file_name: str
    (
        prev_md_doc_file_name,
        next_md_doc_file_name,
    ) = docs_toctree_util.get_doc_prev_and_next_md_file_names(
        md_doc_file_name="not_existing_document.md"
    )
    assert prev_md_doc_file_name == ""
    assert next_md_doc_file_name == ""

    (
        prev_md_doc_file_name,
        next_md_doc_file_name,
    ) = docs_toctree_util.get_doc_prev_and_next_md_file_names(
        md_doc_file_name="circle.md"
    )
    assert prev_md_doc_file_name == "rectangle.md"
    assert next_md_doc_file_name == "ellipse.md"


@apply_test_settings()
def test__get_expected_prev_md_file_name() -> None:
    toctree_file_names: List[str] = ["a.md", "b.md"]
    expected_prev_md_file_name: str = docs_toctree_util._get_expected_prev_md_file_name(
        toctree_file_names=toctree_file_names,
        i=0,
    )
    assert expected_prev_md_file_name == ""

    expected_prev_md_file_name = docs_toctree_util._get_expected_prev_md_file_name(
        toctree_file_names=toctree_file_names,
        i=1,
    )
    assert expected_prev_md_file_name == "a.md"


@apply_test_settings()
def test__get_expected_next_md_file_name() -> None:
    toctree_file_names: List[str] = ["a.md", "b.md"]
    expected_next_md_file_name: str = docs_toctree_util._get_expected_next_md_file_name(
        toctree_file_names=toctree_file_names,
        i=1,
    )
    assert expected_next_md_file_name == ""

    expected_next_md_file_name = docs_toctree_util._get_expected_next_md_file_name(
        toctree_file_names=toctree_file_names,
        i=0,
    )
    assert expected_next_md_file_name == "b.md"


@apply_test_settings(retrying_sleep_seconds=1)
def test__update_adjacent_doc_modified_time_if_toctree_updated() -> None:
    original_file_prev_modified_time: float = os.path.getmtime(
        filename="./docs_src/source/sprite.md"
    )
    translated_file_prev_modified_time: float = os.path.getmtime(
        filename="./docs_src/source/jp_sprite.md"
    )
    is_updated: bool = (
        docs_toctree_util._update_adjacent_doc_modified_time_if_toctree_updated(
            adjacent_doc_file_name="sprite.md",
            expected_md_file_name="sprite.md",
        )
    )
    assert not is_updated

    is_updated = (
        docs_toctree_util._update_adjacent_doc_modified_time_if_toctree_updated(
            adjacent_doc_file_name=" ",
            expected_md_file_name="",
        )
    )
    assert not is_updated

    is_updated = (
        docs_toctree_util._update_adjacent_doc_modified_time_if_toctree_updated(
            adjacent_doc_file_name="sprite.md",
            expected_md_file_name="stage.md",
        )
    )
    assert is_updated
    after_modified_time: float = os.path.getmtime(
        filename="./docs_src/source/sprite.md"
    )
    assert original_file_prev_modified_time != after_modified_time
    after_modified_time = os.path.getmtime(filename="./docs_src/source/jp_sprite.md")
    assert translated_file_prev_modified_time != after_modified_time


@apply_test_settings(retrying_sleep_seconds=1.3)
def test_update_docs_prev_and_next_page_modified_time() -> None:
    docs_toctree_util.update_docs_prev_and_next_page_modified_time()

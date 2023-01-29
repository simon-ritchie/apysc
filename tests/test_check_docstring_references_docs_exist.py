from typing import List

from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises
from scripts import check_docstring_references_docs_exist as mod


@apply_test_settings()
def test__extract_file_names() -> None:
    file_names: List[str] = mod._extract_file_names(dir_path="./apysc/_display/")
    for file_name in file_names:
        assert file_name.endswith(".html")
        assert "/" not in file_name
    expected_file_names: List[str] = [
        "sprite.html",
        "stage.html",
        "graphics_draw_rect.html",
    ]
    for expected_file_name in expected_file_names:
        assert expected_file_name in file_names


@apply_test_settings()
def test__main() -> None:
    file_names: List[str] = mod._main(dir_path="./apysc/_display/")
    assert "sprite.html" in file_names
    assert "stage.html" in file_names


@apply_test_settings()
def test__assert_url_contains_language_path() -> None:
    mod._assert_url_contains_language_path(
        url="https://simon-ritchie.github.io/apysc/en/stage.html"
    )

    assert_raises(
        expected_error_class=AssertionError,
        callable_=mod._assert_url_contains_language_path,
        url="https://simon-ritchie.github.io/apysc/stage.html",
    )

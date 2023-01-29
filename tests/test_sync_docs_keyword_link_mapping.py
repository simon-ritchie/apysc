import os
from typing import Dict

from apysc._file import file_util
from apysc._lint_and_doc.docs_lang import Lang
from apysc._testing.testing_helper import apply_test_settings
from scripts import sync_docs_keyword_link_mapping


@apply_test_settings()
def test__create_keyword_link_mappings() -> None:
    keyword_link_mappings: Dict[
        str, str
    ] = sync_docs_keyword_link_mapping._create_keyword_link_mappings(
        lang=Lang.EN,
    )
    assert keyword_link_mappings["Stage"] == (
        "https://simon-ritchie.github.io/apysc/en/stage.html"
    )
    assert keyword_link_mappings["Sprite"] == (
        "https://simon-ritchie.github.io/apysc/en/sprite.html"
    )

    keyword_link_mappings = (
        sync_docs_keyword_link_mapping._create_keyword_link_mappings(
            lang=Lang.JP,
        )
    )
    assert keyword_link_mappings["Stage"] == (
        "https://simon-ritchie.github.io/apysc/jp/jp_stage.html"
    )
    assert keyword_link_mappings["Sprite"] == (
        "https://simon-ritchie.github.io/apysc/jp/jp_sprite.html"
    )


@apply_test_settings()
def test_sync() -> None:
    expected_en_script_path: str = "./docs/en/static/keyword_link_mapping.js"
    file_util.remove_file_if_exists(file_path=expected_en_script_path)
    sync_docs_keyword_link_mapping.sync(lang=Lang.EN)
    assert os.path.exists(expected_en_script_path)
    script_txt: str = file_util.read_txt(file_path=expected_en_script_path)
    assert 'const KEYWORD_LINK_MAPPINGS = {"' in script_txt
    assert "Sprite" in script_txt
    assert "function() {\n" in script_txt

    expected_jp_script_path: str = "./docs/jp/static/keyword_link_mapping.js"
    file_util.remove_file_if_exists(file_path=expected_jp_script_path)
    sync_docs_keyword_link_mapping.sync(lang=Lang.JP)
    assert os.path.exists(expected_jp_script_path)
    script_txt = file_util.read_txt(file_path=expected_jp_script_path)
    assert "jp_sprite" in script_txt

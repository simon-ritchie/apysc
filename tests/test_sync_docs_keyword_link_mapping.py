from random import randint
from typing import Dict

from retrying import retry

from scripts import sync_docs_keyword_link_mapping
from apysc._lint_and_doc.docs_lang import Lang


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__create_keyword_link_mappings() -> None:
    keyword_link_mappings: Dict[str, str] = (
        sync_docs_keyword_link_mapping._create_keyword_link_mappings(
            lang=Lang.EN,
        )
    )
    assert keyword_link_mappings["Stage"] == (
        "https://simon-ritchie.github.io/apysc/en/stage.html"
    )
    assert keyword_link_mappings["Sprite"] == (
        "https://simon-ritchie.github.io/apysc/en/sprite.html"
    )

    keyword_link_mappings: Dict[str, str] = (
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

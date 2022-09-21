"""The module to synchronize documents keyword link mappings.
"""

import sys
from typing import Dict, List

sys.path.append("./")

from apysc._lint_and_doc.docs_lang import Lang
from apysc._lint_and_doc import lint_and_doc_hash_util
from apysc._lint_and_doc.lint_and_doc_hash_util import HashType
from apysc._lint_and_doc.docs_keyword_link_mapping import MAPPINGS

_HASH_TARGET_FILE_PATHS: List[str] = [
    "./scripts/sync_docs_keyword_link_mapping.py",
    "./apysc/_lint_and_doc",
]

_MAPPING_SCRIPT_FORMAT: str = """
$(document).ready(function() {
    const KEYWORD_LINK_MAPPINGS = {keyword_link_mappings};
    for (let keyword in KEYWORD_LINK_MAPPINGS) {
        let link = KEYWORD_LINK_MAPPINGS[keyword];
                $("span:contains(" + keyword + ")").each(function() {
            let elemText = $(this).text();
            elemText = sanitise(elemText);
            if (elemText !== keyword) {
                return;
            }
            let className = $(this).attr("class");
            className = sanitise(className);
            if (className !== "pre") {
                return;
            }
            $(this).html("<a href='" + link + "'>" + $(this).html() + "</a>");
        });
    }
});
"""

_Keyword = str
_Link = str


def sync(*, lang: Lang) -> None:
    """
    Synchronize specified language's documents keyword link mappings.

    Parameters
    ----------
    lang : Lang
        A target language to synchronize.
    """
    keyword_link_mappings: Dict[_Keyword, _Link] = _create_keyword_link_mappings(
        lang=lang
    )
    pass


def _create_keyword_link_mappings(*, lang: Lang) -> Dict[_Keyword, _Link]:
    """
    Create target language's keyword link mappings.

    Parameters
    ----------
    lang : Lang
        A target language.

    Returns
    -------
    keyword_link_mappings : Dict[_Keyword, _Link]
        Created keyword link mappings.
    """
    keyword_link_mappings: Dict[_Keyword, _Link] = {}
    for keyword, doc_file_name in MAPPINGS.items():
        if lang != Lang.EN:
            doc_file_name = f"{lang.value}_{doc_file_name}"
        link: str = (
            f"https://simon-ritchie.github.io/apysc/{lang.value}/{doc_file_name}.html"
        )
        keyword_link_mappings[keyword] = link
    return keyword_link_mappings

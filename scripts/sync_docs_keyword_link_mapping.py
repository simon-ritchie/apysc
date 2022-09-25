"""The module to synchronize documents keyword link mappings.
"""

import json
import sys
from typing import Dict

sys.path.append("./")

from apysc._lint_and_doc.docs_keyword_link_mapping import MAPPINGS
from apysc._lint_and_doc.docs_lang import Lang

_MAPPING_SCRIPT_FORMAT: str = """
$(document).ready(function() {{
    const KEYWORD_LINK_MAPPINGS = {keyword_link_mappings};
    const CURRENT_PAGE_FILE_NAME = location.pathname.substring(
        location.pathname.lastIndexOf('/') + 1
    );
    for (let keyword in KEYWORD_LINK_MAPPINGS) {{
        let link = KEYWORD_LINK_MAPPINGS[keyword];
        let link_file_name = link.substring(link.lastIndexOf('/') + 1);
        if (link_file_name === CURRENT_PAGE_FILE_NAME) {
            continue;
        }
        $("span:contains(" + keyword + ")").each(function() {{
            let elemText = $(this).text();
            elemText = sanitise(elemText);
            if (elemText !== keyword) {{
                return;
            }}
            let className = $(this).attr("class");
            className = sanitise(className);
            if (className !== "pre") {{
                return;
            }}
            $(this).html("<a href='" + link + "'>" + $(this).html() + "</a>");
        }});
    }}
}});
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
    from apysc._file import file_util

    keyword_link_mappings: Dict[_Keyword, _Link] = _create_keyword_link_mappings(
        lang=lang
    )
    keyword_link_mappings_json: str = json.dumps(keyword_link_mappings)
    mapping_script: str = _MAPPING_SCRIPT_FORMAT.format(
        keyword_link_mappings=keyword_link_mappings_json,
    )
    script_file_path: str = f"./docs/{lang.value}/static/keyword_link_mapping.js"
    file_util.save_plain_txt(txt=mapping_script, file_path=script_file_path)


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

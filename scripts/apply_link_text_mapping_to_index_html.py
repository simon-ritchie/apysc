"""Apply table-of-contents text mappings to each index's
markdown file.

Command examples:
$ python scripts/apply_link_text_mapping_to_index_html.py
"""

import os
import sys
from logging import Logger
from typing import Dict, Pattern, Optional, Match
from typing import List
import re

sys.path.append('./')

from apysc._console import loggers

logger: Logger = loggers.get_info_logger()


def apply() -> None:
    """Apply table-of-contents text mappings to each index's
    markdown file.
    """
    from apysc._lint_and_doc import lint_and_doc_hash_util
    from apysc._lint_and_doc.lint_and_doc_hash_util import HashType
    print('-' * 20)
    logger.info(
        msg='Applying index.md\'s table-of-contents text mappings...')
    html_paths: List[str] = _get_target_html_paths()
    for html_path in html_paths:
        is_file_updated: bool = lint_and_doc_hash_util.is_file_updated(
            file_path=html_path,
            hash_type=HashType.INDEX_HTML_LINK_TEXT_MAPPING)
        if not is_file_updated:
            continue
        logger.info(
            msg=f'Applying mappings to the {html_path}')
        _apply_mapping(html_path=html_path)
        lint_and_doc_hash_util.save_target_file_hash(
            file_path=html_path,
            hash_type=HashType.INDEX_HTML_LINK_TEXT_MAPPING)


def _apply_mapping(*, html_path: str) -> None:
    """
    Apply each link text mapping to a specified HTML file.

    Parameters
    ----------
    html_path : str
        A target HTML's file path.
    """
    from apysc._file import file_util
    mappings: Dict[str, str] = _extract_mappings_from_index_md()
    html_txt: str = file_util.read_txt(file_path=html_path)
    for mapping_key, mapping_value in mappings.items():
        html_txt = html_txt.replace(mapping_key, mapping_value)
    file_util.save_plain_txt(txt=html_txt, file_path=html_path)


def _extract_mappings_from_index_md() -> Dict[str, str]:
    """
    Extract mappings from the `index.md` file.

    Returns
    -------
    mappings : dict
        A dictionary for the mappings.
        Each key has a no-underscore link text and
        each value has a link text with underscores.
    """
    from apysc._file import file_util
    index_md_txt: str = file_util.read_txt(
        file_path='./docs_src/source/index.md')
    pattern: Pattern = re.compile(pattern=r'^- \[(.*?\_.*?)\]')
    lines: List[str] = index_md_txt.splitlines()
    mappings: Dict[str, str] = {}
    for line in lines:
        match: Optional[Match] = pattern.search(string=line)
        if match is None:
            continue
        link_txt: str = match.group(1)
        words: List[str] = link_txt.split(' ')
        for word in words:
            if '_' not in word:
                continue
            mappings[word.replace('_', ' ')] = word
    return mappings


def _get_target_html_paths() -> List[str]:
    """
    Get target index.html's file paths.

    Returns
    -------
    html_paths : list of str
        Target HTML files paths.
    """
    html_paths: List[str] = []
    DIR_PATH: str = './docs/'
    file_names: List[str] = os.listdir(DIR_PATH)
    for file_name in file_names:
        if not file_name.endswith('index.html'):
            continue
        html_path: str = os.path.join(
            DIR_PATH,
            file_name,
        )
        html_paths.append(html_path)
    return html_paths


if __name__ == '__main__':
    apply()

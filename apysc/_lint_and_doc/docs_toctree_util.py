"""The utility module for the documents toctree.
"""

import os
from typing import List, Tuple, Pattern, Optional, Match
import re

_TOCTREE_DEFINED_EN_FILE_NAMES: List[str] = [
    "index",
]


def get_toctree_file_names() -> List[str]:
    """
    Get toctree file names from the toctree defined files.

    Returns
    -------
    toctree_file_names : List[str]
        Result toctree file names
        (e.g., ["what_apysc_can_do.md", "quick_start.md", ...]).
    """
    toctree_file_names: List[str] = []
    for toctree_defined_en_file_name in _TOCTREE_DEFINED_EN_FILE_NAMES:
        extracted_toctree_file_names: List[str] = _extract_toctree_file_names_from_file(
            toctree_defined_en_file_name=toctree_defined_en_file_name,
        )
        toctree_file_names.extend(extracted_toctree_file_names)
    return toctree_file_names


def _extract_toctree_file_names_from_file(
    *, toctree_defined_en_file_name: str
) -> List[str]:
    """
    Extract toctree file names from a specified file.

    Parameters
    ----------
    toctree_defined_en_file_name : str
        An English document file name that contains the toctree definition.

    Returns
    -------
    toctree_file_names : List[str]
        Extracted toctree file names.
    """
    from apysc._file import file_util
    file_str: str = file_util.read_txt(
        file_path=f"./docs_src/source/{toctree_defined_en_file_name}.md"
    )
    lines: List[str] = file_str.splitlines()
    toctree_file_names: List[str] = []
    is_toctree_range_lines: bool = False
    for line in lines:
        if '```{toctree}' in line:
            is_toctree_range_lines = True
            continue
        if 'maxdepth' in line:
            continue
        if is_toctree_range_lines and '```' in line:
            is_toctree_range_lines = False
            continue
        if not is_toctree_range_lines:
            continue
        toctree_file_names.append(f'{line.strip()}.md')
    return toctree_file_names


_LINK_PREV_PATTERN: Pattern = re.compile(
    pattern=r'\<link rel="prev" title=".+?" href="(.+?)\.html"'
)
_LINK_NEXT_PATTERN: Pattern = re.compile(
    pattern=r'\<link rel="next" title=".+?" href="(.+?)\.html"'
)


def get_doc_prev_and_next_md_file_names(*, md_doc_file_name: str) -> Tuple[str, str]:
    """
    Get specified markdown file's previous and next markdown file names.

    Parameters
    ----------
    md_doc_file_name : str
        Target markdown file name (e.g., sprite.md).

    Returns
    -------
    prev_md_doc_file_name : str
        A previous markdown file name.
    next_md_doc_file_name : str
        A next markdown file name.
    """
    from apysc._file import file_util
    html_file_path: str = f"./docs/en/{md_doc_file_name.replace('.md', '.html', 1)}"
    if not os.path.exists(html_file_path):
        return "", ""
    prev_md_doc_file_name: str = ""
    next_md_doc_file_name: str = ""
    html_str: str = file_util.read_txt(file_path=html_file_path)
    lines: List[str] = html_str.splitlines()
    for line in lines:
        if prev_md_doc_file_name == "":
            match: Optional[Match] = _LINK_PREV_PATTERN.search(string=line)
            if match is not None:
                prev_md_doc_file_name = f"{match.group(1)}.md"
                continue
        if next_md_doc_file_name == "":
            match = _LINK_NEXT_PATTERN.search(string=line)
            if match is not None:
                next_md_doc_file_name = f"{match.group(1)}.md"
                continue
    return prev_md_doc_file_name, next_md_doc_file_name

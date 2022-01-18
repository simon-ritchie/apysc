"""Utility implementations for docstrings.
"""

from typing import List
import os
import re

_DOCSTRING_PATH_COMMENT_KEYWORD: str = 'Docstring:'


def reset_replaced_docstring_section(md_file_path: str) -> bool:
    """
    Reset converted a markdown's docstring section.

    Parameters
    ----------
    md_file_path : str
        Target markdown document file path.

    Returns
    -------
    is_executed : bool
        Replacing is executed or not.
    """
    from apysc._file import file_util
    if not os.path.isfile(md_file_path):
        return False
    md_txt: str = file_util.read_txt(file_path=md_file_path)
    matches: List[str] = _get_docstring_path_comment_matches(md_txt=md_txt)
    if not matches:
        return False
    md_txt = _remove_replaced_docstring_section_from_md_txt(
        md_txt=md_txt, matches=matches)
    pass


def _remove_replaced_docstring_section_from_md_txt(
        md_txt: str, matches: List[str]) -> str:
    """
    Remove replaced docstring from a specified markdown text.

    Parameters
    ----------
    md_txt : str
        Target markdown text.
    matches : list of str
        Matched docstring path specification comments.

    Returns
    -------
    md_txt : str
        Result markdown text.
    """
    lines: List[str] = md_txt.splitlines()
    result_lines: List[str] = []
    is_reset_section_range: bool = False
    for line in lines:
        if is_reset_section_range:
            if line.startswith('#'):
                result_lines.append(f'\n\n{line}')
                is_reset_section_range = False
            continue
        docstring_path_specification_comment: str = \
            _extract_docstring_path_specification_comment_from_line(
                line=line, matches=matches)
        if docstring_path_specification_comment != '':
            result_lines.append(line)
            is_reset_section_range = True
            continue
    pass


def _extract_docstring_path_specification_comment_from_line(
        line: str, matches: List[str]) -> str:
    """
    Extract a docstring path specification comment
    from a specified markdown line text.

    Parameters
    ----------
    line : str
        Target markdown line text.
    matches : list of str
        Matched docstring path specification comments.

    Returns
    -------
    docstring_path_specification_comment : str
        Extracted comment string.
    """
    for match in matches:
        if match in line:
            return match
    return ''


def _get_docstring_path_comment_matches(md_txt: str) -> List[str]:
    """
    Get matched docstring path specification comments.

    Parameters
    ----------
    md_txt : str
        Target markdown text.

    Returns
    -------
    matches : list of str
        Matched comments.
    """
    matches: List[str] = re.findall(
        pattern=(
            rf'\<\!\-\-.*?{_DOCSTRING_PATH_COMMENT_KEYWORD}.*?'
            r'.*?\-\-\>'
        ),
        string=md_txt,
        flags=re.MULTILINE)
    return matches

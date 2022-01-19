"""Utility implementations for docstrings.
"""

from typing import List, Match, Optional, Tuple
import os
import re

_DOCSTRING_PATH_COMMENT_KEYWORD: str = 'Docstring:'
_DOCSTRING_PATH_COMMENT_PATTERN: str = (
    rf'\<\!\-\-.*?{_DOCSTRING_PATH_COMMENT_KEYWORD}'
    r'(?P<path>.*?)\-\-\>'
)


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
    md_txt: str = file_util.read_txt(file_path=md_file_path)
    matches: List[str] = _get_docstring_path_comment_matches(md_txt=md_txt)
    if not matches:
        return False
    md_txt = _remove_replaced_docstring_section_from_md_txt(
        md_txt=md_txt, matches=matches)
    with open(md_file_path, 'w') as f:
        f.write(md_txt)
    return True


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
                result_lines.append(f'\n{line}')
                is_reset_section_range = False
            continue
        docstring_path_specification_comment: str = \
            _extract_docstring_path_specification_comment_from_line(
                line=line, matches=matches)
        if docstring_path_specification_comment != '':
            result_lines.append(line)
            is_reset_section_range = True
            continue
        result_lines.append(line)
    md_txt = '\n'.join(result_lines)
    return md_txt


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
    matches: List[str] = []
    for match in re.finditer(
            pattern=_DOCSTRING_PATH_COMMENT_PATTERN,
            string=md_txt,
            flags=re.MULTILINE):
        matches.append(match.group(0))
    return matches


def replace_docstring_path_specification(md_file_path: str) -> None:
    """
    Replace a docstring path specification in a specified
    markdown document by a converted docstring text.

    Parameters
    ----------
    md_file_path : str
        Target markdown file path.
    """
    from apysc._file import file_util
    md_txt: str = file_util.read_txt(file_path=md_file_path)
    lines: List[str] = md_txt.splitlines()
    result_lines: List[str] = []
    for line in lines:
        match: Optional[Match] = re.search(
            pattern=_DOCSTRING_PATH_COMMENT_PATTERN, string=line)
        if match is not None:
            result_lines.append(line)
            result_lines.append('')
            markdown_format_docstring: str = \
                _convert_docstring_path_comment_to_markdown_format(
                    docstring_path_comment=match.group(0)
                )
            result_lines.append(markdown_format_docstring)
            continue

        result_lines.append(line)
        continue
    pass


def _convert_docstring_path_comment_to_markdown_format(
        docstring_path_comment: str) -> str:
    """
    Convert a specified docstring path comment to a
    markdown format text.

    Parameters
    ----------
    docstring_path_comment : str
        Target docstring path comment.

    Returns
    -------
    markdown_format_docstring : str
        Converted text.
    """
    module_or_class_package_path: str
    callable_name: str
    module_or_class_package_path, callable_name = \
        _extract_package_path_and_callable_name_from_path(
            docstring_path_comment=docstring_path_comment,
        )
    pass


def _extract_package_path_and_callable_name_from_path(
        docstring_path_comment) -> Tuple[str, str]:
    """
    Extract a module or class package path and callable
    name from a specified path comment.

    Parameters
    ----------
    docstring_path_comment : str
        Target docstring path comment.

    Returns
    -------
    module_or_class_package_path : str
        Extracted module or class package path.
        e.g., 'apy.path' or 'any.path.AnyClass'.
    callable_name : str
        Extracted callable name.
    """
    path: str = _extract_path_from_docstring_comment(
        docstring_path_comment=docstring_path_comment)
    pass


def _extract_path_from_docstring_comment(
        docstring_path_comment: str) -> str:
    """
    Extract a path string from a specified docstring path comment.

    Parameters
    ----------
    docstring_path_comment : str
        Target docstring path comment.

    Returns
    -------
    path : str
        Extracted path string.
    """
    match: Optional[Match] = re.search(
        pattern=_DOCSTRING_PATH_COMMENT_PATTERN,
        string=docstring_path_comment)
    if match is None:
        return ''
    path: str = match.group(1)
    path = path.strip()
    return path

"""Utility implementations for docstrings.
"""

from ctypes import Union
from types import ModuleType
import importlib
from typing import Any, Callable, List, Match, Optional, Tuple, Type
import os
import re

from typing_extensions import TypedDict

_DOCSTRING_PATH_COMMENT_KEYWORD: str = 'Docstring:'
_DOCSTRING_PATH_COMMENT_PATTERN: str = (
    rf'\<\!\-\-.*?{_DOCSTRING_PATH_COMMENT_KEYWORD}'
    r'(?P<path>.*?)\-\-\>'
)

_PARAMETERS_SECTION_PATTERN: str = r'\s{4}Parameters$'
_RETURNS_SECTION_PATTERN: str = r'\s{4}Returns$'
_SECTION_PATTERNS: List[str] = [
    _PARAMETERS_SECTION_PATTERN,
    _RETURNS_SECTION_PATTERN,
    r'\s{4}Yields$',
    r'\s{4}Receives$',
    r'\s{4}Raises$',
    r'\s{4}Warns$',
    r'\s{4}Warnings$',
    r'\s{4}See Also$',
    r'\s{4}Notes$',
    r'\s{4}References$',
    r'\s{4}Examples$',
    r'\s{4}Attributes$',
    r'\s{4}Methods$',
    r'\s{4}Methods$',
]
_HYPHENS_LINE_PATTERN: str = r'\s{4}-----'


def reset_replaced_docstring_section(*, md_file_path: str) -> bool:
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
        *, md_txt: str, matches: List[str]) -> str:
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
        *, line: str, matches: List[str]) -> str:
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


def _get_docstring_path_comment_matches(*, md_txt: str) -> List[str]:
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


def replace_docstring_path_specification(*, md_file_path: str) -> None:
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
        *, docstring_path_comment: str) -> str:
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
    from apysc._file import module_util
    module_or_class_package_path: str
    callable_name: str
    module_or_class_package_path, callable_name = \
        _extract_package_path_and_callable_name_from_path(
            docstring_path_comment=docstring_path_comment,
        )
    module_or_class: Any = module_util.read_module_or_class_from_package_path(
        module_or_class_package_path=module_or_class_package_path)
    callable_: Callable = getattr(module_or_class, callable_name)
    if callable_.__doc__ is None:
        return ''
    markdown_format_docstring: str = _convert_docstring_to_markdown(
        docstring=callable_.__doc__)
    pass


def _convert_docstring_to_markdown(*, docstring: str) -> str:
    """
    Convert a specified docstring to a markdown format text.

    Parameters
    ----------
    docstring : str
        Target docstring.

    Returns
    -------
    markdown : str
        Converted markdown text.
    """
    summary: str = _extract_summary_from_docstring(docstring=docstring)
    parameters: List[_Parameter] = _extract_parameters_from_docstring(
        docstring=docstring)
    pass


class _Parameter(TypedDict):
    name: str
    type_str: str
    description: str


def _extract_parameters_from_docstring(
        docstring: str) -> List[_Parameter]:
    """
    Extract parameter values from a docstring.

    Parameters
    ----------
    docstring : str
        Target docstring.

    Returns
    -------
    parameters : list of _Parameter
        Extracted parameter values.
    """
    lines: List[str] = docstring.splitlines()
    is_parameter_section_range: bool = False
    base_indent_num: int = 0
    is_description_area: bool = False
    param_name: str = ''
    param_type_str: str = ''
    description_lines: List[str] = []
    for line in lines:
        if _is_parameters_section_pattern_line(line=line):
            is_parameter_section_range = True
            continue
        if not is_parameter_section_range:
            continue
        if _is_hyphens_line(line=line):
            continue
        if _is_section_line(line=line):
            break
        if not is_description_area:
            is_description_area = True
            description_lines = []
            param_name, param_type_str = _get_value_name_and_type_from_line(
                line=line)
            base_indent_num = _get_indent_num_from_line(line=line)
            continue
        pass
    pass


def _get_indent_num_from_line(*, line: str) -> int:
    """
    Get an indent number from a specified docstring line.

    Parameters
    ----------
    line : str
        Target docstring line.

    Returns
    -------
    indent_num : int
        Indent number of a specified docstring line.
    """
    spaces: int = 0
    for char in line:
        if char != ' ':
            break
        spaces += 1
    indent_num: int = spaces // 4
    return indent_num


def _get_value_name_and_type_from_line(*, line: str) -> Tuple[str, str]:
    """
    Get a parameter or return value and type from
    a specified line.

    Parameters
    ----------
    line : str
        Target docstring line.

    Returns
    -------
    value_name : str
        Target parameter or return value name.
    type_name : str
        Target parameter or return value type name.
    """
    if ':' not in line:
        return '', ''
    splitted: List[str] = line.split(':', maxsplit=1)
    value_name: str = splitted[0].strip()
    type_name: str = splitted[1].strip()
    return value_name, type_name


def _is_hyphens_line(*, line: str) -> bool:
    """
    Get a boolean indicating whether a specified line is
    a hyphens line or not.

    Parameters
    ----------
    line : str
        Target docstring line.

    Returns
    -------
    result : bool
        If a specified line is a hyphens line, this function
        returns True.
    """
    match: Optional[Match] = re.search(
        pattern=_HYPHENS_LINE_PATTERN, string=line)
    if match is None:
        return False
    return True


def _is_parameters_section_pattern_line(*, line: str) -> bool:
    """
    Get a boolean indicating whether a specified line
    is a parameters section or not.

    Parameters
    ----------
    line : str
        Target docstring line.

    Returns
    -------
    result : bool
        If a specified line is the parameters section,
        this function returns True.
    """
    match: Optional[Match] = re.search(
        pattern=_PARAMETERS_SECTION_PATTERN, string=line)
    if match is None:
        return False
    return True


def _extract_summary_from_docstring(*, docstring: str) -> str:
    """
    Extract a summary text from a docstring.

    Parameters
    ----------
    docstring : str
        Target docstring.

    Returns
    -------
    summary : str
        Extracted summary text.

    Notes
    -----
    This function converts line break to a space.
    """
    from apysc._string import string_util
    lines: List[str] = docstring.splitlines()
    result_lines: List[str] = []
    for line in lines:
        if _is_section_line(line=line):
            break
        result_lines.append(line)
    summary: str = '\n'.join(result_lines)
    summary = summary.strip()
    summary = summary.replace('\n', ' ')
    summary = string_util.replace_double_spaces_to_single_space(
        string=summary)
    summary = summary.strip()
    return summary


def _is_section_line(*, line: str) -> bool:
    """
    Get a boolean indicating whether a specified docstring line
    is a section line or not.

    Parameters
    ----------
    line : str
        Target docstring line text.

    Returns
    -------
    result : bool
        If a specified docstring line is section line, this
        function returns True.
    """
    for pattern in _SECTION_PATTERNS:
        match: Optional[Match] = re.search(
            pattern=pattern, string=line)
        if match is None:
            continue
        return True
    return False


def _extract_package_path_and_callable_name_from_path(
        *, docstring_path_comment) -> Tuple[str, str]:
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
    if '.' not in path:
        return '', ''
    splitted: List[str] = path.rsplit('.', maxsplit=1)
    module_or_class_package_path: str = splitted[0]
    callable_name: str = splitted[1]
    return module_or_class_package_path, callable_name


def _extract_path_from_docstring_comment(
        *, docstring_path_comment: str) -> str:
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

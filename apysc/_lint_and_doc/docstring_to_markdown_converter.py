"""The script to convert and sync each docstring to
markdown files.
"""

import os
from types import ModuleType
from typing import List, Optional


def convert_recursively(*, dir_path: str) -> None:
    """
    Convert each docstring in the specified directory
    to markdown files recursively.

    Parameters
    ----------
    dir_path : str
        Target directory path.
    """
    from apysc._file import module_util
    if not os.path.isdir(dir_path):
        return
    file_or_dir_names: List[str] = os.listdir(dir_path)
    for file_or_dir_name in file_or_dir_names:
        file_or_dir_path: str = os.path.join(
            dir_path, file_or_dir_name)
        if os.path.isfile(file_or_dir_path):
            convert_recursively(dir_path=file_or_dir_path)
            continue
        if not file_or_dir_path.endswith('.py'):
            continue
        module: ModuleType = module_util.read_target_path_module(
            module_path=file_or_dir_path)
        markdown: str = _convert_module_docstring_to_markdown(
            module=module)
        pass
    pass


def _convert_module_docstring_to_markdown(
        *, module: ModuleType) -> str:
    """
    Convert a specified module's docstring to a markdown string.

    Parameters
    ----------
    module : ModuleType
        Target module.

    Returns
    -------
    markdown : str
        Converted markdown string.
    """
    markdown: str = ''
    markdown = _append_module_docstring_to_markdown(
        markdown=markdown,
        module_docstring=module.__doc__)
    pass


def _append_module_docstring_to_markdown(
        *, markdown: str,
        module_docstring: Optional[str]) -> str:
    """
    Append a module description docstring to a specified
    markdown string.

    Parameters
    ----------
    markdown : str
        Target markdown string.
    module_docstring : str or None
        Target module description docstring.

    Returns
    -------
    markdown : str
        Result markdown string.
    """
    from apysc._lint_and_doc import docstring_util
    from apysc._lint_and_doc.docstring_util import Reference
    if module_docstring is None:
        return markdown
    summary: str = docstring_util.extract_summary_from_docstring(
        docstring=module_docstring)
    notes: str = docstring_util.extract_notes_from_docstring(
        docstring=module_docstring)
    references: List[Reference] = docstring_util.\
        extract_reference_values_from_docstring(docstring=module_docstring)

    if markdown != '':
        markdown += '\n\n'
    markdown += '## Module summary'
    markdown = docstring_util.append_summary_to_markdown(
        markdown=markdown, summary=summary,
        heading_label='')
    markdown = docstring_util.append_notes_to_markdown(
        markdown=markdown, notes=notes)
    markdown = docstring_util.append_references_to_markdown(
        markdown=markdown, references=references)
    markdown = docstring_util.remove_trailing_hr_tag(markdown=markdown)
    return markdown

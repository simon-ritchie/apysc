"""The script to convert and sync each docstring to
markdown files.
"""

import os
from types import ModuleType
from typing import Callable, List, Optional, Tuple
import inspect


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
    markdown: str = f'# {module.__name__} docstrings'
    markdown = _append_module_docstring_to_markdown(
        markdown=markdown,
        module_docstring=module.__doc__)

    toplevel_functions: List[Callable] = _get_module_toplevel_functions(
        module=module)
    for toplevel_function in toplevel_functions:
        markdown = _append_toplevel_function_docstring_to_markdown(
            markdown=markdown, toplevel_function=toplevel_function)
    pass


def _append_toplevel_function_docstring_to_markdown(
        *, markdown: str,
        toplevel_function: Callable) -> str:
    """
    Append a top-level function docstring to a markdown string.

    Parameters
    ----------
    markdown : str
        Target markdown string.
    toplevel_function : Callable
        Target top-level functions.

    Returns
    -------
    markdown : str
        Result markdown string.
    """
    if toplevel_function.__doc__ is None:
        return markdown
    if markdown != '':
        markdown += '\n\n'
    markdown += f'## {toplevel_function.__name__} function docstring'
    markdown = _append_each_section_to_markdown(
        markdown=markdown,
        docstring=toplevel_function.__doc__,
    )
    return markdown


def _append_each_section_to_markdown(
        markdown: str, docstring: str) -> str:
    """
    Append each docstring section to a specified markdown string.

    Parameters
    ----------
    markdown : str
        Target markdown string.
    docstring : str
        Target docstring.

    Returns
    -------
    markdown : str
        Result markdown string.
    """
    from apysc._lint_and_doc import docstring_util
    from apysc._lint_and_doc.docstring_util import Parameter, Return, Raise, Example, Reference
    summary: str = docstring_util.extract_summary_from_docstring(
        docstring=docstring)
    parameters: List[Parameter] = \
        docstring_util.extract_param_or_rtn_values_from_docstring(
            target_type=Parameter, docstring=docstring)
    returns: List[Return] = \
        docstring_util.extract_param_or_rtn_values_from_docstring(
            target_type=Return, docstring=docstring)
    raises: List[Raise] = docstring_util.extract_raise_values_from_docstring(
        docstring=docstring)
    notes: str = docstring_util.extract_notes_from_docstring(
        docstring=docstring)
    examples: List[Example] = \
        docstring_util.extract_example_values_from_docstring(
            docstring=docstring)
    references: List[Reference] = \
        docstring_util.extract_reference_values_from_docstring(
            docstring=docstring)

    markdown = docstring_util.append_summary_to_markdown(
        markdown=markdown, summary=summary,
        heading_label='')
    markdown = docstring_util.append_params_or_rtns_to_markdown(
        markdown=markdown, params_or_rtns=parameters)
    markdown = docstring_util.append_params_or_rtns_to_markdown(
        markdown=markdown, params_or_rtns=returns)
    markdown = docstring_util.append_raises_to_markdown(
        markdown=markdown, raises=raises)
    markdown = docstring_util.append_notes_to_markdown(
        markdown=markdown, notes=notes)
    markdown = docstring_util.append_examples_to_markdown(
        markdown=markdown, examples=examples)
    markdown = docstring_util.append_references_to_markdown(
        markdown=markdown, references=references)
    markdown = docstring_util.remove_trailing_hr_tag(markdown=markdown)
    return markdown


def _get_module_toplevel_functions(*, module: ModuleType) -> List[Callable]:
    """
    Get top-level functions from a specified module.

    Parameters
    ----------
    module : ModuleType
        Target module.

    Returns
    -------
    toplevel_functions : list of Callable
        Top-level functions.
    """
    members: List[Tuple[str, Callable]] = inspect.getmembers(
        module, predicate=inspect.isfunction)
    toplevel_functions: List[Callable] = [
        function for _, function in members]
    return toplevel_functions


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

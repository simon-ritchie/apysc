"""The script to convert and sync each docstring to
markdown files.
"""

import inspect
import os
import re
from types import ModuleType
from typing import Callable
from typing import Dict
from typing import List
from typing import Match
from typing import Optional
from typing import Tuple
from typing import Type


def convert_recursively(*, dir_path: str) -> List[str]:
    """
    Convert each docstring in the specified directory
    to markdown files recursively.

    Parameters
    ----------
    dir_path : str
        Target directory path.

    Returns
    -------
    saved_markdown_file_paths : list of str
        list of saved markdown file paths.
    """
    from apysc._lint_and_doc import lint_and_doc_hash_util

    if not os.path.isdir(dir_path):
        return []
    saved_markdown_file_paths: List[str] = []
    file_or_dir_names: List[str] = os.listdir(dir_path)
    for file_or_dir_name in file_or_dir_names:
        file_or_dir_path: str = os.path.join(dir_path, file_or_dir_name)
        if os.path.isdir(file_or_dir_path) and not _is_excluding_dir_path(
            dir_path=file_or_dir_path
        ):
            convert_recursively(dir_path=file_or_dir_path)
            continue
        if not file_or_dir_path.endswith(".py"):
            continue
        is_file_updated: bool = lint_and_doc_hash_util.is_file_updated(
            file_path=file_or_dir_path,
            hash_type=lint_and_doc_hash_util.HashType.DOCSTRING_TO_MARKDOWN,
        )
        if not is_file_updated:
            continue
        saved_markdown_file_path: str = _save_markdown(module_path=file_or_dir_path)
        saved_markdown_file_paths.append(saved_markdown_file_path)
        lint_and_doc_hash_util.save_target_file_hash(
            file_path=file_or_dir_path,
            hash_type=lint_and_doc_hash_util.HashType.DOCSTRING_TO_MARKDOWN,
        )
    return saved_markdown_file_paths


_EXCLUDING_DIR_PATHS: List[str] = [
    "apysc/_translation/",
]


def _is_excluding_dir_path(*, dir_path: str) -> bool:
    """
    Get a boolean indicating whether a specified directory path
    is a excluding condition or not.

    Parameters
    ----------
    dir_path : str
        A target directory path.

    Returns
    -------
    result : bool
        This interface returns True if a specified directory path
        is excluding condition.
    """
    for excluding_dir_path in _EXCLUDING_DIR_PATHS:
        if excluding_dir_path in dir_path:
            return True
    return False


def _save_markdown(*, module_path: str) -> str:
    """
    Save a specified module's markdown file.

    Parameters
    ----------
    module_path : str
        Target Python module path.

    Returns
    -------
    markdown_file_path : str
        Saved markdown file path.
    """
    from apysc._file import file_util

    markdown: str = _convert_module_docstring_to_markdown(module_path=module_path)
    markdown_file_path: str = module_path.replace(".py", ".md", 1)
    if markdown_file_path.startswith("./"):
        markdown_file_path = markdown_file_path.replace("./", "", 1)
    markdown_file_path = os.path.join("./docstring_markdowns/", markdown_file_path)
    file_util.save_plain_txt(txt=markdown, file_path=markdown_file_path)
    return markdown_file_path


def _convert_module_docstring_to_markdown(*, module_path: str) -> str:
    """
    Convert a specified module's docstring to a markdown string.

    Parameters
    ----------
    module_path : str
        Target Python module path.

    Returns
    -------
    markdown : str
        Converted markdown string.
    """
    from apysc._file import file_util
    from apysc._file import module_util

    module: ModuleType = module_util.read_target_path_module(module_path=module_path)
    module_str: str = file_util.read_txt(file_path=module_path)
    markdown: str = f"# `{module.__name__}` docstrings"
    markdown = _append_module_docstring_to_markdown(
        markdown=markdown, docstring=module.__doc__
    )

    toplevel_functions: List[Callable] = _get_module_toplevel_functions(module=module)
    for toplevel_function in toplevel_functions:
        if f"def {toplevel_function.__name__}(" not in module_str:
            continue
        markdown = _append_toplevel_function_docstring_to_markdown(
            markdown=markdown, toplevel_function=toplevel_function
        )

    toplevel_classes: List[Type] = _get_toplevel_classes(module=module)
    for toplevel_class in toplevel_classes:
        match: Optional[Match] = re.search(
            pattern=(rf"class {toplevel_class.__name__}[:\(]"), string=module_str
        )
        if match is None:
            continue
        markdown = _append_toplevel_class_docstring_to_markdown(
            markdown=markdown, toplevel_class=toplevel_class, module_str=module_str
        )

    return markdown


def _append_toplevel_class_docstring_to_markdown(
    *, markdown: str, toplevel_class: Type, module_str: str
) -> str:
    """
    Append a top-level class docstring to a specified
    markdown string.

    Parameters
    ----------
    markdown : str
        Target markdown string.
    toplevel_class : Type
        Target top-level class.
    module_str : str
        Target Python module's string.

    Returns
    -------
    markdown : str
        A result markdown string.
    """
    markdown += f"\n\n## `{toplevel_class.__name__}` class docstring"
    if toplevel_class.__doc__ is not None:
        markdown = _append_each_section_to_markdown(
            markdown=markdown, docstring=toplevel_class.__doc__
        )

    methods: List[Callable] = _get_methods_from_class(class_=toplevel_class)
    for method in methods:
        if method.__doc__ is None:
            continue
        if f"    def {method.__name__}(" not in module_str:
            continue
        markdown += f"\n\n### `{method.__name__}` method docstring"
        markdown = _append_each_section_to_markdown(
            markdown=markdown, docstring=method.__doc__
        )

    return markdown


def _get_methods_from_class(*, class_: Type) -> List[Callable]:
    """
    Get methods from a specified class.

    Parameters
    ----------
    class_ : Type
        Target class.

    Returns
    -------
    methods : list of Callable
        Extracted methods.
    """
    members: List[Tuple[str, Callable]] = inspect.getmembers(class_, predicate=callable)
    methods: List[Callable] = []
    excluding_target_builtin_methods_dict: Dict[
        str, str
    ] = _get_excluding_target_builtin_methods()
    for _, method in members:
        if method.__doc__ is None:
            continue
        builtin_docstring: str = excluding_target_builtin_methods_dict.get(
            method.__name__, ""
        )
        if method.__doc__ == builtin_docstring or method.__name__ == "type":
            continue
        methods.append(method)
    return methods


def _get_excluding_target_builtin_methods() -> Dict[str, str]:
    """
    Get an excluding target built-in methods' docstring
    values dict.

    Returns
    -------
    excluding_target_builtin_methods_dict : dict
        A dictionary which has builtin method name's keys
        and docstring values.
    """

    class _EmptyClass:
        pass

    members: List[Tuple[str, Callable]] = inspect.getmembers(
        _EmptyClass, predicate=callable
    )
    excluding_target_builtin_methods_dict: Dict[str, str] = {}
    for method_name, method in members:
        if method.__doc__ is None:
            continue
        excluding_target_builtin_methods_dict[method_name] = method.__doc__
    return excluding_target_builtin_methods_dict


def _get_toplevel_classes(*, module: ModuleType) -> List[Type]:
    """
    Get top-level classes from a specified module.

    Parameters
    ----------
    module : ModuleType
        Target module.

    Returns
    -------
    toplevel_classes : list of Type
        Top-level classes.
    """
    members: List[Tuple[str, Type]] = inspect.getmembers(
        module, predicate=inspect.isclass
    )
    toplevel_classes: List[Type] = [class_ for _, class_ in members]
    return toplevel_classes


def _append_toplevel_function_docstring_to_markdown(
    *, markdown: str, toplevel_function: Callable
) -> str:
    """
    Append a top-level function docstring to a specified
    markdown string.

    Parameters
    ----------
    markdown : str
        Target markdown string.
    toplevel_function : Callable
        Target top-level functions.

    Returns
    -------
    markdown : str
        A result markdown string.
    """
    if toplevel_function.__doc__ is None:
        return markdown
    if markdown != "":
        markdown += "\n\n"
    markdown += f"## `{toplevel_function.__name__}` function docstring"
    markdown = _append_each_section_to_markdown(
        markdown=markdown,
        docstring=toplevel_function.__doc__,
    )
    return markdown


def _append_each_section_to_markdown(markdown: str, docstring: str) -> str:
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
        A result markdown string.
    """
    from apysc._lint_and_doc import docstring_util
    from apysc._lint_and_doc.docstring_util import Example
    from apysc._lint_and_doc.docstring_util import Parameter
    from apysc._lint_and_doc.docstring_util import Raise
    from apysc._lint_and_doc.docstring_util import Reference
    from apysc._lint_and_doc.docstring_util import Return

    summary: str = docstring_util.extract_summary_from_docstring(docstring=docstring)
    parameters: List[
        Parameter
    ] = docstring_util.extract_param_or_rtn_values_from_docstring(
        target_type=Parameter, docstring=docstring
    )
    returns: List[Return] = docstring_util.extract_param_or_rtn_values_from_docstring(
        target_type=Return, docstring=docstring
    )
    raises: List[Raise] = docstring_util.extract_raise_values_from_docstring(
        docstring=docstring
    )
    notes: str = docstring_util.extract_notes_from_docstring(docstring=docstring)
    examples: List[Example] = docstring_util.extract_example_values_from_docstring(
        docstring=docstring
    )
    references: List[
        Reference
    ] = docstring_util.extract_reference_values_from_docstring(docstring=docstring)

    markdown = docstring_util.append_summary_to_markdown(
        markdown=markdown, summary=summary, heading_label=""
    )
    markdown = docstring_util.append_params_or_rtns_to_markdown(
        markdown=markdown, params_or_rtns=parameters
    )
    markdown = docstring_util.append_params_or_rtns_to_markdown(
        markdown=markdown, params_or_rtns=returns
    )
    markdown = docstring_util.append_raises_to_markdown(
        markdown=markdown, raises=raises
    )
    markdown = docstring_util.append_notes_to_markdown(markdown=markdown, notes=notes)
    markdown = docstring_util.append_examples_to_markdown(
        markdown=markdown, examples=examples
    )
    markdown = docstring_util.append_references_to_markdown(
        markdown=markdown, references=references
    )
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
        module, predicate=inspect.isfunction
    )
    toplevel_functions: List[Callable] = [function for _, function in members]
    return toplevel_functions


def _append_module_docstring_to_markdown(
    *, markdown: str, docstring: Optional[str]
) -> str:
    """
    Append a module description docstring to a
    specified markdown string.

    Parameters
    ----------
    markdown : str
        Target markdown string.
    docstring : str or None
        Target module description docstring.

    Returns
    -------
    markdown : str
        A result markdown string.
    """
    from apysc._lint_and_doc import docstring_util
    from apysc._lint_and_doc.docstring_util import Reference

    if docstring is None:
        return markdown
    summary: str = docstring_util.extract_summary_from_docstring(docstring=docstring)
    notes: str = docstring_util.extract_notes_from_docstring(docstring=docstring)
    references: List[
        Reference
    ] = docstring_util.extract_reference_values_from_docstring(docstring=docstring)

    if markdown != "":
        markdown += "\n\n"
    markdown += "## Module summary"
    markdown = docstring_util.append_summary_to_markdown(
        markdown=markdown, summary=summary, heading_label=""
    )
    markdown = docstring_util.append_notes_to_markdown(markdown=markdown, notes=notes)
    markdown = docstring_util.append_references_to_markdown(
        markdown=markdown, references=references
    )
    markdown = docstring_util.remove_trailing_hr_tag(markdown=markdown)
    return markdown

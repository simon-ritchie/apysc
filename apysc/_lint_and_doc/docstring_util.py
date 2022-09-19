"""Utility implementations for docstrings.

Mainly the following interfaces are defined:

- get_docstring_src_module_paths
    - Get docstring source module paths from a specified
        markdown file path.
- reset_replaced_docstring_section
    - Reset converted a markdown's docstring section.
- replace_docstring_path_specification
    - Replace a docstring path specification with a converted
        docstring text in a specified markdown document.
- remove_trailing_hr_tag
    - Remove a trailing `<hr>` tag from a specified markdown string.
- append_summary_to_markdown
    - Append an interface summary string to a specified
        markdown string.
- append_notes_to_markdown
    - Append a notes string to a specified markdown string.
- extract_notes_from_docstring
    - Extract a notes' value from a docstring.
- append_examples_to_markdown
    - Append examples to a specified markdown string.
- extract_example_values_from_docstring
    - Extract example values from a docstring.
- append_references_to_markdown
    - Append references to a specified markdown string.
- append_raises_to_markdown
    - Append raises to a specified markdown string.
- append_params_or_rtns_to_markdown
    - Append parameters or returns to a specified markdown string.
- extract_reference_values_from_docstring
    - Extract reference values from a docstring.
- extract_raise_values_from_docstring
    - Extract raise values from a docstring.
- extract_param_or_rtn_values_from_docstring
    - Extract parameter or return values from a docstring.
- extract_summary_from_docstring
    - Extract a summary text from a docstring.
- extract_docstrings_from_module
    - Extract docstrings from a specified module.
"""

import inspect
import os
import re
from enum import Enum
from inspect import Signature
from types import ModuleType
from typing import Any
from typing import Callable
from typing import List
from typing import Match
from typing import Optional
from typing import Pattern
from typing import Tuple
from typing import Type
from typing import TypeVar

from typing_extensions import final

DOCSTRING_PATH_COMMENT_KEYWORD: str = "Docstring:"
DOCSTRING_PATH_COMMENT_PATTERN: str = (
    rf"^\<\!\-\-.*?{DOCSTRING_PATH_COMMENT_KEYWORD}" r"(?P<path>.*?)\-\-\>"
)

_HYPHENS_LINE_PATTERN: str = r"(\s{4}|^)-----"


class _SectionPattern(Enum):
    PARAMETERS = r"(\s{4}|^)Parameters$"
    RETURNS = r"(\s{4}|^)Returns$"
    YIELDS = r"(\s{4}|^)Yields$"
    RECEIVES = r"(\s{4}|^)Receives$"
    RAISES = r"(\s{4}|^)Raises$"
    WARNS = r"(\s{4}|^)Warns$"
    WARNINGS = r"(\s{4}|^)Warnings$"
    SEE_ALSO = r"(\s{4}|^)See Also$"
    NOTES = r"(\s{4}|^)Notes$"
    REFERENCES = r"(\s{4}|^)References$"
    EXAMPLES = r"(\s{4}|^)Examples$"
    ATTRIBUTES = r"(\s{4}|^)Attributes$"
    METHODS = r"(\s{4}|^)Methods$"


def get_docstring_src_module_paths(md_file_path: str) -> List[str]:
    """
    Get docstring source module paths from a specified
    markdown file path.

    Parameters
    ----------
    md_file_path : str
        Target markdown file path.

    Returns
    -------
    module_paths : list of str
        Extracted docstring source module paths.
    """
    from apysc._file import file_util
    from apysc._file import module_util

    md_txt: str = file_util.read_txt(file_path=md_file_path)
    lines: List[str] = md_txt.splitlines()
    module_paths: List[str] = []
    pattern: Pattern = re.compile(pattern=DOCSTRING_PATH_COMMENT_PATTERN)
    for line in lines:
        if not line.startswith("<!--"):
            continue
        match: Optional[Match] = pattern.search(string=line)
        if match is None:
            continue
        package_path: str = match.group(1).rsplit(".", maxsplit=1)[0]
        package_path = package_path.strip()
        module_or_class: Any = module_util.read_module_or_class_from_package_path(
            module_or_class_package_path=package_path
        )
        if inspect.isclass(module_or_class):
            package_path = package_path.rsplit(".", maxsplit=1)[0]
        module_path: str = package_path.replace(".", "/")
        module_path = f"./{module_path}.py"
        module_paths.append(module_path)
    return module_paths


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
        md_txt=md_txt, matches=matches
    )
    with open(md_file_path, "w") as f:
        f.write(md_txt)
    return True


def _remove_replaced_docstring_section_from_md_txt(
    *, md_txt: str, matches: List[str]
) -> str:
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
            if line.startswith("#"):
                result_lines.append(f"\n{line}")
                is_reset_section_range = False
            continue
        docstring_path_specification_comment: str = (
            _extract_docstring_path_specification_comment_from_line(
                line=line, matches=matches
            )
        )
        if docstring_path_specification_comment != "":
            result_lines.append(line)
            is_reset_section_range = True
            continue
        result_lines.append(line)
    md_txt = "\n".join(result_lines)
    return md_txt


def _extract_docstring_path_specification_comment_from_line(
    *, line: str, matches: List[str]
) -> str:
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
    return ""


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
        pattern=DOCSTRING_PATH_COMMENT_PATTERN, string=md_txt, flags=re.MULTILINE
    ):
        matches.append(match.group(0))
    return matches


def replace_docstring_path_specification(*, md_file_path: str) -> None:
    """
    Replace a docstring path specification with a converted
    docstring text in a specified markdown document.

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
            pattern=DOCSTRING_PATH_COMMENT_PATTERN, string=line
        )
        if match is not None:
            result_lines.append(line)
            result_lines.append("")
            markdown_format_docstring: str = (
                _convert_docstring_path_comment_to_markdown_format(
                    docstring_path_comment=match.group(0),
                    md_file_path=md_file_path,
                )
            )
            result_lines.append(markdown_format_docstring)
            continue

        result_lines.append(line)
        continue
    md_txt = "\n".join(result_lines)
    file_util.save_plain_txt(txt=md_txt, file_path=md_file_path)


class _DocstringPathNotFoundError(Exception):
    pass


class _DocstringCallableNotExistsError(Exception):
    pass


def _convert_docstring_path_comment_to_markdown_format(
    *, docstring_path_comment: str, md_file_path: str
) -> str:
    """
    Convert a specified docstring path comment to a
    markdown format text.

    Parameters
    ----------
    docstring_path_comment : str
        Target docstring path comment.
    md_file_path : str
        Target markdown file path.

    Returns
    -------
    markdown_format_docstring : str
        Converted text.
    """
    module_or_class_package_path: str
    callable_name: str
    (
        module_or_class_package_path,
        callable_name,
    ) = _extract_package_path_and_callable_name_from_path(
        docstring_path_comment=docstring_path_comment,
    )
    callable_: Callable = _get_callable_from_package_path_and_callable_name(
        module_or_class_package_path=module_or_class_package_path,
        callable_name=callable_name,
    )
    if callable_.__doc__ is None:
        return ""
    if callable(callable_):
        signature: Optional[Signature] = inspect.signature(callable_)
        callable_name = callable_.__name__
    else:
        signature = None
        callable_name = ""
    markdown_format_docstring: str = _convert_docstring_to_markdown(
        docstring=callable_.__doc__,
        signature=signature,
        callable_name=callable_name,
        md_file_path=md_file_path,
    )
    return markdown_format_docstring


def _get_callable_from_package_path_and_callable_name(
    *, module_or_class_package_path: str, callable_name: str
) -> Callable:
    """
    Get a callable object from a specified package path and
    callable name.

    Parameters
    ----------
    module_or_class_package_path : str
        Target module or class package path.
    callable_name : str
        Target callable name.

    Raises
    ------
    _DocstringPathNotFoundError
        If a specified package path's module or class
        does not exist.
    _DocstringCallableNotExistsError
        If a target module or class does not have a specified
        name function or method.

    Returns
    -------
    callable_ : Callable
        Target callable object.
    """
    from apysc._file import module_util

    try:
        module_or_class: Any = module_util.read_module_or_class_from_package_path(
            module_or_class_package_path=module_or_class_package_path
        )
    except Exception:
        raise _DocstringPathNotFoundError(
            "Could not found module or class of the docstring path."
            f"\nModule or class package path: {module_or_class_package_path}"
        )
    try:
        callable_: Callable = getattr(module_or_class, callable_name)
    except Exception:
        raise _DocstringCallableNotExistsError(
            "Specified docstring path's module or class does not have "
            "a target callable attribute."
            f"\nModule or class package path: {module_or_class_package_path}",
            f"\nCallable name: {callable_name}",
        )
    return callable_


def _convert_docstring_to_markdown(
    *,
    docstring: str,
    signature: Optional[Signature],
    callable_name: str,
    md_file_path: str,
) -> str:
    """
    Convert a specified docstring to a markdown format text.

    Parameters
    ----------
    docstring : str
        Target docstring.
    signature : Signature or None
        Target callable's signature. If a target interface
        is property, this argument becomes None.
    callable_name : str
        Target callable name.
    md_file_path : str
        Target markdown file path.

    Returns
    -------
    markdown : str
        Converted markdown text.
    """
    summary: str = extract_summary_from_docstring(docstring=docstring)
    parameters: List[Parameter] = extract_param_or_rtn_values_from_docstring(
        target_type=Parameter, docstring=docstring
    )
    returns: List[Return] = extract_param_or_rtn_values_from_docstring(
        target_type=Return, docstring=docstring
    )
    raises: List[Raise] = extract_raise_values_from_docstring(docstring=docstring)
    notes: str = extract_notes_from_docstring(docstring=docstring)
    examples: List[Example] = extract_example_values_from_docstring(docstring=docstring)
    references: List[Reference] = extract_reference_values_from_docstring(
        docstring=docstring
    )
    references = _slice_references_by_md_file_path(
        references=references, md_file_path=md_file_path
    )
    markdown: str = (
        '<span class="inconspicuous-txt">Note: the document '
        "build script generates and updates this "
        "API document section automatically. Maybe this section "
        "is duplicated compared with previous sections.</span>"
    )
    if signature is not None:
        markdown += f"\n\n**[Interface signature]** `{callable_name}{signature}`<hr>"
    markdown = append_summary_to_markdown(
        markdown=markdown, summary=summary, heading_label="**[Interface summary]**\n\n"
    )
    markdown = append_params_or_rtns_to_markdown(
        markdown=markdown, params_or_rtns=parameters
    )
    markdown = append_params_or_rtns_to_markdown(
        markdown=markdown, params_or_rtns=returns
    )
    markdown = append_raises_to_markdown(markdown=markdown, raises=raises)
    markdown = append_notes_to_markdown(markdown=markdown, notes=notes)
    markdown = append_examples_to_markdown(markdown=markdown, examples=examples)
    markdown = append_references_to_markdown(markdown=markdown, references=references)
    markdown = remove_trailing_hr_tag(markdown=markdown)
    return markdown


def remove_trailing_hr_tag(*, markdown: str) -> str:
    """
    Remove a trailing `<hr>` tag from a specified markdown string.

    Parameters
    ----------
    markdown : str
        Target markdown string.

    Returns
    -------
    markdown : str
        A result markdown string.
    """
    markdown = markdown.strip()
    hr_tag: str = "<hr>"
    if markdown.endswith(hr_tag):
        markdown = markdown[: -len(hr_tag)]
    markdown = markdown.strip()
    return markdown


def append_summary_to_markdown(
    *, markdown: str, summary: str, heading_label: str
) -> str:
    """
    Append an interface summary string to a specified
    markdown string.

    Parameters
    ----------
    markdown : str
        Target markdown string.
    summary : str
        Target summary string.
    heading_label : str
        A label to append at the beginning.

    Returns
    -------
    markdown : str
        A result markdown string.
    """
    if summary == "":
        return markdown
    if markdown != "":
        markdown += "\n\n"
    if summary.strip().startswith("<br>"):
        summary = summary.replace("<br>", "", 1)
    markdown += f"{heading_label}{summary}<hr>"
    return markdown


def append_notes_to_markdown(*, markdown: str, notes: str) -> str:
    """
    Append a notes string to a specified markdown string.

    Parameters
    ----------
    markdown : str
        Target markdown string.
    notes : str
        Target notes string.

    Returns
    -------
    markdown : str
        A result markdown string.
    """
    if notes == "":
        return markdown
    if markdown != "":
        markdown += "\n\n"
    if notes.strip().startswith("<br>"):
        notes = notes.replace("<br>", "", 1)
    markdown += "**[Notes]**" f"\n\n{notes}<hr>"
    return markdown


def extract_notes_from_docstring(*, docstring: str) -> str:
    """
    Extract a notes' value from a docstring.

    Parameters
    ----------
    docstring : str
        Target docstring.

    Returns
    -------
    notes : str
        Extract notes text value.
    """
    lines: List[str] = docstring.splitlines()
    lines = _remove_blank_lines_from_list(lines=lines)
    is_notes_section_range: bool = False
    notes_lines: List[str] = []
    for line in lines:
        if _is_target_section_pattern_line(
            line=line, section_pattern=_SectionPattern.NOTES
        ):
            is_notes_section_range = True
            continue
        if _is_skip_target_line(
            is_target_section_range=is_notes_section_range, line=line
        ):
            continue
        if _is_section_line(line=line):
            break

        line = _append_br_tag_and_replace_symbol_if_first_char_is_hyphen(line=line)
        notes_lines.append(line)
    notes: str = "\n".join(notes_lines)
    notes = _remove_line_breaks_and_unnecessary_spaces(text=notes)
    return notes


class _ParamOrRtnBase:
    _name: str
    _type_str: str
    _description: str

    def __init__(self, *, name: str, type_str: str, description: str) -> None:
        """
        Parameter or return value's base class.

        Parameters
        ----------
        name : str
            Parameter or return value name.
        type_str : str
            Parameter or return value type name.
        description : str
            Parameter or return value description.
        """
        self._name = name
        self._type_str = type_str
        self._description = description

    def __eq__(self, other: Any) -> bool:
        """
        The method for equality comparison.

        Parameters
        ----------
        other : Any
            The other instance to compare.

        Returns
        -------
        result : bool
            If each attribute is equal to the other, this
            method returns True.
        """
        if not isinstance(other, _ParamOrRtnBase):
            return False
        if self.name != other.name:
            return False
        if self.type_str != other.type_str:
            return False
        if self.description != other.description:
            return False
        return True

    @property
    def name(self) -> str:
        """
        Get a parameter or return value name.

        Returns
        -------
        name : str
            A parameter or return value name.
        """
        return self._name

    @property
    def type_str(self) -> str:
        """
        Get a parameter or return value type name.

        Returns
        -------
        type_str : str
            A parameter or return value type name.
        """
        return self._type_str

    @property
    def description(self) -> str:
        """
        Get a parameter or return value description.

        Returns
        -------
        description : str
            A parameter or return value description.
        """
        return self._description


class Parameter(_ParamOrRtnBase):
    """Parameter value type."""


class Return(_ParamOrRtnBase):
    """Return value type."""


class Raise:
    """Raise value type."""

    _err_class_name: str
    _description: str

    def __init__(self, *, err_class_name: str, description: str) -> None:
        """
        Raise value type.

        Parameters
        ----------
        err_class_name : str
            Target error class name.
        description : str
            Error condition description.
        """
        self._err_class_name = err_class_name
        self._description = description

    @property
    def err_class_name(self) -> str:
        """
        Get a target error class name.

        Returns
        -------
        err_class_name : str
            A target error class name.
        """
        return self._err_class_name

    @property
    def description(self) -> str:
        """
        Get a error condition description.

        Returns
        -------
        description : str
            A error condition description.
        """
        return self._description

    def __eq__(self, other: Any) -> bool:
        """
        The method for equality comparison.

        Parameters
        ----------
        other : Any
            The other value to compare.

        Returns
        -------
        result : bool
            If each attribute is equal to the other, this
            method returns True.
        """
        if not isinstance(other, Raise):
            return False
        if self.err_class_name != other.err_class_name:
            return False
        if self._description != other._description:
            return False
        return True


class Reference:
    """Reference value type."""

    _page_label: str
    _url: str

    def __init__(self, *, page_label: str, url: str) -> None:
        """
        Reference value type.

        Parameters
        ----------
        page_label : str
            Target reference page label.
        url : str
            Target reference page URL.
        """
        self._page_label = page_label
        self._url = url

    @property
    def page_label(self) -> str:
        """
        Get a target reference page label.

        Returns
        -------
        page_label : str
            A target reference page label.
        """
        return self._page_label

    @property
    def url(self) -> str:
        """
        Get a target reference page URL.

        Returns
        -------
        url : str
            A target reference page.
        """
        return self._url

    @final
    def __eq__(self, other: Any) -> bool:
        """
        The method for equality comparison.

        Parameters
        ----------
        other : Any
            The other value to compare.

        Returns
        -------
        result : bool
            If each attribute is equal to the other, this
            method returns True.
        """
        if not isinstance(other, Reference):
            return False
        if self.page_label != other.page_label:
            return False
        if self.url != other.url:
            return False
        return True


class Example:
    """Example value type."""

    _input_code_block: str
    _expected_output: str

    def __init__(self, *, input_code_block: str, expected_output: str = "") -> None:
        """
        Example value type.

        Parameters
        ----------
        input_code_block : str
            Input code block string.
        expected_output : str, default ''
            Expected output string.
        """
        self._input_code_block = input_code_block
        self._expected_output = expected_output

    @property
    def input_code_block(self) -> str:
        """
        Get a input code block string.

        Returns
        -------
        input_code_block : str
            A input code block string.
        """
        return self._input_code_block

    @property
    def expected_output(self) -> str:
        """
        Get a expected output string.

        Returns
        -------
        expected_output : str
            A expected output string.
        """
        return self._expected_output

    def __eq__(self, other: Any) -> bool:
        """
        The method for equality comparison.

        Parameters
        ----------
        other : Any
            The other value to compare.

        Returns
        -------
        result : bool
            If each attribute is equal to the other, this
            method returns True.
        """
        if not isinstance(other, Example):
            return False
        if self.input_code_block != other.input_code_block:
            return False
        if self.expected_output != other.expected_output:
            return False
        return True


def _slice_references_by_md_file_path(
    references: List[Reference], md_file_path: str
) -> List[Reference]:
    """
    Slice a specified references list to exclude the
    same URL's document file.

    Parameters
    ----------
    references : list of Reference
        Target references list to slice.
    md_file_path : str
        Target markdown file path.

    Returns
    -------
    sliced_references : list of Reference
        Sliced list.
    """
    md_file_name: str = os.path.basename(md_file_path)
    md_file_name = md_file_name.rsplit(".", maxsplit=1)[0]
    sliced_references: List[Reference] = []
    for reference in references:
        reference_file_name: str = reference.url.rsplit("/", 1)[-1]
        reference_file_name = reference_file_name.rsplit(".", maxsplit=1)[0]
        if reference_file_name == md_file_name:
            continue
        sliced_references.append(reference)
    return sliced_references


def append_examples_to_markdown(*, markdown: str, examples: List[Example]) -> str:
    """
    Append examples to a specified markdown string.

    Parameters
    ----------
    markdown : str
        Target markdown string.
    examples : list of Example
        Examples list value to append.

    Returns
    -------
    markdown : str
        A result markdown string.
    """
    if not examples:
        return markdown
    if markdown != "":
        markdown += "\n\n"
    markdown += "**[Examples]**\n\n```py"
    for i, example in enumerate(examples):
        if i != 0:
            markdown += "\n"
        markdown += f"\n{example.input_code_block}"
        if example.expected_output != "":
            markdown += f"\n{example.expected_output}"
    markdown += "\n```"
    markdown += "\n\n<hr>"
    return markdown


def extract_example_values_from_docstring(*, docstring: str) -> List[Example]:
    """
    Extract example values from a docstring.

    Parameters
    ----------
    docstring : str
        Target docstring.

    Returns
    -------
    example_values : list of Example
        Extracted example values.
    """
    lines: List[str] = docstring.splitlines()
    lines = _remove_blank_lines_from_list(lines=lines)
    is_example_section_range: bool = False
    input_code_block_lines: List[str] = []
    example_values: List[Example] = []
    for line in lines:
        if _is_target_section_pattern_line(
            line=line, section_pattern=_SectionPattern.EXAMPLES
        ):
            is_example_section_range = True
            continue
        if _is_skip_target_line(
            is_target_section_range=is_example_section_range, line=line
        ):
            continue
        if _is_section_line(line=line):
            break
        if _is_example_output_line(line=line):
            _make_example_and_append_to_list(
                example_values=example_values,
                input_code_block_lines=input_code_block_lines,
                expected_output=line,
            )
            continue
        input_code_block_lines.append(line)
    _make_example_and_append_to_list(
        example_values=example_values,
        input_code_block_lines=input_code_block_lines,
        expected_output="",
    )
    return example_values


def _make_example_and_append_to_list(
    *,
    example_values: List[Example],
    input_code_block_lines: List[str],
    expected_output: str,
) -> None:
    """
    Make an example value and append it to a specified list.

    Notes
    -----
    This function clears a list of input code block lines.

    Parameters
    ----------
    example_values : list of Example
        A list to append an example value.
    input_code_block_lines : list of str
        A list of input code block lines.
    expected_output : str
        An expected output string.
    """
    if not input_code_block_lines:
        return
    input_code_block_lines_: List[str] = [
        line.strip() for line in input_code_block_lines
    ]
    input_code_block: str = "\n".join(input_code_block_lines_)
    example: Example = Example(
        input_code_block=input_code_block, expected_output=expected_output.strip()
    )
    example_values.append(example)
    input_code_block_lines.clear()


def _is_example_output_line(*, line: str) -> bool:
    """
    Get a boolean indicating whether a specified line
    is an example section's output line or not.

    Parameters
    ----------
    line : str
        Target docstring line.

    Returns
    -------
    result : bool
        This function returns True if a specified line
        is an example section's output line.
    """
    line = line.strip()
    if line.startswith(">>>") or line.startswith("..."):
        return False
    return True


def append_references_to_markdown(markdown: str, references: List[Reference]) -> str:
    """
    Append references to a specified markdown string.

    Parameters
    ----------
    markdown : str
        Target markdown string.
    references : list of Reference
        References list value to append.

    Returns
    -------
    markdown : str
        A result markdown string.
    """
    if not references:
        return markdown
    if markdown != "":
        markdown += "\n\n"
    markdown += "**[References]**\n"
    for reference in references:
        markdown += f"\n- [{reference.page_label}]({reference.url})"
    markdown += "\n\n<hr>"
    return markdown


def append_raises_to_markdown(*, markdown: str, raises: List[Raise]) -> str:
    """
    Append raises to a specified markdown string.

    Parameters
    ----------
    markdown : str
        Target markdown string.
    raises : list of Raise
        Raises list value to append.

    Returns
    -------
    markdown : str
        A result markdown string.
    """
    if not raises:
        return markdown
    if markdown != "":
        markdown += "\n\n"
    markdown += "**[Raises]**\n"
    for raise_ in raises:
        markdown += f"\n- {raise_.err_class_name}: {raise_.description}"
    markdown += "\n\n<hr>"
    return markdown


_ParamOrRtn = TypeVar("_ParamOrRtn", Parameter, Return)


def append_params_or_rtns_to_markdown(
    *, markdown: str, params_or_rtns: List[_ParamOrRtn]
) -> str:
    """
    Append parameters or returns to a specified markdown string.

    Parameters
    ----------
    markdown : str
        Target markdown string.
    params_or_rtns : list of _ParamOrRtn
        Parameters or returns to append to.

    Returns
    -------
    markdown : str
        A result markdown string.
    """
    if not params_or_rtns:
        return markdown
    if isinstance(params_or_rtns[0], Parameter):
        section_label: str = "Parameters"
    else:
        section_label = "Returns"
    if markdown != "":
        markdown += "\n\n"
    markdown += f"**[{section_label}]**\n"
    for parameter in params_or_rtns:
        markdown += (
            f"\n- `{parameter.name}`: {parameter.type_str}"
            f"\n  - {parameter.description}"
        )
    markdown += "\n\n<hr>"
    return markdown


def extract_reference_values_from_docstring(*, docstring: str) -> List[Reference]:
    """
    Extract reference values from a docstring.

    Parameters
    ----------
    docstring : str
        Target docstring.

    Returns
    -------
    reference_values : list of Reference
        Extracted reference values.
    """
    lines: List[str] = docstring.splitlines()
    lines = _remove_blank_lines_from_list(lines=lines)
    is_references_section_range: bool = False
    page_label: str = ""
    url: str = ""
    base_indent_num: int = 0
    reference_values: List[Reference] = []
    for line in lines:
        current_indent_num: int = _get_indent_num_from_line(line=line)
        base_indent_num = _get_base_indent_num_if_not_set(
            line=line, base_indent_num=base_indent_num
        )
        if _is_target_section_pattern_line(
            line=line, section_pattern=_SectionPattern.REFERENCES
        ):
            is_references_section_range = True
            continue
        if _is_skip_target_line(
            is_target_section_range=is_references_section_range, line=line
        ):
            continue
        if _is_section_line(line=line):
            break
        if current_indent_num == base_indent_num:
            page_label = _remove_unnecessary_markdown_list_from_line(line=line)
            continue
        url = _remove_unnecessary_markdown_list_from_line(line=line)
        url = _remove_noqa(string=url)
        _make_reference_and_append_to_list(
            reference_values=reference_values, page_label=page_label, url=url
        )
        url = ""
    _make_reference_and_append_to_list(
        reference_values=reference_values, page_label=page_label, url=url
    )
    return reference_values


def _remove_noqa(string: str) -> str:
    """
    Remove a noqa comment from a specified string.

    Parameters
    ----------
    string : str
        Target string.

    Returns
    -------
    string : str
        Result string.
    """
    string = string.replace("# noqa", "", 1).strip()
    return string


def _make_reference_and_append_to_list(
    *, reference_values: List[Reference], page_label: str, url: str
) -> None:
    """
    Make a reference value and append it to a specified list.

    Parameters
    ----------
    reference_values : list of Reference
        A list to append a reference value.
    page_label : str
        Target reference page label.
    url : str
        Target reference page URL.
    """
    if url == "":
        return
    reference: Reference = Reference(page_label=page_label, url=url)
    reference_values.append(reference)


def _remove_unnecessary_markdown_list_from_line(*, line: str) -> str:
    """
    Remove unnecessary markdown list string from a line.

    Parameters
    ----------
    line : str
        Target docstring line.

    Returns
    -------
    line : str
        Result docstring line.
    """
    line = line.replace("- ", "", 1)
    line = line.strip()
    return line


def extract_raise_values_from_docstring(*, docstring: str) -> List[Raise]:
    """
    Extract raise values from a docstring.

    Parameters
    ----------
    docstring : str
        Target docstring.

    Returns
    -------
    raise_values : list of Raise
        Extracted raise values.
    """
    lines: List[str] = docstring.splitlines()
    lines = _remove_blank_lines_from_list(lines=lines)
    is_raises_section_range: bool = False
    err_class_name: str = ""
    base_indent_num: int = 0
    description_lines: List[str] = []
    raise_values: List[Raise] = []
    for line in lines:
        current_indent_num: int = _get_indent_num_from_line(line=line)
        base_indent_num = _get_base_indent_num_if_not_set(
            line=line, base_indent_num=base_indent_num
        )
        if _is_target_section_pattern_line(
            line=line, section_pattern=_SectionPattern.RAISES
        ):
            is_raises_section_range = True
            continue
        if _is_skip_target_line(
            is_target_section_range=is_raises_section_range, line=line
        ):
            continue
        if _is_section_line(line=line):
            break
        if current_indent_num == base_indent_num:
            _make_raise_description_and_append_to_list(
                raise_values=raise_values,
                err_class_name=err_class_name,
                description_lines=description_lines,
            )
            err_class_name = line.strip()
            continue

        line = _append_br_tag_and_replace_symbol_if_first_char_is_hyphen(line=line)
        description_lines.append(line)
    _make_raise_description_and_append_to_list(
        raise_values=raise_values,
        err_class_name=err_class_name,
        description_lines=description_lines,
    )
    return raise_values


def _append_br_tag_and_replace_symbol_if_first_char_is_hyphen(line: str) -> str:
    """
    Append a break tag and replace the hyphen symbol
    if the first character is the hyphen symbol.

    Parameters
    ----------
    line : str
        Target docstring line.

    Returns
    -------
    line : str
        Replaced docstring line.
    """
    first_char: str = ""
    for char in line:
        if char == " ":
            continue
        first_char = char
        break
    if first_char == "-" and line.strip().startswith("- "):
        line = line.replace("- ", "・", 1)
        line = f"<br>{line}"
    return line


def _remove_blank_lines_from_list(*, lines: List[str]) -> List[str]:
    """
    Remove blank lines from a list of lines.

    Parameters
    ----------
    lines : list of str
        Target list of lines.

    Returns
    -------
    result_lines : list of str
        A blank lines removed line list.
    """
    result_lines: List[str] = []
    for line in lines:
        if line.strip() == "":
            continue
        result_lines.append(line)
    return result_lines


def _get_base_indent_num_if_not_set(*, line: str, base_indent_num: int) -> int:
    """
    Get a base indent number from a line if it is an
    initial value.

    Parameters
    ----------
    line : str
        Target docstring line.
    base_indent_num : int
        Current base indent number.

    Returns
    -------
    base_indent_num : int
        If the base_indent_num argument is zero, this function
        returns the current line indent number. Otherwise, it
        returns the same value of the base_indent_num argument.
    """
    if base_indent_num != 0:
        return base_indent_num
    current_indent_num: int = _get_indent_num_from_line(line=line)
    return current_indent_num


def _make_raise_description_and_append_to_list(
    *, raise_values: List[Raise], err_class_name: str, description_lines: List[str]
) -> None:
    """
    Make a raise value description from a list of lines and
    append raise value to a specified list.

    Notes
    -----
    This function clears a list of description lines.

    Parameters
    ----------
    raise_values : list of Raise
        A list to append a raise value.
    err_class_name : str
        Target error class name.
    description_lines : list of str
        A list of description lines.
    """
    if not description_lines:
        return
    description: str = "\n".join(description_lines)
    description = _remove_line_breaks_and_unnecessary_spaces(text=description)
    raise_: Raise = Raise(err_class_name=err_class_name, description=description)
    raise_values.append(raise_)
    description_lines.clear()


def extract_param_or_rtn_values_from_docstring(
    *, target_type: Type[_ParamOrRtn], docstring: str
) -> List[_ParamOrRtn]:
    """
    Extract parameter or return values from a docstring.

    Parameters
    ----------
    target_type : Type
        Target type of the Parameter or Return.
    docstring : str
        Target docstring.

    Returns
    -------
    param_or_rtn_values : list of Parameter or Return
        Extracted parameter or return values.
    """
    lines: List[str] = docstring.splitlines()
    lines = _remove_blank_lines_from_list(lines=lines)
    is_param_or_rtn_section_range: bool = False
    value_name: str = ""
    value_type_str: str = ""
    base_indent_num: int = 0
    description_lines: List[str] = []
    param_or_rtn_values: List[_ParamOrRtn] = []
    params_or_rtns_section_pattern: _SectionPattern = (
        _get_params_or_rtns_section_pattern_by_type(target_type=target_type)
    )
    for line in lines:
        current_indent_num: int = _get_indent_num_from_line(line=line)
        base_indent_num = _get_base_indent_num_if_not_set(
            line=line, base_indent_num=base_indent_num
        )
        if _is_target_section_pattern_line(
            line=line, section_pattern=params_or_rtns_section_pattern
        ):
            is_param_or_rtn_section_range = True
            continue
        if _is_skip_target_line(
            is_target_section_range=is_param_or_rtn_section_range, line=line
        ):
            continue
        if _is_section_line(line=line):
            break
        if current_indent_num == base_indent_num:
            _make_prm_or_rtn_description_and_append_to_list(
                target_type=target_type,
                param_or_rtn_values=param_or_rtn_values,
                value_name=value_name,
                value_type_str=value_type_str,
                description_lines=description_lines,
            )
            value_name, value_type_str = _get_value_name_and_type_from_line(line=line)
            continue
        description_lines.append(line)
    _make_prm_or_rtn_description_and_append_to_list(
        target_type=target_type,
        param_or_rtn_values=param_or_rtn_values,
        value_name=value_name,
        value_type_str=value_type_str,
        description_lines=description_lines,
    )
    return param_or_rtn_values


def _is_skip_target_line(*, is_target_section_range: bool, line: str) -> bool:
    """
    Get a boolean indicating whether a specified line
    is skipping target or not.

    Parameters
    ----------
    is_target_section_range : bool
        A boolean indicating whether a specified line
        is in a range of target section.
    line : str
        Target docstring line.

    Returns
    -------
    result : bool
        A boolean indicating whether a specified line
        is skipping target or not.
    """
    if not is_target_section_range:
        return True
    if _is_hyphens_line(line=line):
        return True
    return False


def _get_params_or_rtns_section_pattern_by_type(
    *, target_type: Type[_ParamOrRtnBase]
) -> _SectionPattern:
    """
    Get the parameters or returns section pattern
    of a specified type.

    Parameters
    ----------
    target_type : Parameter or Return
        Target type.

    Returns
    -------
    pattern : _SectionPattern
        Target section pattern.

    Raises
    ------
    ValueError
        If a provided argument is an invalid target's type.
    """
    if target_type == Parameter:
        return _SectionPattern.PARAMETERS
    if target_type == Return:
        return _SectionPattern.RETURNS
    raise ValueError(f"Invalid type argument is provided: {target_type}")


def _make_prm_or_rtn_description_and_append_to_list(
    *,
    target_type: Type[_ParamOrRtn],
    param_or_rtn_values: List[_ParamOrRtn],
    value_name: str,
    value_type_str: str,
    description_lines: List[str],
) -> None:
    """
    Make a parameter or return value description from a list of
    lines and append parameter or return value to a specified list.

    Notes
    -----
    This function clears a list of description lines.

    Parameters
    ----------
    target_type : Type
        Target type of the Parameter or Return.
    param_or_rtn_values : lisf of _ParamOrRtnBase
        A list to append a parameter or return value.
    value_name : str
        Parameter or return value name.
    value_type_str : str
        Parameter or return type name.
    description_lines : list of str
        A list of description lines.
    """
    if not description_lines:
        return
    description: str = "\n".join(description_lines)
    description = _remove_line_breaks_and_unnecessary_spaces(text=description)
    param_or_rtn: _ParamOrRtn = target_type(
        name=value_name, type_str=value_type_str, description=description
    )
    param_or_rtn_values.append(param_or_rtn)
    description_lines.clear()


def _get_indent_num_from_line(*, line: str) -> int:
    """
    Get an indentation number from a specified docstring line.

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
        if char != " ":
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
    if ":" not in line:
        return "", ""
    splitted: List[str] = line.split(":", maxsplit=1)
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
    match: Optional[Match] = re.search(pattern=_HYPHENS_LINE_PATTERN, string=line)
    if match is None:
        return False
    return True


def _is_target_section_pattern_line(
    *, line: str, section_pattern: _SectionPattern
) -> bool:
    """
    Get a boolean indicating whether a specified line
    matches a target section pattern or not.

    Parameters
    ----------
    line : str
        Target docstring line.
    section_pattern : _SectionPattern
        Target section pattern.

    Returns
    -------
    result : bool
        If a specified line is the parameters section,
        this function returns True.
    """
    match: Optional[Match] = re.search(pattern=section_pattern.value, string=line)
    if match is None:
        return False
    return True


def extract_summary_from_docstring(*, docstring: str) -> str:
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
    lines: List[str] = docstring.splitlines()
    result_lines: List[str] = []
    for line in lines:
        if _is_section_line(line=line):
            break
        line = _append_br_tag_and_replace_symbol_if_first_char_is_hyphen(line=line)
        result_lines.append(line)
    summary: str = "\n".join(result_lines)
    summary = _remove_line_breaks_and_unnecessary_spaces(text=summary)
    return summary


def _remove_line_breaks_and_unnecessary_spaces(*, text: str) -> str:
    """
    Remove line breaks of single and unnecessary spaces
    (e.g., double spaces and leading and trailing spaces).

    Parameters
    ----------
    text : str
        Target text.

    Returns
    -------
    text : str
        Converted text.
    """
    from apysc._string import string_util

    text = text.strip()
    text = text.replace("\n", " ")
    text = string_util.replace_double_spaces_to_single_space(string=text)
    text = text.strip()
    return text


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
        If a specified docstring line is a section line,
        this function returns True.
    """
    for pattern in _SectionPattern:
        match: Optional[Match] = re.search(pattern=pattern.value, string=line)
        if match is None:
            continue
        return True
    return False


def _extract_package_path_and_callable_name_from_path(
    *, docstring_path_comment: str
) -> Tuple[str, str]:
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
        docstring_path_comment=docstring_path_comment
    )
    if "." not in path:
        return "", ""
    splitted: List[str] = path.rsplit(".", maxsplit=1)
    module_or_class_package_path: str = splitted[0]
    callable_name: str = splitted[1]
    return module_or_class_package_path, callable_name


def _extract_path_from_docstring_comment(*, docstring_path_comment: str) -> str:
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
        pattern=DOCSTRING_PATH_COMMENT_PATTERN, string=docstring_path_comment
    )
    if match is None:
        return ""
    path: str = match.group(1)
    path = path.strip()
    return path


def extract_docstrings_from_module(*, module: ModuleType) -> List[str]:
    """
    Extract docstrings from a specified module.

    Parameters
    ----------
    module : ModuleType
        A target module.

    Returns
    -------
    docstrings : List[str]
        An extracted docstrings list.
    """
    docstrings: List[str] = []
    if module.__doc__ is not None:
        docstrings.append(module.__doc__)

    function_members: List[Tuple[str, Callable]] = inspect.getmembers(
        object=module, predicate=inspect.isfunction
    )
    function: Callable
    for _, function in function_members:
        if function.__doc__ is not None:
            docstrings.append(function.__doc__)

    class_members: List[Tuple[str, Type]] = inspect.getmembers(
        object=module, predicate=inspect.isclass
    )
    class_: Type
    for _, class_ in class_members:
        if class_.__doc__ is not None:
            docstrings.append(class_.__doc__)
        method_members: List[Tuple[str, Callable]] = inspect.getmembers(
            object=class_, predicate=inspect.ismethod
        )
        method: Callable
        for _, method in method_members:
            if method.__doc__ is not None:
                docstrings.append(method.__doc__)

    return docstrings

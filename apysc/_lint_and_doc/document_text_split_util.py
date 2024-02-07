"""This module is for the document splitting utility.
"""

from typing import List
from typing import Union

from typing_extensions import final


class Heading:
    """
    This class is for the document's heading.
    """

    _text: str
    _overall_text: str
    _sharp_num: int

    @final
    def __init__(self, *, heading_text: str) -> None:
        """
        This class is for the document's heading.

        Parameters
        ----------
        heading_text : str
            A heading text of a document.
        """
        self._overall_text = heading_text
        sharp_num: int = 0
        for char in heading_text:
            if char != "#":
                break
            sharp_num += 1
        text: str = heading_text.replace("#", "", sharp_num).strip()
        self._text = text
        self._sharp_num = sharp_num

    @property
    def text(self) -> str:
        """
        Get a heading text except first sharp symbols.

        Returns
        -------
        text : str
            A heading text except first sharp symbols.
        """
        return self._text

    @property
    def overall_text(self) -> str:
        """
        Get an overall heading text.

        Returns
        -------
        overall_text : str
            A overall heading text.
        """
        return self._overall_text

    @property
    def sharp_num(self) -> int:
        """
        Get a sharp number of a heading text's sharp symbols.

        Returns
        -------
        sharp_num : int
            A sharp number of a heading text's sharp symbols.
        """
        return self._sharp_num


class BodyText:
    """
    This class is for a document body text.
    """

    _text: str

    @final
    def __init__(self, *, text: str) -> None:
        """
        This class is for a document body text.

        Parameters
        ----------
        text : str
            A document body text.
        """
        self._text = text.strip()

    @property
    def text(self) -> str:
        """
        Get a document body text.

        Returns
        -------
        text : str
            A document body text.
        """
        return self._text


class CodeBlock:
    _code_block: str
    _overall_code_block: str
    _code_type: str = ""

    @final
    def __init__(self, *, code_block: str) -> None:
        """
        The class for a document code block.

        Parameters
        ----------
        code_block : str
            A document code block.
        """
        code_block = code_block.strip()
        self._overall_code_block = code_block
        code_block_lines: List[str] = []
        lines: List[str] = code_block.splitlines()
        for line in lines:
            if line.startswith("```") and self._code_type == "":
                self._code_type = line.replace("```", "").strip()
                continue
            if line.startswith("```"):
                break
            if line == "# runnable":
                continue
            code_block_lines.append(line)
        self._code_block = "\n".join(code_block_lines).strip()

    @property
    def code_block(self) -> str:
        """
        Get a code block string except triple-quotations.

        Returns
        -------
        code_block : str
            A code block string except triple-quotations.
        """
        return self._code_block

    @property
    def overall_code_block(self) -> str:
        """
        Get an overall code block string.

        Returns
        -------
        overall_code_block : str
            An overall code block string.
        """
        return self._overall_code_block

    @property
    def code_type(self) -> str:
        """
        Get a code type of a code block.

        Returns
        -------
        code_type : str
            A code type (e.g., 'py').
        """
        return self._code_type


def split_markdown_document(
    *, markdown_txt: str
) -> List[Union[Heading, BodyText, CodeBlock]]:
    """
    Split a specified markdown document to `Heading`,
    `BodyText`, and `CodeBlock` values.

    Parameters
    ----------
    markdown_txt : str
        A target markdown document.

    Returns
    -------
    splitted_values : list of Heading, BodyText, and CodeBlock
        A list of splitted `Heading`, `BodyText`, and `CodeBlock`
        values.
    """
    is_code_block: bool = False
    current_code_block_lines: List[str] = []
    current_body_text_lines: List[str] = []
    lines: List[str] = markdown_txt.splitlines()
    splitted_values: List[Union[Heading, BodyText, CodeBlock]] = []
    for line in lines:
        if not is_code_block and line.startswith("```"):
            _create_body_text_and_append_to_list_if_values_exist(
                splitted_values=splitted_values, body_text_lines=current_body_text_lines
            )
            is_code_block = True
            current_code_block_lines.append(line)
            continue

        if is_code_block:
            current_code_block_lines.append(line)
            if line.startswith("```"):
                code_block: CodeBlock = _create_code_block_from_list(
                    code_block_lines=current_code_block_lines
                )
                splitted_values.append(code_block)
                is_code_block = False
                continue
            continue

        if line.startswith("#"):
            _create_body_text_and_append_to_list_if_values_exist(
                splitted_values=splitted_values, body_text_lines=current_body_text_lines
            )
            splitted_values.append(Heading(heading_text=line))
            continue

        current_body_text_lines.append(line)

    _create_body_text_and_append_to_list_if_values_exist(
        splitted_values=splitted_values, body_text_lines=current_body_text_lines
    )
    return splitted_values


def _create_body_text_and_append_to_list_if_values_exist(
    *,
    splitted_values: List[Union[Heading, BodyText, CodeBlock]],
    body_text_lines: List[str]
) -> None:
    """
    Create a body text instance from a specified body
    text lines list and append it to a result list.
    This interface skips the appending if a specified
    body text line list is blank.

    Notes
    -----
    This function clears a specified body text lines list
    at the end.

    Parameters
    ----------
    splitted_values : list of Heading, BodyText, and CodeBlock
        A result list to append a body text instance.
    body_text_lines : list of str
        A target body text line's list.
    """
    if not body_text_lines:
        return
    body_text_str: str = "\n".join(body_text_lines)
    splitted_values.append(BodyText(text=body_text_str))
    body_text_lines.clear()


def _create_code_block_from_list(*, code_block_lines: List[str]) -> CodeBlock:
    """
    Create a code block instance from a specified lines list.

    Notes
    -----
    This function clears a specified list at the end of the
    function.

    Parameters
    ----------
    code_block_lines : list of str
        A target code block lines.

    Returns
    -------
    code_block : CodeBlock
        A created code block instance.
    """
    code_block_str: str = "\n".join(code_block_lines)
    code_block: CodeBlock = CodeBlock(code_block=code_block_str)
    code_block_lines.clear()
    return code_block

"""This module is for the document splitting utility.
"""


from typing import List


class Heading:
    """The class for the document's heading.
    """

    _text: str
    _overall_text: str
    _sharp_num: int

    def __init__(self, *, heading_text: str) -> None:
        """
        The class for the document's heading.

        Parameters
        ----------
        heading_text : str
            A heading text of a document.
        """
        self._overall_text = heading_text
        sharp_num: int = 0
        for char in heading_text:
            if char != '#':
                break
            sharp_num += 1
        text: str = heading_text.replace('#', '', sharp_num).strip()
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
        Get a overall heading text.

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
    """The class for a document body text.
    """

    _text: str

    def __init__(self, text: str) -> None:
        """
        The class for a document body text.

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
    _code_type: str

    def __init__(self, code_block: str) -> None:
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
            if line.startswith('```') and not hasattr(self, '_code_type'):
                self._code_type = line.replace('```', '').strip()
                continue
            if line.startswith('```'):
                break
            if line == '# runnable':
                continue
            code_block_lines.append(line)
        self._code_block = '\n'.join(code_block_lines).strip()

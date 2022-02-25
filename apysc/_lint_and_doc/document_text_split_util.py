"""This module is for the document splitting utility.
"""


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

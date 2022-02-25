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

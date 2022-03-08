"""This module is for the data model of the document's link
text translation mappings.
"""

from types import ModuleType
from typing import List
from typing import Optional
from typing import Tuple

from apysc._lint_and_doc.docs_lang import Lang


class Mapping:
    """This class is for a single link-text translation mapping.
    """

    _link_text: str
    _mapping_text: str

    def __init__(self, *, link_text: str, mapping_text: str) -> None:
        """
        A single link-text translation mapping.

        Parameters
        ----------
        link_text : str
            A link (source) text.
        mapping_text : str
            A mapping (tlanslated) text.
        """
        self._link_text = link_text
        self._mapping_text = mapping_text

    @property
    def link_text(self) -> str:
        """
        Get a link (source) text value.

        Returns
        -------
        link_text : str
            A link (source) text value.
        """
        return self._link_text

    @property
    def mapping_text(self) -> str:
        """
        Get a mapping (tlanslated) text.

        Returns
        -------
        mapping_text : str
            A mapping (tlanslated) text.
        """
        return self.mapping_text

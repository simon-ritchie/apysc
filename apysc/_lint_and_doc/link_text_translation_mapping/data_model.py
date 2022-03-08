"""This module is for the data model of the document's link
text translation mappings.
"""

from types import ModuleType
from typing import List
from typing import Optional
from typing import Tuple
from functools import lru_cache

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
        return self._mapping_text


class Mappings:
    """This class is for link-text translation mappings.
    """

    mappings: List[Mapping]

    def __init__(self, mappings: List[Mapping]) -> None:
        """
        The class for link-text translation mappings.

        Parameters
        ----------
        mappings : list of Mapping
            A target mappings list.
        """
        self.mappings = mappings


def get_link_text_translation_str_if_exists(
        *, key: str, lang: Lang) -> str:
    """
    If a mapping setting exists, get a link-text translation
    string from a specified language key string.

    Parameters
    ----------
    key : str
        A target key string (source English string).
    lang : Lang
        A target language.

    Returns
    -------
    translation_str : str
        A translated string. If there is no link-text translation
        mapping setting, this interface returns a blank string.
    """
    mappings: Optional[Mappings] = _read_mappings(lang=lang)
    pass


@lru_cache(maxsize=None)
def _read_mappings(*, lang: Lang) -> Optional[Mappings]:
    """
    Read a link-text translation mappings settings if it exists.

    Parameters
    ----------
    lang : Lang
        A target language.

    Returns
    -------
    mappings : Mappings or None
        A read mappings settings. If there is no mappings
        settings, this interface returns None.
    """
    from apysc._file import module_util
    module_path: str = _get_mapping_module_path_from_lang(lang=lang)
    pass


def _get_mapping_module_path_from_lang(*, lang: Lang) -> str:
    """
    Get a link-text translation mappings settings module path
    of a specified language.

    Parameters
    ----------
    lang : Lang
        A target language.

    Returns
    -------
    module_path : str
        A link-text translation mappings settings module path
        of a specified language.
    """
    module_path: str = (
        './apysc/_lint_and_doc/link_text_translation_mapping/'
        f'{lang.value}.py'
    )
    return module_path

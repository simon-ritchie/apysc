from abc import ABC
from abc import abstractmethod
from typing import Union

from apysc._type.string import String


class CssInterface(ABC):
    @abstractmethod
    def get_css(self, *, name: Union[str, String]) -> String:
        """
        Get a CSS value string.

        Parameters
        ----------
        name : str or String
            CSS name (e.g., 'display').

        Returns
        -------
        css : ap.String
            CSS value.

        References
        ----------
        - Display object get_css and set_css interfaces
            - https://simon-ritchie.github.io/apysc/en/display_object_get_and_set_css.html  # noqa
        """
        return String("")

    @abstractmethod
    def set_css(self, *, name: Union[str, String], value: Union[str, String]) -> None:
        """
        Set a specified value string to the CSS.

        Parameters
        ----------
        name : str or String
            CSS name (e.g., 'display').
        value : str or String
            A CSS value string (e.g., 'none').

        References
        ----------
        - Display object get_css and set_css interfaces
            - https://simon-ritchie.github.io/apysc/en/display_object_get_and_set_css.html  # noqa
        """

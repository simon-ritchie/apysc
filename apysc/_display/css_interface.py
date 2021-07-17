"""Class implementation for the css interface.
"""

from typing import Any, Dict, Union

import apysc as ap
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class CssInterface(VariableNameInterface, RevertInterface):

    _css: Dict[str, ap.String]

    def _initialize_css_if_not_initialized(self) -> None:
        """
        Initialize the _css attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_css'):
            return
        self._css = {}

    def get_css(self, name: Union[str, ap.String]) -> ap.String:
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
        """
        self._initialize_css_if_not_initialized()
        if isinstance(name, ap.String):
            name_: str = name._value
        else:
            name_ = name
        if name_ in self._css:
            css: ap.String = self._css[name_]
        else:
            css = ap.String('')
        return css

    def _make_snapshot(self, snapshot_name: str) -> None:
        pass

    def _revert(self, snapshot_name: str) -> None:
        pass

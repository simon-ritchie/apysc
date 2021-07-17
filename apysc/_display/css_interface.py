"""Class implementation for the css interface.
"""

from typing import Dict, Union

import apysc as ap
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class CssInterface(VariableNameInterface, RevertInterface):

    _css: ap.Dictionary

    def _initialize_css_if_not_initialized(self) -> None:
        """
        Initialize the _css attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_css'):
            return
        self._css = ap.Dictionary({})

    def _make_snapshot(self, snapshot_name: str) -> None:
        pass

    def _revert(self, snapshot_name: str) -> None:
        pass

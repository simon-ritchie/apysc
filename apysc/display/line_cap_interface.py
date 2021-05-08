"""Class implementation for line cap interface.
"""

from typing import Dict
from typing import Union

from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface
from apysc.display.line_caps import LineCaps


class LineCapInterface(VariableNameInterface, RevertInterface):

    _line_cap: LineCaps

    def _initialize_line_cap_if_not_initialized(self) -> None:
        """
        Inilialize _line_cap attribute if that it is not
        initialized yet.
        """
        if hasattr(self, '_line_cap'):
            return
        self._line_cap = LineCaps.BUTT

    def line_cap(self) -> LineCaps:
        """
        Get this instance's line cap style setting.

        Parameters
        ----------
        is_test : bool/object/str/int/etc
            
        """
        pass

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        pass

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        pass

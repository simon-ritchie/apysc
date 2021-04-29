"""Class implementation for visible interface.
"""

from apysc import Boolean
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface


class VisibleInterface(VariableNameInterface, RevertInterface):

    _visible: Boolean

    def _initialize_visible_if_not_initialized(self) -> None:
        """
        Initialize _visible attribute if it is not initialized yet.
        """
        if hasattr(self, '_visible'):
            return
        self._visible = Boolean(True)

    def _make_snapshot(self, snapshot_name: str) -> None:
        pass

    def _revert(self, snapshot_name: str) -> None:
        pass

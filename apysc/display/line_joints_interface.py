"""Class implementation for line joints interface.
"""

from typing import Any
from typing import Dict
from typing import Union

from apysc import String
from apysc.display.line_joints import LineJoints
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface


class LineJointsInterface(VariableNameInterface, RevertInterface):

    _line_joints: String

    def _initialize_line_joints_if_not_initialized(self) -> None:
        """
        Initialize _line_joints attribute if that it is not
        initialized yet.
        """
        if hasattr(self, '_line_joints'):
            return
        self._line_joints = String(LineJoints.MITER.value)

    @property
    def line_joints(self) -> Any:
        """
        Get this instance's line joints style setting.

        Returns
        -------
        line_joints : String
            Line joints style setting.
        """
        self._initialize_line_joints_if_not_initialized()
        return self._line_joints._copy()

    def _make_snapshot(self, snapshot_name: str) -> None:
        pass

    def _revert(self, snapshot_name: str) -> None:
        pass

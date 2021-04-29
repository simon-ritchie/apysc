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

    @property
    def visible(self) -> Boolean:
        """
        Get a visibility of this instance.

        Returns
        -------
        result : Boolean
            If this instance is visible, True will be returned.
        """
        from apysc.type import value_util
        self._initialize_visible_if_not_initialized()
        return value_util.get_copy(value=self._visible)

    @visible.setter
    def visible(self, value: Boolean) -> None:
        """
        Update visibility of this instance.

        Parameters
        ----------
        value : Boolean
            Boolean value to set.
        """
        from apysc.validation import bool_validation
        bool_validation.validate_bool(value=value)
        if isinstance(value, bool):
            value = Boolean(value)
        self._visible = value

    def _make_snapshot(self, snapshot_name: str) -> None:
        pass

    def _revert(self, snapshot_name: str) -> None:
        pass

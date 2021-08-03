"""Class implementation for the ellipse height interface.
"""

from typing import Dict

import apysc as ap
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class EllipseHeightInterface(VariableNameInterface, RevertInterface):

    _ellipse_height: ap.Int

    def _initialize_ellipse_height_if_not_initialized(self) -> None:
        """
        Initialize _ellipse_height attribute it hasn't been initialized yet.
        """
        if hasattr(self, '_ellipse_height'):
            return
        self._ellipse_height = ap.Int(0)

    @property
    def ellipse_height(self) -> ap.Int:
        """
        Get ellipse height value.

        Returns
        -------
        ellipse_height : Int
            Ellipse height value.
        """
        with ap.DebugInfo(
                callable_='ellipse_height', locals_=locals(),
                module_name=__name__, class_=EllipseHeightInterface):
            from apysc._type import value_util
            self._initialize_ellipse_height_if_not_initialized()
            return value_util.get_copy(value=self._ellipse_height)

    @ellipse_height.setter
    def ellipse_height(self, value: ap.Int) -> None:
        """
        Update ellipse height value.

        Parameters
        ----------
        value : int or Int
            Ellipse height value.
        """
        with ap.DebugInfo(
                callable_='ellipse_height', locals_=locals(),
                module_name=__name__, class_=EllipseHeightInterface):
            from apysc._validation import number_validation
            number_validation.validate_integer(integer=value)
            if isinstance(value, int):
                value = ap.Int(value)
            self._ellipse_height = value
            self._ellipse_height.\
                _append_incremental_calc_substitution_expression()
            self._append_ellipse_height_update_expression()

    def _append_ellipse_height_update_expression(self) -> None:
        """
        Append ellipse height updating expression.
        """
        with ap.DebugInfo(
                callable_=self._append_ellipse_height_update_expression,
                locals_=locals(),
                module_name=__name__, class_=EllipseHeightInterface):
            from apysc._type import value_util
            self._initialize_ellipse_height_if_not_initialized()
            if hasattr(self, '_ellipse_width'):
                width_value_str: str = value_util.get_value_str_for_expression(
                    value=getattr(self, '_ellipse_width'))
            else:
                width_value_str = value_util.get_value_str_for_expression(
                    value=0)
            height_value_str: str = value_util.get_value_str_for_expression(
                value=self._ellipse_height)
            expression: str = (
                f'{self.variable_name}.radius({width_value_str}, '
                f'{height_value_str});'
            )
            ap.append_js_expression(expression=expression)

    _ellipse_height_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make the value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_ellipse_height_snapshots'):
            self._ellipse_height_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_ellipse_height_if_not_initialized()
        self._ellipse_height_snapshots[snapshot_name] = int(
            self._ellipse_height._value)

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert the value if the snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._ellipse_height._value = self._ellipse_height_snapshots[
            snapshot_name]

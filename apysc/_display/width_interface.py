"""Class implementation for witdth interface.
"""

from typing import Dict
from typing import Union

import apysc as ap
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class WidthInterface(VariableNameInterface, RevertInterface):

    _width: ap.Int

    def _initialize_width_if_not_initialized(self) -> None:
        """
        Initialize _width attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_width'):
            return
        self._width = ap.Int(0)

    @property
    def width(self) -> ap.Int:
        """
        Get this instance's width.

        Returns
        -------
        width : Int
            This instance's width.
        """
        with ap.DebugInfo(
                callable_='width', locals_=locals(),
                module_name=__name__, class_=WidthInterface):
            from apysc._type import value_util
            self._initialize_width_if_not_initialized()
            return value_util.get_copy(value=self._width)

    @width.setter
    def width(self, value: ap.Int) -> None:
        """
        Update this instance's width.

        Parameters
        ----------
        value : Int
            Width value to set.
        """
        with ap.DebugInfo(
                callable_='width', locals_=locals(),
                module_name=__name__, class_=WidthInterface):
            self._update_width_and_skip_appending_exp(value=value)
            self._width._append_incremental_calc_substitution_expression()
            self._append_width_update_expression()

    def _append_width_update_expression(self) -> None:
        """
        Append width updating expression.
        """
        with ap.DebugInfo(
                callable_=self._append_width_update_expression,
                locals_=locals(),
                module_name=__name__, class_=WidthInterface):
            expression: str = (
                f'{self.variable_name}.width({self.width});'
            )
            ap.append_js_expression(expression=expression)

    def _update_width_and_skip_appending_exp(
            self, value: Union[int, ap.Int]) -> None:
        """
        Update width value and skip appending expression to file.

        Parameters
        ----------
        value : int or Int
            Width value to set.
        """
        from apysc._converter import cast
        from apysc._validation import size_validation
        self._initialize_width_if_not_initialized()
        value = cast.to_int_from_float(int_or_float=value)
        size_validation.validate_size_is_int(size=value)
        size_validation.validate_size_is_gte_zero(size=value)
        if isinstance(value, int):
            value = ap.Int(value)
        self._width = value

    _width_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_width_snapshots'):
            self._width_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_width_if_not_initialized()
        self._width_snapshots[snapshot_name] = int(self._width._value)

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._width._value = self._width_snapshots[snapshot_name]

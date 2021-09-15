"""Class implementation for ellipse the width interface.
"""

from typing import Dict

import apysc as ap
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class EllipseWidthInterface(
        VariableNameInterface, RevertInterface, AttrLinkingInterface):

    _ellipse_width: ap.Int

    def _initialize_ellipse_width_if_not_initialized(self) -> None:
        """
        Initialize _ellipse_width attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_ellipse_width'):
            return
        self._ellipse_width = ap.Int(0)

        self._append_ellipse_width_attr_linking_setting()

    def _append_ellipse_width_attr_linking_setting(self) -> None:
        """
        Append a ellipse-height attribute linking setting.
        """
        with ap.DebugInfo(
                callable_=self._append_ellipse_width_attr_linking_setting,
                locals_=locals(),
                module_name=__name__, class_=EllipseWidthInterface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._ellipse_width, attr_name='ellipse_width')
            self._append_attr_to_linking_stack(
                attr=self._ellipse_width, attr_name='ellipse_width')

    @property
    def ellipse_width(self) -> ap.Int:
        """
        Get ellipse width value.

        Returns
        -------
        ellipse_width : Int
            Ellipse width value.
        """
        with ap.DebugInfo(
                callable_='ellipse_width', locals_=locals(),
                module_name=__name__, class_=EllipseWidthInterface):
            from apysc._type import value_util
            self._initialize_ellipse_width_if_not_initialized()
            return value_util.get_copy(value=self._ellipse_width)

    @ellipse_width.setter
    def ellipse_width(self, value: ap.Int) -> None:
        """
        Update ellipse width value.

        Parameters
        ----------
        value : int or Int
            Ellipse width value.
        """
        with ap.DebugInfo(
                callable_='ellipse_width', locals_=locals(),
                module_name=__name__, class_=EllipseWidthInterface):
            from apysc._validation import number_validation
            number_validation.validate_integer(integer=value)
            if isinstance(value, int):
                value = ap.Int(value)
            self._ellipse_width = value
            self._ellipse_width.\
                _append_incremental_calc_substitution_expression()
            self._append_ellipse_width_update_expression()

            self._append_ellipse_width_attr_linking_setting()

    def _append_ellipse_width_update_expression(self) -> None:
        """
        Append ellipse width updating expression.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_ellipse_width_update_expression,
                locals_=locals(),
                module_name=__name__, class_=EllipseWidthInterface):
            from apysc._type import value_util
            self._initialize_ellipse_width_if_not_initialized()
            width_value_str: str = value_util.get_value_str_for_expression(
                value=self._ellipse_width)
            if hasattr(self, '_ellipse_height'):
                height_value_str: str = value_util.\
                    get_value_str_for_expression(
                        value=getattr(self, '_ellipse_height'))
            else:
                height_value_str = value_util.get_value_str_for_expression(
                    value=0)
            expression: str = (
                f'{self.variable_name}.radius({width_value_str}, '
                f'{height_value_str});'
            )
            ap.append_js_expression(expression=expression)

    _ellipse_width_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make the value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_ellipse_width_snapshots'):
            self._ellipse_width_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_ellipse_width_if_not_initialized()
        self._ellipse_width_snapshots[snapshot_name] = int(
            self._ellipse_width._value)

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
        self._ellipse_width._value = self._ellipse_width_snapshots[
            snapshot_name]

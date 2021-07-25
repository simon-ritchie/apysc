"""Class implementation of the width and height Interfaces
for the ellipse.

Notes
-----
Subclass that inherit the normal WidthInterface and HeightInterface
can't use this interface.
"""

from typing import Dict

import apysc as ap
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class WidthAndHeightInterfacesForEllipse(
        VariableNameInterface, RevertInterface):

    _width: ap.Int
    _height: ap.Int

    def _initialize_width_and_height_if_not_initialized(self) -> None:
        """
        Initialize _width and _height attributes if these are not
        initialized yet.
        """
        if not hasattr(self, '_width'):
            self._width = ap.Int(0)
        if not hasattr(self, '_height'):
            self._height = ap.Int(0)

    @property
    def width(self) -> ap.Int:
        """
        Get a ellipse width value.

        Returns
        -------
        width : Int
            Ellipse width.
        """
        with ap.DebugInfo(
                callable_='width', locals_=locals(),
                module_name=__name__,
                class_=WidthAndHeightInterfacesForEllipse):
            from apysc._type import value_util
            self._initialize_width_and_height_if_not_initialized()
            return value_util.get_copy(value=self._width)

    @width.setter
    def width(self, value: ap.Int) -> None:
        """
        Update a ellipse width value.

        Parameters
        ----------
        value : int or Int
            Ellipse width value.
        """
        with ap.DebugInfo(
                callable_='width', locals_=locals(),
                module_name=__name__,
                class_=WidthAndHeightInterfacesForEllipse):
            from apysc._validation import number_validation
            if not isinstance(value, ap.Int):
                number_validation.validate_integer(integer=value)
                value = ap.Int(value)
            self._width = value
            self._width._append_incremental_calc_substitution_expression()
            self._append_ellipse_width_and_height_update_expression()

    @property
    def height(self) -> ap.Int:
        """
        Get a ellipse height value.

        Returns
        -------
        height : Int
            Ellipse height.
        """
        with ap.DebugInfo(
                callable_='height', locals_=locals(),
                module_name=__name__,
                class_=WidthAndHeightInterfacesForEllipse):
            from apysc._type import value_util
            self._initialize_width_and_height_if_not_initialized()
            return value_util.get_copy(value=self._height)

    @height.setter
    def height(self, value: ap.Int) -> None:
        """
        Update a ellipse height value.

        Parameters
        ----------
        value : int or Int
            Ellipse height value.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='height', locals_=locals(),
                module_name=__name__,
                class_=WidthAndHeightInterfacesForEllipse):
            from apysc._validation import number_validation
            if not isinstance(value, ap.Int):
                number_validation.validate_integer(integer=value)
                value = ap.Int(value)
            self._height = value
            self._height._append_incremental_calc_substitution_expression()
            self._append_ellipse_width_and_height_update_expression()

    def _append_ellipse_width_and_height_update_expression(self) -> None:
        """
        Append an ellipse width and height updating expression
        to the file.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_ellipse_width_and_height_update_expression,  # noqa
                locals_=locals(),
                module_name=__name__,
                class_=WidthAndHeightInterfacesForEllipse):
            from apysc._type import value_util
            self._initialize_width_and_height_if_not_initialized()
            width_value_str: str = value_util.get_value_str_for_expression(
                value=self._width)
            height_value_str: str = value_util.get_value_str_for_expression(
                value=self._height)
            expression: str = (
                f'{self.variable_name}.radius('
                f'parseInt({width_value_str} / 2), '
                f'parseInt({height_value_str}) / 2);'
            )
            ap.append_js_expression(expression=expression)

    _width_snapshots: Dict[str, int]
    _height_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make the values' snapshots.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_width_snapshots'):
            self._width_snapshots = {}
        if not hasattr(self, '_height_snapshots'):
            self._height_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_width_and_height_if_not_initialized()
        self._width_snapshots[snapshot_name] = int(self._width._value)
        self._height_snapshots[snapshot_name] = int(self._height._value)

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert the values if the snapshots exist.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._width._value = self._width_snapshots[snapshot_name]
        self._height._value = self._height_snapshots[snapshot_name]

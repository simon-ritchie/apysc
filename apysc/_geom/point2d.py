"""2-dimensional geometry point class implementation.
"""

from typing import Any
from typing import Dict
from typing import Union

import apysc as ap
from apysc._event.custom_event_interface import CustomEventInterface
from apysc._type.dictionary_structure import DictionaryStructure
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface

_int = Union[int, ap.Int]


class Point2D(
        VariableNameInterface, RevertInterface, DictionaryStructure,
        CustomEventInterface):
    """
    2-dimensional geometry point class.
    """

    _x: ap.Int
    _y: ap.Int

    def __init__(self, x: _int, y: _int) -> None:
        """
        2-dimensional geometry point.

        Parameters
        ----------
        x : int or Int
            X-coordinate.
        y : int or Int
            Y-coordinate.
        """
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=Point2D):
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            from apysc._validation.number_validation import validate_integer
            validate_integer(integer=x)
            validate_integer(integer=y)
            if isinstance(x, int):
                x = ap.Int(x)
            if isinstance(y, int):
                y = ap.Int(y)
            self._x = x
            self._y = y
            self.variable_name = \
                expression_variables_util.get_next_variable_name(
                    type_name=var_names.POINT2D)
            self._append_constructor_expression()

    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression to file.
        """
        with ap.DebugInfo(
                callable_=self._append_constructor_expression,
                locals_=locals(),
                module_name=__name__, class_=Point2D):
            expression: str = (
                f'var {self.variable_name} = {{'
                f'"x": {self._x.variable_name}, '
                f'"y": {self._y.variable_name}}};')
            ap.append_js_expression(expression=expression)

    @property
    def x(self) -> ap.Int:
        """
        X-coordinate property.

        Returns
        -------
        x : Int
            X-coordinate.
        """
        with ap.DebugInfo(
                callable_='x', locals_=locals(),
                module_name=__name__, class_=Point2D):
            x: ap.Int = ap.Int(self._x._value)
            self._append_x_getter_expression(x=x)
            return x

    @x.setter
    def x(self, value: ap.Int) -> None:
        """
        Update x-coordinate property.

        Parameters
        ----------
        value : Int
            X-coordinate to set.
        """
        with ap.DebugInfo(
                callable_='x', locals_=locals(),
                module_name=__name__, class_=Point2D):
            from apysc._validation.number_validation import validate_integer
            validate_integer(integer=value)
            if isinstance(value, int):
                value = ap.Int(value)
            self._x = value
            self._x._append_incremental_calc_substitution_expression()
            self._append_x_setter_expression(value=value)

    def _append_x_getter_expression(self, x: ap.Int) -> None:
        """
        Append x property getter expression to file.

        Parameters
        ----------
        x : Int
            Target x value.
        """
        with ap.DebugInfo(
                callable_=self._append_x_getter_expression, locals_=locals(),
                module_name=__name__, class_=Point2D):
            expression: str = (
                f'{x.variable_name} = '
                f'{self.variable_name}["x"];'
            )
            ap.append_js_expression(expression=expression)

    def _append_x_setter_expression(self, value: ap.Int) -> None:
        """
        Append x property setter expression to file.

        Parameters
        ----------
        value : Int
            X-coordinate to set.
        """
        with ap.DebugInfo(
                callable_=self._append_x_setter_expression, locals_=locals(),
                module_name=__name__, class_=Point2D):
            expression: str = (
                f'{self.variable_name}["x"] = {value.variable_name};'
            )
            ap.append_js_expression(expression=expression)

    @property
    def y(self) -> ap.Int:
        """
        Y-coordinate property.

        Returns
        -------
        y : Int
            Y-coordinate.
        """
        with ap.DebugInfo(
                callable_='y', locals_=locals(),
                module_name=__name__, class_=Point2D):
            y: ap.Int = ap.Int(self._y._value)
            self._append_y_getter_expression(y=y)
            return y

    @y.setter
    def y(self, value: ap.Int) -> None:
        """
        Update y-coordinate property.

        Parameters
        ----------
        value : Int
            Y-coordinate to set.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='y', locals_=locals(),
                module_name=__name__, class_=Point2D):
            from apysc._validation.number_validation import validate_integer
            validate_integer(integer=value)
            if isinstance(value, int):
                value = ap.Int(value)
            self._y = value
            self._y._append_incremental_calc_substitution_expression()
            self._append_y_setter_expression(value=value)

    def _append_y_getter_expression(self, y: ap.Int) -> None:
        """
        Append y property getter expression to file.

        Parameters
        ----------
        y : Int
            Target y value.
        """
        with ap.DebugInfo(
                callable_=self._append_y_getter_expression, locals_=locals(),
                module_name=__name__, class_=Point2D):
            expression: str = (
                f'{y.variable_name} = '
                f'{self.variable_name}["y"];'
            )
            ap.append_js_expression(expression=expression)

    def _append_y_setter_expression(self, value: ap.Int) -> None:
        """
        Append y property setter expression to file.

        Parameters
        ----------
        value : Int
            Y-coordinate to set.
        """
        with ap.DebugInfo(
                callable_=self._append_y_setter_expression,
                locals_=locals(),
                module_name=__name__, class_=Point2D):
            expression: str = (
                f'{self.variable_name}["y"] = {value.variable_name};'
            )
            ap.append_js_expression(expression=expression)

    def __eq__(self, other: Any) -> Any:
        """
        Equal comparison method.

        Parameters
        ----------
        other : Any
            Other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        with ap.DebugInfo(
                callable_='__eq__', locals_=locals(),
                module_name=__name__, class_=Point2D):
            result: ap.Boolean
            if not isinstance(other, Point2D):
                result = ap.Boolean(False)
                return result
            if other.x == self.x and other.y == self.y:
                result = ap.Boolean(True)
                return result
            result = ap.Boolean(False)
            return result

    def __ne__(self, other: Any) -> Any:
        """
        Not equal comparison method.

        Parameters
        ----------
        other : Any
            Other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        with ap.DebugInfo(
                callable_='__ne__', locals_=locals(),
                module_name=__name__, class_=Point2D):
            result: ap.Boolean = self == other
            result = result.not_
            return result

    _x_snapshots: Dict[str, int]
    _y_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make values' snapshots.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_x_snapshots'):
            self._x_snapshots = {}
        if not hasattr(self, '_y_snapshots'):
            self._y_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._x_snapshots[snapshot_name] = int(self._x._value)
        self._y_snapshots[snapshot_name] = int(self._y._value)

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert values if snapshots exist.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._x._value = self._x_snapshots[snapshot_name]
        self._y._value = self._y_snapshots[snapshot_name]

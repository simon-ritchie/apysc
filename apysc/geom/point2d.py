"""2-dimensional geometry point class implementation.
"""

from typing import Any, Union
from apysc import Int, Boolean
from apysc.type.variable_name_interface import VariableNameInterface

_int = Union[int, Int]


class Point2D(VariableNameInterface):

    _x: Int
    _y: Int

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
        from apysc.validation.number_validation import validate_integer
        from apysc.expression import var_names
        from apysc.expression import expression_variables_util
        validate_integer(integer=x)
        validate_integer(integer=y)
        if isinstance(x, int):
            x = Int(x)
        if isinstance(y, int):
            y = Int(y)
        self._x = x
        self._y = y
        self.variable_name = expression_variables_util.get_next_variable_name(
            type_name=var_names.POINT2D)
        self._append_constructor_expression()

    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression to file.
        """
        from apysc.expression import expression_file_util
        expression: str = (
            f'var {self.variable_name} = {{'
            f'"x": {self._x.variable_name}, "y": {self._y.variable_name}}};'
        )
        expression_file_util.append_js_expression(expression=expression)

    @property
    def x(self) -> Int:
        """
        X-coordinate property.

        Returns
        -------
        x : Int
            X-coordinate.
        """
        x: Int = Int(self._x._value)
        self._append_x_getter_expression(x=x)
        return x

    def _append_x_getter_expression(self, x: Int) -> None:
        """
        Append x property getter expression to file.

        Parameters
        ----------
        x : Int
            Target x value.
        """
        from apysc.expression import expression_file_util
        expression: str = (
            f'{x.variable_name} = '
            f'{self.variable_name}["x"];'
        )
        expression_file_util.append_js_expression(expression=expression)

    @x.setter
    def x(self, value: Any) -> None:
        """
        Update x-coordinate property.

        Parameters
        ----------
        value : int or Int
            X-coordinate to set.
        """
        from apysc.validation.number_validation import validate_integer
        validate_integer(integer=value)
        if isinstance(value, int):
            value = Int(value)
        self._x = value

    @property
    def y(self) -> Int:
        """
        Y-coordinate property.

        Parameters
        ----------
        y : Int
            Y-coordinate.
        """
        y: Int = Int(self._y._value)
        self._append_y_getter_expression(y=y)
        return y

    def _append_y_getter_expression(self, y: Int) -> None:
        """
        Append y property getter expression to file.

        Parameters
        ----------
        y : Int
            Target y value.
        """
        from apysc.expression import expression_file_util
        expression: str = (
            f'{y.variable_name} = '
            f'{self.variable_name}["y"];'
        )
        expression_file_util.append_js_expression(expression=expression)

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
        result: Boolean
        if not isinstance(other, Point2D):
            result = Boolean(False)
            return result
        if other.x == self.x and other.y == self.y:
            result = Boolean(True)
            return result
        result = Boolean(False)
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
        result: Boolean = self == other
        result = result.not_
        return result

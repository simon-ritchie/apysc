"""Class implementation for the rotation_around_point interface.
"""

from typing import Union

import apysc as ap
from apysc._type.variable_name_interface import VariableNameInterface


class RotationAroundPointInterface(VariableNameInterface):

    _rotation_around_point: ap.Dictionary[str, ap.Int]

    def _initialize_rotation_around_point_if_not_initialized(self) -> None:
        """
        Initialize the `_rotation_around_point` attribute if it hasn't
        been initialized yet.
        """
        if hasattr(self, '_rotation_around_point'):
            return
        self._rotation_around_point = ap.Dictionary({})

    def get_rotation_around_point(self, x: ap.Int, y: ap.Int) -> ap.Int:
        """
        Get a rotation value around the given coordinates.

        Parameters
        ----------
        x : Int
            X-coordinate.
        y : Int
            Y-coordinate.

        Returns
        -------
        rotation : Int
            Rotation value around the given coordinates.
        """
        with ap.DebugInfo(
                callable_=self.get_rotation_around_point, locals_=locals(),
                module_name=__name__, class_=RotationAroundPointInterface):
            from apysc._display import rotation_interface_helper
            from apysc._validation import number_validation
            from apysc._type.expression_string import ExpressionString
            number_validation.validate_integer(integer=x)
            number_validation.validate_integer(integer=y)
            self._initialize_rotation_around_point_if_not_initialized()
            default_val: ap.Int = ap.Int(0)
            key_exp_str: ExpressionString = rotation_interface_helper.\
                get_coordinates_key_for_expression(
                    x=int(x._value), y=int(y._value))
            rotation: ap.Int = self._rotation_around_point.get(
                key=key_exp_str, default=default_val)
            return rotation

    def set_rotation_around_point(
            self, rotation: ap.Int, x: ap.Int, y: ap.Int) -> None:
        """
        Update a rotation value around the given coordinates.

        Parameters
        ----------
        rotation : Int
            Rotation value to set.
        x : Int
            X-coordinate.
        y : Int
            Y-coordinate.
        """
        with ap.DebugInfo(
                callable_=self.set_rotation_around_point, locals_=locals(),
                module_name=__name__, class_=RotationAroundPointInterface):
            from apysc._display import rotation_interface_helper
            from apysc._validation import number_validation
            from apysc._type.expression_string import ExpressionString
            number_validation.validate_integer(integer=rotation)
            number_validation.validate_integer(integer=x)
            number_validation.validate_integer(integer=y)
            self._initialize_rotation_around_point_if_not_initialized()
            key_exp_str: ExpressionString = rotation_interface_helper.\
                get_coordinates_key_for_expression(
                    x=int(x._value), y=int(y._value))
            self._rotation_around_point._value[key_exp_str.value] = rotation

    def rotate_around_point(
            self, additional_rotation: Union[int, ap.Int],
            x: Union[int, ap.Int], y: Union[int, ap.Int]) -> None:
        """
        Add a rotation value around the specified point.

        Notes
        -----
        - This interface value is a relative value, not a absolute value,
            so if you call this value multiple times, total rotation will
            be cumulative.
        - This interface is not supported by the container instance, such
            as the `Sprite` class due to the HTML (SVG) specification.

        Parameters
        ----------
        additional_rotation : int or Int
            A value to add.
        x : int or Int
            Rotation point of a x-coordinate.
        y : int or Int
            Rotation point of a y-coordinate.

        References
        ----------
        - GraphicsBase rotate_around_point interface document
            - https://bit.ly/3z4Z4zg
        """
        with ap.DebugInfo(
                callable_=self.rotate_around_point, locals_=locals(),
                module_name=__name__, class_=RotationAroundPointInterface):
            from apysc._type import value_util
            from apysc._validation import number_validation
            number_validation.validate_integer(integer=additional_rotation)
            number_validation.validate_integer(integer=x)
            number_validation.validate_integer(integer=y)
            rotation_value_str: str = value_util.get_value_str_for_expression(
                value=additional_rotation)
            x_value_str: str = value_util.get_value_str_for_expression(value=x)
            y_value_str: str = value_util.get_value_str_for_expression(value=y)
            expression: str = (
                f'{self.variable_name}.rotate('
                f'{rotation_value_str}, {x_value_str}, {y_value_str});'
            )
            ap.append_js_expression(expression=expression)

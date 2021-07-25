"""Class implementation for the rotate_around_center interface.
"""

from typing import Union

import apysc as ap
from apysc._type.variable_name_interface import VariableNameInterface


class RotateAroundPointInterface(VariableNameInterface):

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
                module_name=__name__, class_=RotateAroundPointInterface):
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

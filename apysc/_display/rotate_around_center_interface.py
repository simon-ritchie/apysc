"""Class implementation for the rotate_around_center interface.
"""

from typing import Union

import apysc as ap
from apysc._type.variable_name_interface import VariableNameInterface


class RotateAroundCenterInterface(VariableNameInterface):

    def rotate_around_center(
            self, additional_rotation: Union[int, ap.Int]) -> None:
        """
        Add a rotation value around the center of this instance.

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

        References
        ----------
        - GraphicsBase rotate_around_center interface document
            - https://bit.ly/3hP6d12
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.rotate_around_center, locals_=locals(),
                module_name=__name__, class_=RotateAroundCenterInterface):
            from apysc._type import value_util
            from apysc._validation import number_validation
            number_validation.validate_integer(
                integer=additional_rotation)
            value_str: str = value_util.get_value_str_for_expression(
                value=additional_rotation)
            expression: str = (
                f'{self.variable_name}.rotate({value_str});'
            )
            ap.append_js_expression(expression=expression)

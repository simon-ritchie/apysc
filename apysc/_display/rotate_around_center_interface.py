"""Class implementation for the rotate_around_center interface.
"""

from typing import Dict, Union

from apysc import Int
from apysc._type.variable_name_interface import VariableNameInterface


class RotateAroundCenterInterface(VariableNameInterface):

    @property
    def rotate_around_center(self) -> Union[int, Int]:
        """
        Rotation around the center of this instance setting.

        Raises
        ------
        ValueError
            This getter interface will always raise an exception.

        Returns
        -------
        rotate_around_center : int or Int
            Getter interface will always raise an exception
            so this value will never be returned.
        """
        raise ValueError('This getter interface is not supported.')

    @rotate_around_center.setter
    def rotate_around_center(self, value: Union[int, Int]) -> None:
        """
        Add a rotation value around the center of this instance.

        Notes
        -----
        This property is a relative value, not a absolute value,
        so if you set this value multiple times, total rotation will
        be cumulative.

        Parameters
        ----------
        value : int or Int
            The value to set.
        """
        from apysc._validation import number_validation
        from apysc import append_js_expression
        from apysc._type import value_util
        number_validation.validate_integer(integer=value)
        value_str: str = value_util.get_value_str_for_expression(value=value)
        expression: str = (
            f'{self.variable_name}.rotate({value_str});'
        )
        append_js_expression(expression=expression)

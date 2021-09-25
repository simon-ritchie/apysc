"""Implementations of Circle class.
"""

from typing import Union

import apysc as ap
from apysc._display.cx_interface import CxInterface
from apysc._display.cy_interface import CyInterface
from apysc._display.line_base import LineBase
from apysc._display.radius_interface import RadiusInterface


class Circle(  # type: ignore
        CxInterface, CyInterface, LineBase, RadiusInterface):
    """
    The circle vector graphics class.

    References
    ----------
    - Graphics draw_circle interface document
        - https://bit.ly/36Sgmn3
    """

    def __init__(
            self,
            parent: 'ap.Graphics',
            x: Union[int, ap.Int],
            y: Union[int, ap.Int],
            radius: Union[int, ap.Int]) -> None:
        """
        Create a circle vector graphics.

        Parameters
        ----------
        parent : Graphics
            Graphics instance to link this graphics.
        x : int or Int
            X-coordinate of the circle center.
        y : int or Int
            Y-coordinate of the circle center.
        radius : int or Int
            Circle radius.

        References
        ----------
        - Graphics draw_circle interface document
            - https://bit.ly/36Sgmn3
        """
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=Circle):
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            from apysc._validation import size_validation
            variable_name: str = expression_variables_util.\
                get_next_variable_name(type_name=var_names.CIRCLE)
            super(Circle, self).__init__(
                parent=parent, x=0, y=0, variable_name=variable_name)
            size_validation.validate_size_is_gt_zero(size=radius)
            self._radius = self._get_converted_radius_int(radius=radius)
            self._set_initial_basic_values(parent=parent)
            self._append_constructor_expression()
            self._set_center_coordinates(x=x, y=y)
            self._set_line_setting_if_not_none_value_exists(
                parent_graphics=parent)
            self._set_overflow_visible_setting()

            self._append_applying_new_attr_val_exp(
                new_attr=self._radius, attr_name='radius')
            self._append_attr_to_linking_stack(
                attr=self._radius, attr_name='radius')

    def _set_center_coordinates(
            self,
            x: Union[int, ap.Int],
            y: Union[int, ap.Int]) -> None:
        """
        Set a center x-coordinate and a center y-coordinate.

        Parameters
        ----------
        x : int or Int
            X-coordinate of the circle center.
        y : int or Int
            Y-coordinate of the circle center.
        """
        with ap.DebugInfo(
                callable_=self._set_center_coordinates, locals_=locals(),
                module_name=__name__, class_=Circle):
            from apysc._converter.to_apysc_val_from_builtin import \
                get_copied_int_from_builtin_val
            self.x = get_copied_int_from_builtin_val(integer=x)
            self.y = get_copied_int_from_builtin_val(integer=y)

    def _append_constructor_expression(self) -> None:
        """
        Append a construcor expression.
        """
        with ap.DebugInfo(
                callable_=self._append_constructor_expression,
                locals_=locals(),
                module_name=__name__, class_=Circle):
            from apysc._display.stage import get_stage_variable_name
            from apysc._type import value_util
            stage_variable_name: str = get_stage_variable_name()
            radius_str: str = value_util.get_value_str_for_expression(
                value=self._radius)
            expression: str = (
                f'var {self.variable_name} = {stage_variable_name}'
                f'\n  .circle({radius_str} * 2)'
                '\n  .attr({'
            )
            expression = self._append_basic_vals_expression(
                expression=expression, indent_num=2)
            expression += '\n  });'
            ap.append_js_expression(expression=expression)

    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of
        debugging).

        Returns
        -------
        repr_str : str
            Type name and variable name will be set
            (e.g., `Circle('<variable_name>')`).
        """
        repr_str: str = f"Circle('{self.variable_name}')"
        return repr_str

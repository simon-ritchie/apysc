"""Implementation of the Ellipse class.
"""

from typing import Union

from apysc._display import graphics
from apysc._display.cx_interface import CxInterface
from apysc._display.cy_interface import CyInterface
from apysc._display.line_base import LineBase
from apysc._display.width_and_height_interfaces_for_ellipse import \
    WidthAndHeightInterfacesForEllipse
from apysc._type.int import Int


class Ellipse(  # type: ignore
        CxInterface, CyInterface, LineBase,
        WidthAndHeightInterfacesForEllipse):
    """
    The ellipse vector graphics class.

    References
    ----------
    - Graphics draw_ellipse interface
        - https://bit.ly/3xPVicP

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.begin_fill(color='#0af')
    >>> ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
    ...     x=100, y=100, width=80, height=50)
    >>> ellipse.x
    Int(100)

    >>> ellipse.y
    Int(100)

    >>> ellipse.width
    Int(80)

    >>> ellipse.height
    Int(50)

    >>> ellipse.fill_color
    String('#00aaff')
    """

    def __init__(
            self,
            *,
            parent: 'graphics.Graphics',
            x: Union[int, Int],
            y: Union[int, Int],
            width: Union[int, Int],
            height: Union[int, Int]) -> None:
        """
        Create a ellipse vector graphics.

        Parameters
        ----------
        parent : Graphics
            Graphics instance to link this graphics.
        x : int or Int
            X-coordinate of the ellipse center.
        y : int or Int
            Y-coordinate of the ellipse center.
        width : int or Int
            Ellipse width.
        height : int or Int
            Ellipse height.

        References
        ----------
        - Graphics draw_ellipse interface
            - https://bit.ly/3xPVicP

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
        ...     x=100, y=100, width=80, height=50)
        >>> ellipse.x
        Int(100)

        >>> ellipse.y
        Int(100)

        >>> ellipse.width
        Int(80)

        >>> ellipse.height
        Int(50)

        >>> ellipse.fill_color
        String('#00aaff')
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=Ellipse):
            from apysc._converter.to_apysc_val_from_builtin import \
                get_copied_int_from_builtin_val
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            from apysc._validation import size_validation
            variable_name: str = expression_variables_util.\
                get_next_variable_name(type_name=var_names.ELLIPSE)
            super(Ellipse, self).__init__(
                parent=parent, x=0, y=0, variable_name=variable_name)
            size_validation.validate_size_is_gt_zero(size=width)
            size_validation.validate_size_is_gt_zero(size=height)
            self._width = get_copied_int_from_builtin_val(integer=width)
            self._height = get_copied_int_from_builtin_val(integer=height)
            self._set_initial_basic_values(parent=parent)
            self._append_constructor_expression()
            self.x = get_copied_int_from_builtin_val(integer=x)
            self.y = get_copied_int_from_builtin_val(integer=y)
            self._set_line_setting_if_not_none_value_exists(
                parent_graphics=parent)
            self._set_overflow_visible_setting()

            self._append_width_attr_linking_setting()
            self._append_height_attr_linking_setting()

    def _append_constructor_expression(self) -> None:
        """
        Append a constructor expression.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_constructor_expression,
                locals_=locals(),
                module_name=__name__, class_=Ellipse):
            from apysc._display.stage import get_stage_variable_name
            from apysc._type import value_util
            stage_variable_name: str = get_stage_variable_name()
            width_str: str = value_util.get_value_str_for_expression(
                value=self._width)
            height_str: str = value_util.get_value_str_for_expression(
                value=self._height)
            expression: str = (
                f'var {self.variable_name} = {stage_variable_name}'
                f'\n  .ellipse({width_str}, {height_str})'
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
            (e.g., `Ellipse('<variable_name>')`).
        """
        repr_str: str = f"Ellipse('{self.variable_name}')"
        return repr_str

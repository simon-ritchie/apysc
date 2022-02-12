"""Implementations of Circle class.
"""

from typing import Union

from apysc._display import graphics
from apysc._display.cx_interface import CxInterface
from apysc._display.cy_interface import CyInterface
from apysc._display.line_base import LineBase
from apysc._display.radius_interface import RadiusInterface
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int


class Circle(  # type: ignore
        CxInterface, CyInterface, LineBase, RadiusInterface):
    """
    The circle vector graphics class.

    References
    ----------
    - Graphics draw_circle interface document
        - https://simon-ritchie.github.io/apysc/graphics_draw_circle.html  # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.begin_fill(color='#0af')
    >>> circle: ap.Circle = sprite.graphics.draw_circle(
    ...     x=100, y=100, radius=50)
    >>> circle.x
    Int(100)

    >>> circle.y
    Int(100)

    >>> circle.radius
    Int(50)

    >>> circle.fill_color
    String('#00aaff')
    """

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='Circle')
    def __init__(
            self,
            *,
            parent: 'graphics.Graphics',
            x: Union[int, Int],
            y: Union[int, Int],
            radius: Union[int, Int]) -> None:
        """
        Create a circle vector graphic.

        Parameters
        ----------
        parent : Graphics
            Graphics instance to link this graphic.
        x : Int or int
            X-coordinate of the circle center.
        y : Int or int
            Y-coordinate of the circle center.
        radius : Int or int
            Circle radius.

        References
        ----------
        - Graphics draw_circle interface document
            - https://simon-ritchie.github.io/apysc/graphics_draw_circle.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> circle: ap.Circle = sprite.graphics.draw_circle(
        ...     x=100, y=100, radius=50)
        >>> circle.x
        Int(100)

        >>> circle.y
        Int(100)

        >>> circle.radius
        Int(50)

        >>> circle.fill_color
        String('#00aaff')
        """
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

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='Circle')
    def _set_center_coordinates(
            self,
            *,
            x: Union[int, Int],
            y: Union[int, Int]) -> None:
        """
        Set a center x-coordinate and a center y-coordinate.

        Parameters
        ----------
        x : Int or int
            X-coordinate of the circle center.
        y : Int or int
            Y-coordinate of the circle center.
        """
        from apysc._converter.to_apysc_val_from_builtin import \
            get_copied_int_from_builtin_val
        self.x = get_copied_int_from_builtin_val(integer=x)
        self.y = get_copied_int_from_builtin_val(integer=y)

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='Circle')
    def _append_constructor_expression(self) -> None:
        """
        Append a constructor expression.
        """
        import apysc as ap
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

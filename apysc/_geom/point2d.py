"""2-dimensional geometry point class implementation.
"""

from typing import Any
from typing import Dict
from typing import Union

from apysc._event.custom_event_interface import CustomEventInterface
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.dictionary_structure import DictionaryStructure
from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface
from apysc._validation import arg_validation_decos

_Int = Union[int, Int]


class Point2D(
        VariableNameInterface, RevertInterface, DictionaryStructure,
        CustomEventInterface):
    """
    2-dimensional geometry point class.

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.begin_fill(color='#0af')
    >>> point_1: ap.Point2D = ap.Point2D(x=0, y=0)
    >>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
    ...     points=[
    ...         point_1,
    ...         ap.Point2D(x=0, y=50),
    ...         ap.Point2D(x=50, y=25),
    ...     ])

    >>> point_1.x
    Int(0)

    >>> point_1.y
    Int(0)
    """

    _x: Int
    _y: Int

    @arg_validation_decos.is_integer(arg_position_index=1)
    @arg_validation_decos.is_integer(arg_position_index=2)
    @add_debug_info_setting(
        module_name=__name__, class_name='Point2D')
    def __init__(self, x: _Int, y: _Int) -> None:
        """
        2-dimensional geometry point.

        Parameters
        ----------
        x : int or Int
            X-coordinate.
        y : int or Int
            Y-coordinate.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
        ...     points=[
        ...         ap.Point2D(x=0, y=0),
        ...         ap.Point2D(x=0, y=50),
        ...         ap.Point2D(x=50, y=25),
        ...     ])
        """
        import apysc as ap
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        if isinstance(x, ap.Int):
            x_: ap.Int = x
        else:
            x_ = ap.Int(x)
        if isinstance(y, ap.Int):
            y_: ap.Int = y
        else:
            y_ = ap.Int(y)
        self._x = x_
        self._y = y_
        self.variable_name = \
            expression_variables_util.get_next_variable_name(
                type_name=var_names.POINT2D)
        self._append_constructor_expression()

    @add_debug_info_setting(
        module_name=__name__, class_name='Point2D')
    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression.
        """
        import apysc as ap
        expression: str = (
            f'var {self.variable_name} = {{'
            f'"x": {self._x.variable_name}, '
            f'"y": {self._y.variable_name}}};')
        ap.append_js_expression(expression=expression)

    @property
    @add_debug_info_setting(
        module_name=__name__, class_name='Point2D')
    def x(self) -> Int:
        """
        X-coordinate property.

        Returns
        -------
        x : Int
            X-coordinate.

        Examples
        --------
        >>> import apysc as ap
        >>> point: ap.Point2D = ap.Point2D(x=50, y=100)
        >>> point.x = ap.Int(150)
        >>> point.x
        Int(150)
        """
        import apysc as ap
        x: ap.Int = ap.Int(self._x._value)
        self._append_x_getter_expression(x=x)
        return x

    @x.setter
    @arg_validation_decos.is_num(arg_position_index=1)
    @add_debug_info_setting(
        module_name=__name__, class_name='Point2D')
    def x(self, value: Int) -> None:
        """
        Update x-coordinate property.

        Parameters
        ----------
        value : Int
            X-coordinate to set.
        """
        import apysc as ap
        if not isinstance(value, ap.Int):
            value = ap.Int(value)
        self._x = value
        self._x._append_incremental_calc_substitution_expression()
        self._append_x_setter_expression(value=value)

    @add_debug_info_setting(
        module_name=__name__, class_name='Point2D')
    def _append_x_getter_expression(self, *, x: Int) -> None:
        """
        Append x property getter expression.

        Parameters
        ----------
        x : Int
            Target x value.
        """
        import apysc as ap
        expression: str = (
            f'{x.variable_name} = '
            f'{self.variable_name}["x"];'
        )
        ap.append_js_expression(expression=expression)

    @add_debug_info_setting(
        module_name=__name__, class_name='Point2D')
    def _append_x_setter_expression(self, *, value: Int) -> None:
        """
        Append x property setter expression.

        Parameters
        ----------
        value : Int
            X-coordinate to set.
        """
        import apysc as ap
        expression: str = (
            f'{self.variable_name}["x"] = {value.variable_name};'
        )
        ap.append_js_expression(expression=expression)

    @property
    @add_debug_info_setting(
        module_name=__name__, class_name='Point2D')
    def y(self) -> Int:
        """
        Y-coordinate property.

        Returns
        -------
        y : Int
            Y-coordinate.

        Examples
        --------
        >>> import apysc as ap
        >>> point: ap.Point2D = ap.Point2D(x=50, y=100)
        >>> point.y = ap.Int(150)
        >>> point.y
        Int(150)
        """
        import apysc as ap
        y: ap.Int = ap.Int(self._y._value)
        self._append_y_getter_expression(y=y)
        return y

    @y.setter
    @arg_validation_decos.is_num(arg_position_index=1)
    @add_debug_info_setting(
        module_name=__name__, class_name='Point2D')
    def y(self, value: Int) -> None:
        """
        Update y-coordinate property.

        Parameters
        ----------
        value : Int
            Y-coordinate to set.
        """
        import apysc as ap
        if not isinstance(value, ap.Int):
            value = ap.Int(value)
        self._y = value
        self._y._append_incremental_calc_substitution_expression()
        self._append_y_setter_expression(value=value)

    @add_debug_info_setting(
        module_name=__name__, class_name='Point2D')
    def _append_y_getter_expression(self, *, y: Int) -> None:
        """
        Append y property getter expression.

        Parameters
        ----------
        y : Int
            Target y value.
        """
        import apysc as ap
        expression: str = (
            f'{y.variable_name} = '
            f'{self.variable_name}["y"];'
        )
        ap.append_js_expression(expression=expression)

    @add_debug_info_setting(
        module_name=__name__, class_name='Point2D')
    def _append_y_setter_expression(self, *, value: Int) -> None:
        """
        Append y property setter expression.

        Parameters
        ----------
        value : Int
            Y-coordinate to set.
        """
        import apysc as ap
        expression: str = (
            f'{self.variable_name}["y"] = {value.variable_name};'
        )
        ap.append_js_expression(expression=expression)

    @add_debug_info_setting(
        module_name=__name__, class_name='Point2D')
    def __eq__(self, other: Any) -> Any:
        """
        Equal comparison method.

        Parameters
        ----------
        other : Any
            The other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        import apysc as ap
        result: ap.Boolean
        if not isinstance(other, Point2D):
            result = ap.Boolean(False)
            return result
        return other.x == self.x and other.y == self.y

    @add_debug_info_setting(
        module_name=__name__, class_name='Point2D')
    def __ne__(self, other: Any) -> Any:
        """
        Not equal comparison method.

        Parameters
        ----------
        other : Any
            The other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        import apysc as ap
        result: ap.Boolean = self == other
        result = result.not_
        return result

    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the
        sake of debugging).

        Returns
        -------
        repr_str : str
            Type name and coordinates values are set
            (e.g., `Point2D(Int(50), Int(100))`).
        """
        x_repr: str = repr(self._x)
        y_repr: str = repr(self._y)
        repr_str: str = f'Point2D({x_repr}, {y_repr})'
        return repr_str

    _x_snapshots: Dict[str, int]
    _y_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make values' snapshots.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._set_single_snapshot_val_to_dict(
            dict_name='_x_snapshots',
            value=int(self._x._value), snapshot_name=snapshot_name)
        self._set_single_snapshot_val_to_dict(
            dict_name='_y_snapshots',
            value=int(self._y._value), snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
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

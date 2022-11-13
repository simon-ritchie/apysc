"""2-dimensional geometry point class implementation.
"""

from typing import Any
from typing import Dict
from typing import Union

from typing_extensions import final

from apysc._event.custom_event_mixin import CustomEventMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_to_apysc_val_from_builtin_mixin import (
    AttrToApyscValFromBuiltinMixIn,
)
from apysc._type.dictionary_structure import DictionaryStructure
from apysc._type.int import Int
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos

_Int = Union[int, Int]


class Point2D(
    VariableNameSuffixAttrMixIn,
    VariableNameMixIn,
    RevertMixIn,
    DictionaryStructure,
    CustomEventMixIn,
    VariableNameSuffixMixIn,
    AttrToApyscValFromBuiltinMixIn,
):
    """
    2-dimensional geometry point class.

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.begin_fill(color="#0af")
    >>> point_1: ap.Point2D = ap.Point2D(x=0, y=0)
    >>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
    ...     points=[
    ...         point_1,
    ...         ap.Point2D(x=0, y=50),
    ...         ap.Point2D(x=50, y=25),
    ...     ]
    ... )

    >>> point_1.x
    Int(0)

    >>> point_1.y
    Int(0)
    """

    _x: Int
    _y: Int

    @final
    @arg_validation_decos.is_integer(arg_position_index=1)
    @arg_validation_decos.is_integer(arg_position_index=2)
    @arg_validation_decos.is_builtin_string(arg_position_index=3, optional=True)
    @add_debug_info_setting(module_name=__name__)
    def __init__(self, x: _Int, y: _Int, *, variable_name_suffix: str = "") -> None:
        """
        2-dimensional geometry point.

        Parameters
        ----------
        x : int or Int
            X-coordinate.
        y : int or Int
            Y-coordinate.
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript's debugging.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
        ...     points=[
        ...         ap.Point2D(x=0, y=0),
        ...         ap.Point2D(x=0, y=50),
        ...         ap.Point2D(x=50, y=25),
        ...     ]
        ... )
        """
        import apysc as ap
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        self._variable_name_suffix = variable_name_suffix
        if isinstance(x, ap.Int):
            x_: ap.Int = x
        else:
            suffix: str = self._get_attr_variable_name_suffix(attr_identifier="x")
            x_ = ap.Int(x, variable_name_suffix=suffix)
        if isinstance(y, ap.Int):
            y_: ap.Int = y
        else:
            suffix = self._get_attr_variable_name_suffix(attr_identifier="y")
            y_ = ap.Int(y, variable_name_suffix=suffix)
        self._x = x_
        self._y = y_
        self.variable_name = expression_variables_util.get_next_variable_name(
            type_name=var_names.POINT2D
        )
        self._append_constructor_expression()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression.
        """
        import apysc as ap

        expression: str = (
            f"var {self.variable_name} = {{"
            f'"x": {self._x.variable_name}, '
            f'"y": {self._y.variable_name}}};'
        )
        ap.append_js_expression(expression=expression)

    @property
    @add_debug_info_setting(module_name=__name__)
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

        suffix: str = self._get_attr_variable_name_suffix(attr_identifier="x")
        x: ap.Int = ap.Int(self._x._value, variable_name_suffix=suffix)
        self._append_x_getter_expression(x=x)
        return x

    @x.setter
    @arg_validation_decos.is_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
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
            suffix: str = self._get_attr_variable_name_suffix(attr_identifier="x")
            value = ap.Int(value, variable_name_suffix=suffix)
        self._x = value
        self._x._append_incremental_calc_substitution_expression()
        self._append_x_setter_expression(value=value)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_x_getter_expression(self, *, x: Int) -> None:
        """
        Append x property getter expression.

        Parameters
        ----------
        x : Int
            Target x value.
        """
        import apysc as ap

        expression: str = f"{x.variable_name} = " f'{self.variable_name}["x"];'
        ap.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_x_setter_expression(self, *, value: Int) -> None:
        """
        Append x property setter expression.

        Parameters
        ----------
        value : Int
            X-coordinate to set.
        """
        import apysc as ap

        expression: str = f'{self.variable_name}["x"] = {value.variable_name};'
        ap.append_js_expression(expression=expression)

    @property
    @add_debug_info_setting(module_name=__name__)
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

        suffix: str = self._get_attr_variable_name_suffix(attr_identifier="y")
        y: ap.Int = ap.Int(self._y._value, variable_name_suffix=suffix)
        self._append_y_getter_expression(y=y)
        return y

    @y.setter
    @arg_validation_decos.is_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
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
            suffix: str = self._get_attr_variable_name_suffix(attr_identifier="y")
            value = ap.Int(value, variable_name_suffix=suffix)
        self._y = value
        self._y._append_incremental_calc_substitution_expression()
        self._append_y_setter_expression(value=value)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_y_getter_expression(self, *, y: Int) -> None:
        """
        Append y property getter expression.

        Parameters
        ----------
        y : Int
            Target y value.
        """
        import apysc as ap

        expression: str = f"{y.variable_name} = " f'{self.variable_name}["y"];'
        ap.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_y_setter_expression(self, *, value: Int) -> None:
        """
        Append y property setter expression.

        Parameters
        ----------
        value : Int
            Y-coordinate to set.
        """
        import apysc as ap

        expression: str = f'{self.variable_name}["y"] = {value.variable_name};'
        ap.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
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
            result = ap.Boolean(False, variable_name_suffix=self._variable_name_suffix)
            return result
        return other.x == self.x and other.y == self.y

    @final
    @add_debug_info_setting(module_name=__name__)
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

    @final
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
        x_repr: str = "0"
        if hasattr(self, "_x"):
            x_repr = repr(self._x)
        y_repr: str = "0"
        if hasattr(self, "_y"):
            y_repr = repr(self._y)
        repr_str: str = f"Point2D({x_repr}, {y_repr})"
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
            dict_name="_x_snapshots",
            value=int(self._x._value),
            snapshot_name=snapshot_name,
        )
        self._set_single_snapshot_val_to_dict(
            dict_name="_y_snapshots",
            value=int(self._y._value),
            snapshot_name=snapshot_name,
        )

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

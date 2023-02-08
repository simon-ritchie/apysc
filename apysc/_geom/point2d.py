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
from apysc._type.number import Number
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos


class Point2D(
    VariableNameSuffixAttrOrVarMixIn,
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
    Number(0.0)

    >>> point_1.y
    Number(0.0)
    """

    _x: Number
    _y: Number

    @final
    @arg_validation_decos.is_num(arg_position_index=1)
    @arg_validation_decos.is_num(arg_position_index=2)
    @arg_validation_decos.is_builtin_string(arg_position_index=3, optional=True)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        x: Union[float, Number],
        y: Union[float, Number],
        *,
        variable_name_suffix: str = "",
    ) -> None:
        """
        2-dimensional geometry point.

        Parameters
        ----------
        x : Union[float, Number]
            X-coordinate.
        y : Union[float, Number]
            Y-coordinate.
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

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
        if isinstance(x, ap.Number):
            x_: ap.Number = x
        else:
            suffix: str = self._get_attr_or_variable_name_suffix(value_identifier="x")
            x_ = ap.Number(x, variable_name_suffix=suffix)
        if isinstance(y, ap.Number):
            y_: ap.Number = y
        else:
            suffix = self._get_attr_or_variable_name_suffix(value_identifier="y")
            y_ = ap.Number(y, variable_name_suffix=suffix)
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
    def x(self) -> Number:
        """
        X-coordinate property.

        Returns
        -------
        x : Number
            X-coordinate.

        Examples
        --------
        >>> import apysc as ap
        >>> point: ap.Point2D = ap.Point2D(x=50, y=100)
        >>> point.x = ap.Number(150)
        >>> point.x
        Number(150.0)
        """
        import apysc as ap

        suffix: str = self._get_attr_or_variable_name_suffix(value_identifier="x")
        x: ap.Number = ap.Number(self._x._value, variable_name_suffix=suffix)
        self._append_x_getter_expression(x=x)
        return x

    @x.setter
    @arg_validation_decos.is_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def x(self, value: Number) -> None:
        """
        Update x-coordinate property.

        Parameters
        ----------
        value : Number
            X-coordinate to set.
        """
        import apysc as ap

        if not isinstance(value, ap.Number):
            suffix: str = self._get_attr_or_variable_name_suffix(value_identifier="x")
            value = ap.Number(value, variable_name_suffix=suffix)
        self._x = value
        self._x._append_incremental_calc_substitution_expression()
        self._append_x_setter_expression(value=value)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_x_getter_expression(self, *, x: Number) -> None:
        """
        Append x property getter expression.

        Parameters
        ----------
        x : Number
            Target x value.
        """
        import apysc as ap

        expression: str = f"{x.variable_name} = " f'{self.variable_name}["x"];'
        ap.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_x_setter_expression(self, *, value: Number) -> None:
        """
        Append x property setter expression.

        Parameters
        ----------
        value : Number
            X-coordinate to set.
        """
        import apysc as ap

        expression: str = f'{self.variable_name}["x"] = {value.variable_name};'
        ap.append_js_expression(expression=expression)

    @property
    @add_debug_info_setting(module_name=__name__)
    def y(self) -> Number:
        """
        Y-coordinate property.

        Returns
        -------
        y : Number
            Y-coordinate.

        Examples
        --------
        >>> import apysc as ap
        >>> point: ap.Point2D = ap.Point2D(x=50, y=100)
        >>> point.y = ap.Number(150)
        >>> point.y
        Number(150.0)
        """
        import apysc as ap

        suffix: str = self._get_attr_or_variable_name_suffix(value_identifier="y")
        y: ap.Number = ap.Number(self._y._value, variable_name_suffix=suffix)
        self._append_y_getter_expression(y=y)
        return y

    @y.setter
    @arg_validation_decos.is_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def y(self, value: Number) -> None:
        """
        Update y-coordinate property.

        Parameters
        ----------
        value : Number
            Y-coordinate to set.
        """
        import apysc as ap

        if not isinstance(value, ap.Number):
            suffix: str = self._get_attr_or_variable_name_suffix(value_identifier="y")
            value = ap.Number(value, variable_name_suffix=suffix)
        self._y = value
        self._y._append_incremental_calc_substitution_expression()
        self._append_y_setter_expression(value=value)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_y_getter_expression(self, *, y: Number) -> None:
        """
        Append y property getter expression.

        Parameters
        ----------
        y : Number
            Target y value.
        """
        import apysc as ap

        expression: str = f"{y.variable_name} = " f'{self.variable_name}["y"];'
        ap.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_y_setter_expression(self, *, value: Number) -> None:
        """
        Append y property setter expression.

        Parameters
        ----------
        value : Number
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
            (e.g., `Point2D(Number(50.0), Number(100.0))`).
        """
        x_repr: str = "0"
        if hasattr(self, "_x"):
            x_repr = repr(self._x)
        y_repr: str = "0"
        if hasattr(self, "_y"):
            y_repr = repr(self._y)
        repr_str: str = f"Point2D({x_repr}, {y_repr})"
        return repr_str

    _x_snapshots: Dict[str, float]
    _y_snapshots: Dict[str, float]

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
            value=float(self._x._value),
            snapshot_name=snapshot_name,
        )
        self._set_single_snapshot_val_to_dict(
            dict_name="_y_snapshots",
            value=float(self._y._value),
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

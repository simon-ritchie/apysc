"""Class implementation for boolean.
"""

from typing import Any
from typing import Dict
from typing import Union

from typing_extensions import final

from apysc._event.custom_event_mixin import CustomEventMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.copy_mixin import CopyMixIn
from apysc._type.initial_substitution_exp_mixin import InitialSubstitutionExpMixIn
from apysc._type.int import Int
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos


class Boolean(
    CopyMixIn,
    RevertMixIn,
    CustomEventMixIn,
    VariableNameSuffixMixIn,
    InitialSubstitutionExpMixIn,
):
    """
    Boolean class for the apysc library.

    Notes
    -----
    The Bool class is the alias of the Boolean, and it behaves
    the same as the Boolean class.

    References
    ----------
    - Boolean
        - https://simon-ritchie.github.io/apysc/en/boolean.html

    Examples
    --------
    >>> import apysc as ap
    >>> bool_val_1: ap.Boolean = ap.Boolean(True)
    >>> bool_val_1
    Boolean(True)

    >>> bool_val_2: ap.Bool = ap.Bool(True)
    >>> bool_val_2
    Boolean(True)

    >>> bool_val_2.not_
    Boolean(False)
    """

    _initial_value: Union[bool, int, Int, "Boolean"]
    _value: bool

    @arg_validation_decos.is_acceptable_boolean_value(arg_position_index=1)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        value: Union[bool, int, Int, "Boolean"],
        *,
        variable_name_suffix: str = "",
        skip_init_substitution_expression_appending: bool = False,
    ) -> None:
        """
        Boolean class for apysc library.

        Notes
        -----
        The Bool class is the alias of the Boolean, and it behaves
        the same as the Boolean class.

        Parameters
        ----------
        value : Boolean or Int or bool or int
            Initial boolean value. 0 or 1 are acceptable for
            an integer value.
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript's debugging.
        skip_init_substitution_expression_appending : bool, default False
            A boolean indicates whether to skip an initial substitution
            expression or not. This class uses this option internally.

        References
        ----------
        - Boolean
            - https://simon-ritchie.github.io/apysc/en/boolean.html

        Examples
        --------
        >>> import apysc as ap
        >>> bool_val_1: ap.Boolean = ap.Boolean(True)
        >>> bool_val_1
        Boolean(True)

        >>> bool_val_2: ap.Bool = ap.Bool(True)
        >>> bool_val_2
        Boolean(True)
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        from apysc._expression.event_handler_scope import TemporaryNotHandlerScope

        with TemporaryNotHandlerScope():
            self._variable_name_suffix = variable_name_suffix
            TYPE_NAME: str = var_names.BOOLEAN
            self._initial_value = value
            value_: bool = self._get_bool_from_arg_value(value=value)
            self._value = value_
            self._type_name = TYPE_NAME
            self.variable_name = expression_variables_util.get_next_variable_name(
                type_name=TYPE_NAME
            )
            self._append_constructor_expression()

        self._append_initial_substitution_expression_if_in_handler_scope(
            skip_appending=skip_init_substitution_expression_appending,
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _get_bool_from_arg_value(
        self, *, value: Union[bool, int, Int, "Boolean"]
    ) -> bool:
        """
        Get bool value from specified argument value.

        Parameters
        ----------
        value : Boolean or Int or bool or int
            Specified value. 0 or 1 are acceptable for
            an integer value.

        Returns
        -------
        result : bool
            Converted boolean value.
        """
        from apysc._converter import cast
        from apysc._type.number_value_mixin import NumberValueMixIn
        from apysc._validation import bool_validation

        if isinstance(value, (int, float, NumberValueMixIn)):
            result: bool = cast.to_bool_from_int(integer=value)  # type: ignore
        elif isinstance(value, Boolean):
            result = value._value
        else:
            result = value  # type: ignore
        bool_validation.validate_bool(value=result)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression.
        """
        import apysc as ap

        expression: str = self._create_initial_substitution_expression()
        expression = f"var {expression}"
        ap.append_js_expression(expression=expression)

    @final
    def _create_initial_substitution_expression(self) -> str:
        """
        Create an initial value's substitution expression string.

        Returns
        -------
        expression : str
            Created expression string.
        """
        expression: str = f"{self.variable_name} = "
        if isinstance(self._initial_value, VariableNameMixIn):
            expression += f"Boolean({self._initial_value.variable_name});"
        elif self._value:
            expression += "true;"
        else:
            expression += "false;"
        return expression

    @property
    @add_debug_info_setting(module_name=__name__)
    def value(self) -> Union[bool, int, Int, "Boolean"]:
        """
        Get a current boolean value.

        Returns
        -------
        value : bool
            Current boolean value.

        References
        ----------
        - apysc fundamental data classes value interface
            - https://simon-ritchie.github.io/apysc/en/fundamental_data_classes_value_interface.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> bool_val: ap.Boolean = ap.Boolean(True)
        >>> bool_val.value = False
        >>> bool_val.value
        False

        >>> bool_val.value = ap.Boolean(True)
        >>> bool_val.value
        True
        """
        return self._value

    @value.setter
    @arg_validation_decos.is_acceptable_boolean_value(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def value(self, value: Union[bool, int, Int, "Boolean"]) -> None:
        """
        Set boolean value.

        Parameters
        ----------
        value : Boolean or Int or bool or int
            Any boolean value to set.

        References
        ----------
        - apysc fundamental data classes value interface
            - https://simon-ritchie.github.io/apysc/en/fundamental_data_classes_value_interface.html  # noqa
        """
        from apysc._type.variable_name_mixin import VariableNameMixIn

        self._set_value_and_skip_expression_appending(value=value)
        if isinstance(value, VariableNameMixIn):
            self._append_value_setter_expression(value=value)
        else:
            self._append_value_setter_expression(value=self._value)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_value_setter_expression(
        self, *, value: Union[bool, int, Int, "Boolean"]
    ) -> None:
        """
        Append value's setter expression.

        Parameters
        ----------
        value : bool or VariableNameMixIn
            Any value to set.
        """
        import apysc as ap
        from apysc._type.variable_name_mixin import VariableNameMixIn

        expression: str = f"{self.variable_name} = "
        if isinstance(value, VariableNameMixIn):
            expression += f"Boolean({value.variable_name});"
        elif value:
            expression += "true;"
        else:
            expression += "false;"
        ap.append_js_expression(expression=expression)

    @final
    def _set_value_and_skip_expression_appending(
        self, *, value: Union[bool, int, Int, "Boolean"]
    ) -> None:
        """
        Update value attribute and skip expression appending.

        Parameters
        ----------
        value : Boolean or Int or bool or int
            Any boolean value to set.
        """
        value_: bool = self._get_bool_from_arg_value(value=value)
        self._value = value_

    @final
    def __bool__(self) -> bool:
        """
        Get a boolean value directly.

        Returns
        -------
        result : bool
            Current boolean value.
        """
        return self._value

    def __repr__(self) -> str:
        """
        Get a representation string of this instance.

        Returns
        -------
        repr_str : str
            Representation string of this instance.
        """
        if not hasattr(self, "_value"):
            repr_str: str = "Boolean(False)"
        else:
            repr_str = f"Boolean({self._value})"
        return repr_str

    _value_snapshots: Dict[str, bool]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._set_single_snapshot_val_to_dict(
            dict_name="_value_snapshots", value=self._value, snapshot_name=snapshot_name
        )

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._value = self._value_snapshots[snapshot_name]

    @final
    @add_debug_info_setting(module_name=__name__)
    def __eq__(self, other: Any) -> Any:
        """
        Comparison method for equal condition.

        Parameters
        ----------
        other : *
            The other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        import apysc as ap

        self._validate_comparison_other_type(other=other)
        result: Boolean
        if isinstance(other, Boolean):
            result = Boolean(
                self._value == other._value,
                variable_name_suffix=self._variable_name_suffix,
            )
            self._append_eq_expression(result=result, other=other)
            return result
        elif isinstance(other, ap.Int):
            other_ = bool(other.value)
            result = Boolean(
                self._value == other_, variable_name_suffix=self._variable_name_suffix
            )
        else:
            other = bool(other)
            result = Boolean(
                self._value == other, variable_name_suffix=self._variable_name_suffix
            )
            other = Boolean(other, variable_name_suffix=self._variable_name_suffix)
        self._append_eq_expression(result=result, other=other)
        return result

    @final
    def _validate_comparison_other_type(self, *, other: Any) -> None:
        """
        Validate a comparison's other value type.

        Parameters
        ----------
        other : *
            The other value to compare.

        Raises
        ------
        ValueError
            If the other value type is not Boolean, Int, bool,
            and int.
        """
        import apysc as ap

        ACCEPTABLE_TYPES: tuple = (Boolean, bool, ap.Int, int)
        if isinstance(other, ACCEPTABLE_TYPES):
            return
        raise ValueError(
            "Can't acceptable comparison value type is specified: "
            f"{type(other)}, {other}"
            f"\nAcceptable value types are: {ACCEPTABLE_TYPES}"
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_eq_expression(
        self, *, result: VariableNameMixIn, other: VariableNameMixIn
    ) -> None:
        """
        Append __eq__ method expression.

        Parameters
        ----------
        result : Boolean
            A result boolean value.
        other : Boolean or Int
            The other value to compare.
        """
        import apysc as ap

        other_str: str = other.variable_name
        if isinstance(other, ap.Int):
            other_str = f"Boolean({other_str});"
        expression: str = (
            f"{result.variable_name} = " f"{self.variable_name} === {other_str};"
        )
        ap.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def __ne__(self, other: Any) -> Any:
        """
        Comparison method for not equal condition.

        Parameters
        ----------
        other : *
            The other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        import apysc as ap

        result: Boolean = self == other
        result = result.not_
        if isinstance(other, (Boolean, ap.Int)):
            self._append_ne_expression(result=result, other=other)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_ne_expression(
        self, *, result: VariableNameMixIn, other: VariableNameMixIn
    ) -> None:
        """
        Append __ne__ method expression.

        Parameters
        ----------
        result : Boolean
            A result boolean value.
        other : Boolean or Int
            The other value to compare.
        """
        import apysc as ap

        other_str: str = other.variable_name
        if isinstance(other, ap.Int):
            other_str = f"Boolean({other_str});"
        expression: str = (
            f"{result.variable_name} = " f"{self.variable_name} !== {other_str};"
        )
        ap.append_js_expression(expression=expression)

    @property
    @add_debug_info_setting(module_name=__name__)
    def not_(self) -> "Boolean":
        """
        Get a not condition Boolean value.

        Returns
        -------
        result : Boolean
            Not condition Boolean value.

        Examples
        --------
        >>> import apysc as ap
        >>> bool_val: ap.Boolean = ap.Boolean(True)
        >>> bool_val.not_
        Boolean(False)

        >>> bool_val.value = False
        >>> bool_val.not_
        Boolean(True)
        """
        result: Boolean = Boolean(
            not self, variable_name_suffix=self._variable_name_suffix
        )
        self._append_not_prop_expression(result=result)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_not_prop_expression(self, *, result: VariableNameMixIn) -> None:
        """
        Append not_ property expression.

        Parameters
        ----------
        result : Boolean
            A result Boolean value.
        """
        import apysc as ap

        expression: str = f"{result.variable_name} = " f"!{self.variable_name};"
        ap.append_js_expression(expression=expression)

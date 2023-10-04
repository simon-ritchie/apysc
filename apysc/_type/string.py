"""Class implementation for the string class.
"""

from typing import Any
from typing import Dict
from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._event.custom_event_mixin import CustomEventMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._loop.initialize_with_base_value_interface import (
    InitializeWithBaseValueInterface,
)
from apysc._type.copy_mixin import CopyMixIn
from apysc._type.hashable_interface import HashableInterface
from apysc._type.initial_substitution_exp_mixin import InitialSubstitutionExpMixIn
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.string_apply_max_num_of_decimal_places_mixin import (
    StringApplyMaxNumOfDecimalPlacesMixIn,
)
from apysc._type.string_length_mixin import StringLengthMixIn
from apysc._type.string_lower_mixin import StringLowerMixIn
from apysc._type.string_lstrip_mixin import StringLStripMixIn
from apysc._type.string_rstrip_mixin import StringRStripMixIn
from apysc._type.string_slice_mixin import StringSliceMixIn
from apysc._type.string_split_mixin import StringSplitMixIn
from apysc._type.string_strip_mixin import StringStripMixIn
from apysc._type.string_upper_mixin import StringUpperMixIn
from apysc._type.string_zfill_mixin import StringZfillMixIn
from apysc._type.to_number_mixin import ToNumberMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos


class String(
    StringSplitMixIn,
    StringLStripMixIn,
    StringStripMixIn,
    StringRStripMixIn,
    CopyMixIn["String"],
    RevertMixIn,
    CustomEventMixIn,
    VariableNameSuffixMixIn,
    InitialSubstitutionExpMixIn,
    InitializeWithBaseValueInterface,
    HashableInterface,
    ToNumberMixIn,
    StringLengthMixIn,
    StringApplyMaxNumOfDecimalPlacesMixIn,
    StringZfillMixIn,
    StringLowerMixIn,
    StringUpperMixIn,
    StringSliceMixIn,
):
    """
    String class for apysc library.

    Notes
    -----
    The `Str` class is the alias of `String`.

    References
    ----------
    - String
        - https://simon-ritchie.github.io/apysc/en/string.html
    - String class comparison operations
        - https://simon-ritchie.github.io/apysc/en/string_comparison_operations.html  # noqa
    - String class addition and multiplication operations
        - https://simon-ritchie.github.io/apysc/en/string_addition_and_multiplication.html  # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> _ = ap.Stage()
    >>> string: ap.String = ap.String("Hello")
    >>> string
    String("Hello")

    >>> string += " World!"
    >>> string
    String("Hello World!")

    >>> string.value = "World!"
    >>> string
    String("World!")

    >>> string.value = "Hello!"
    >>> string *= 3
    >>> string
    String("Hello!Hello!Hello!")
    """

    _initial_value: Union[str, "String"]
    _value: str

    @arg_validation_decos.is_string(arg_position_index=1, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        value: Union[str, "String"],
        *,
        variable_name_suffix: str = "",
        skip_init_substitution_expression_appending: bool = False,
    ) -> None:
        """
        String class for apysc library.

        Parameters
        ----------
        value : String or str
            Initial string value.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        skip_init_substitution_expression_appending : bool, default False
            A boolean indicates whether to skip an initial substitution
            expression or not. This class uses this option internally.

        Notes
        -----
        The `Str` class is the alias of `String`.

        References
        ----------
        - String
            - https://simon-ritchie.github.io/apysc/en/string.html
        - String class comparison operations
            - https://simon-ritchie.github.io/apysc/en/string_comparison_operations.html  # noqa
        - String class addition and multiplication operations
            - https://simon-ritchie.github.io/apysc/en/string_addition_and_multiplication.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> string: ap.String = ap.String("Hello")
        >>> string
        String("Hello")

        >>> string += " World!"
        >>> string
        String("Hello World!")
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        from apysc._expression.event_handler_scope import TemporaryNotHandlerScope

        with TemporaryNotHandlerScope():
            value = _escape_str_value(value=value)
            self._variable_name_suffix = variable_name_suffix
            TYPE_NAME: str = var_names.STRING
            self._initial_value = value
            self._type_name = TYPE_NAME
            self._value = self._get_str_value(value=value)
            self.variable_name = expression_variables_util.get_next_variable_name(
                type_name=TYPE_NAME
            )
            self._append_constructor_expression()

        self._append_initial_substitution_expression_if_in_handler_scope(
            skip_appending=skip_init_substitution_expression_appending,
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_constructor_expression(self) -> None:
        """
        Append a constructor expression.
        """
        from apysc._expression import expression_data_util

        expression: str = self._create_initial_substitution_expression()
        expression = f"var {expression}"
        expression_data_util.append_js_expression(expression=expression)

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
        if isinstance(self._initial_value, String):
            expression += f"{self._initial_value.variable_name};"
        else:
            expression += f'"{self._value}";'
        return expression

    @final
    def _get_str_value(self, *, value: Union[str, "String"]) -> str:
        """
        Get a (Python's) str value from a specified value.

        Parameters
        ----------
        value : String or str
            Target string value.

        Returns
        -------
        value : str
            Python's built-in str value.
        """
        if isinstance(value, String):
            return value._value
        return str(value)

    @property
    @add_debug_info_setting(module_name=__name__)
    def value(self) -> Union[str, "String"]:
        """
        Get a current string value.

        Returns
        -------
        value : str
            Current string value.

        References
        ----------
        - apysc fundamental data classes value interface
            - https://simon-ritchie.github.io/apysc/en/fundamental_data_classes_value_interface.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> string: ap.String = ap.String("Hello")
        >>> string.value = "World!"
        >>> string.value
        'World!'
        """
        return self._value

    @value.setter
    @arg_validation_decos.is_string(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def value(self, value: Union[str, "String"]) -> None:
        """
        Set string value.

        Parameters
        ----------
        value : String or str
            Any string value to set.

        References
        ----------
        - apysc fundamental data classes value interface
            - https://simon-ritchie.github.io/apysc/en/fundamental_data_classes_value_interface.html  # noqa
        """
        self._value = self._get_str_value(value=value)
        self._append_value_setter_expression(value=value)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_value_setter_expression(self, *, value: Union[str, "String"]) -> None:
        """
        Append value's setter expression.

        Parameters
        ----------
        value : String or str
            Any string value to set.
        """
        from apysc._expression import expression_data_util

        expression: str = f"{self.variable_name} = "
        if isinstance(value, String):
            expression += f"{value.variable_name};"
        else:
            expression += f'"{value}";'
        expression_data_util.append_js_expression(expression=expression)

    @final
    @arg_validation_decos.is_string(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __add__(self, other: Union[str, "String"]) -> "String":
        """
        Method for addition (string concatenation).

        Parameters
        ----------
        other : String or str
            The other string value to concatenate.

        Returns
        -------
        result : String
            Concatenated result string.
        """
        if isinstance(other, String):
            value: str = self._value + other._value
        else:
            value = self._value + other  # type: ignore
        result: String = self._copy()
        result._value = value
        self._append_addition_expression(result=result, other=other)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_addition_expression(
        self, *, result: VariableNameMixIn, other: Union[str, "String"]
    ) -> None:
        """
        Append addition (string concatenation) expression.

        Parameters
        ----------
        result : String
            Addition result value.
        other : String or str
            The other string value to concatenate.
        """
        from apysc._expression import expression_data_util
        from apysc._type.value_util import get_value_str_for_expression

        right_value: str = get_value_str_for_expression(value=other)
        expression: str = (
            f"var {result.variable_name} = " f"{self.variable_name} + {right_value};"
        )
        expression_data_util.append_js_expression(expression=expression)

    @final
    @arg_validation_decos.is_integer(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __mul__(self, other: Union[int, Any]) -> "String":
        """
        Method for multiplication (string repetition).

        Parameters
        ----------
        other : Int or int
            String repetition number.

        Returns
        -------
        result : String
            Repeated result string.
        """
        from apysc._type.int import Int

        if isinstance(other, Int):
            value: int = other.value  # type: ignore
        else:
            value = other
        result: String = self._copy()
        result._value = result._value * value
        self._append_multiplication_expression(result=result, other=other)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_multiplication_expression(
        self, *, result: VariableNameMixIn, other: Union[int, Any]
    ) -> None:
        """
        Append multiplication (string repetition) expression.

        Parameters
        ----------
        result : String
            Multiplication result value.
        other : Int or int
            String repetition number.
        """
        from apysc._expression import expression_data_util
        from apysc._type.int import Int

        expression: str = f'var {result.variable_name} = "";'
        expression += "\nfor (var i = 0; i < "
        if isinstance(other, Int):
            expression += f"{other.variable_name}"
        else:
            expression += f"{other}"
        expression += "; i++) {"
        expression += f"\n  {result.variable_name} += {self.variable_name};"
        expression += "\n}"
        expression_data_util.append_js_expression(expression=expression)

    @final
    @arg_validation_decos.is_string(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __iadd__(self, other: Union[str, "String"]) -> Any:
        """
        Method for incremental addition (string concatenation).

        Parameters
        ----------
        other : String or str
            The other string value to concatenate.

        Returns
        -------
        result : String
            Concatenated result string.
        """
        from apysc._expression import expression_variables_util

        result: String = self + other
        expression_variables_util.append_substitution_expression(
            left_value=self, right_value=result
        )
        result.variable_name = self.variable_name
        return result

    @final
    @arg_validation_decos.is_integer(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __imul__(self, other: Union[int, Any]) -> Any:
        """
        Method for incremental multiplication (string repetition).

        Parameters
        ----------
        other : Int or int
            String repetition number.

        Returns
        -------
        result : String
            Repetition result string.
        """
        from apysc._expression import expression_variables_util

        result: String = self * other
        expression_variables_util.append_substitution_expression(
            left_value=self, right_value=result
        )
        result.variable_name = self.variable_name
        return result

    def __str__(self) -> str:
        """
        Method for str conversion.

        Returns
        -------
        result : str
            Python builtins str value.
        """
        if not hasattr(self, "_value"):
            return ""
        return self._value

    @final
    @add_debug_info_setting(module_name=__name__)
    def __eq__(self, other: Any) -> Any:
        """
        Method for equal comparison.

        Parameters
        ----------
        other : *
            Any value to compare.

        Returns
        -------
        result : Boolean
            Comparison result. If the equal value of a String
            or str is specified, this interface returns True.
        """
        from apysc._type.boolean import Boolean

        if isinstance(other, str):
            result: Boolean = Boolean(
                self._value == other, variable_name_suffix=self._variable_name_suffix
            )
        elif isinstance(other, String):
            result = Boolean(
                self._value == other._value,
                variable_name_suffix=self._variable_name_suffix,
            )
        else:
            result = Boolean(False)
        other = self._convert_other_val_to_string(other=other)
        if isinstance(other, VariableNameMixIn):
            self._append_eq_expression(result=result, other=other)
        return result

    @final
    def _convert_other_val_to_string(self, *, other: Any) -> Any:
        """
        Convert a comparison other value to a String if it is
        a string value.

        Parameters
        ----------
        other : *
            Other comparison value.

        Returns
        -------
        converted_val : *
            Converted value. If the other value is a string,
            this interface converts it to a String value.
            This interface returns the other type value
            directly (not to be converted).
        """
        if isinstance(other, str):
            return String(other, variable_name_suffix=self._variable_name_suffix)
        return other

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
            Result boolean value.
        other : VariableNameMixIn
            Other value to compare.
        """
        from apysc._expression import expression_data_util

        expression: str = (
            f"{result.variable_name} = "
            f"{self.variable_name} === {other.variable_name};"
        )
        expression_data_util.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def __ne__(self, other: Any) -> Any:
        """
        Method for not equal comparison.

        Parameters
        ----------
        other : *
            Any value to compare.

        Returns
        -------
        result : Boolean
            Comparison result. If a specified value is not
            the equal value of a String or str, this interface
            returns True.
        """
        from apysc._type.boolean import Boolean

        if isinstance(other, str):
            result: Boolean = Boolean(
                self._value != other, variable_name_suffix=self._variable_name_suffix
            )
        elif isinstance(other, String):
            result = Boolean(
                self._value != other._value,
                variable_name_suffix=self._variable_name_suffix,
            )
        else:
            result = Boolean(True, variable_name_suffix=self._variable_name_suffix)
        other = self._convert_other_val_to_string(other=other)
        if isinstance(other, VariableNameMixIn):
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
            Result boolean value.
        other : VariableNameMixIn
            Other value to compare.
        """
        from apysc._expression import expression_data_util

        expression: str = (
            f"{result.variable_name} = "
            f"{self.variable_name} !== {other.variable_name};"
        )
        expression_data_util.append_js_expression(expression=expression)

    @final
    @arg_validation_decos.is_string(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __lt__(self, other: Union[str, Any]) -> Any:
        """
        Method for less than comparison.

        Parameters
        ----------
        other : String or str
            String value to compare.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        from apysc._type.boolean import Boolean

        value: str = self._get_str_value(value=other)
        result: Boolean = Boolean(
            self._value < value, variable_name_suffix=self._variable_name_suffix
        )
        other = self._convert_other_val_to_string(other=other)
        if isinstance(other, VariableNameMixIn):
            self._append_lt_expression(result=result, other=other)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_lt_expression(
        self, *, result: VariableNameMixIn, other: VariableNameMixIn
    ) -> None:
        """
        Append __lt__ method expression.

        Parameters
        ----------
        result : Boolean
            Result boolean value.
        other : VariableNameMixIn
            Other value to compare.
        """
        from apysc._expression import expression_data_util

        expression: str = (
            f"{result.variable_name} = "
            f"{self.variable_name} < {other.variable_name};"
        )
        expression_data_util.append_js_expression(expression=expression)

    @final
    @arg_validation_decos.is_string(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __le__(self, other: Union[str, Any]) -> Any:
        """
        Method for less than or equal comparison.

        Parameters
        ----------
        other : String or str
            String value to compare.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        from apysc._type.boolean import Boolean

        value: str = self._get_str_value(value=other)
        result: Boolean = Boolean(
            self._value <= value, variable_name_suffix=self._variable_name_suffix
        )
        other = self._convert_other_val_to_string(other=other)
        if isinstance(other, VariableNameMixIn):
            self._append_le_expression(result=result, other=other)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_le_expression(
        self, *, result: VariableNameMixIn, other: VariableNameMixIn
    ) -> None:
        """
        Append __le__ method expression.

        Parameters
        ----------
        result : Boolean
            Result boolean value.
        other : VariableNameMixIn
            Other value to compare.
        """
        from apysc._expression import expression_data_util

        expression: str = (
            f"{result.variable_name} = "
            f"{self.variable_name} <= {other.variable_name};"
        )
        expression_data_util.append_js_expression(expression=expression)

    @final
    @arg_validation_decos.is_string(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __gt__(self, other: Union[str, Any]) -> Any:
        """
        Method for greater than comparison.

        Parameters
        ----------
        other : String or str
            String value to compare.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        from apysc._type.boolean import Boolean

        value: str = self._get_str_value(value=other)
        result: Boolean = Boolean(
            self._value > value, variable_name_suffix=self._variable_name_suffix
        )
        other = self._convert_other_val_to_string(other=other)
        if isinstance(other, VariableNameMixIn):
            self._append_gt_expression(result=result, other=other)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_gt_expression(
        self, *, result: VariableNameMixIn, other: VariableNameMixIn
    ) -> None:
        """
        Append __gt__ method expression.

        Parameters
        ----------
        result : Boolean
            Result boolean value.
        other : VariableNameMixIn
            Other value to compare.
        """
        from apysc._expression import expression_data_util

        expression: str = (
            f"{result.variable_name} = "
            f"{self.variable_name} > {other.variable_name};"
        )
        expression_data_util.append_js_expression(expression=expression)

    @final
    @arg_validation_decos.is_string(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __ge__(self, other: Union[str, Any]) -> Any:
        """
        Method for greater than or equal comparison.

        Parameters
        ----------
        other : String or str
            String value to compare.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        from apysc._type.boolean import Boolean

        value: str = self._get_str_value(value=other)
        result: Boolean = Boolean(
            self._value >= value, variable_name_suffix=self._variable_name_suffix
        )
        other = self._convert_other_val_to_string(other=other)
        if isinstance(other, VariableNameMixIn):
            self._append_ge_expression(result=result, other=other)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_ge_expression(
        self, *, result: VariableNameMixIn, other: VariableNameMixIn
    ) -> None:
        """
        Append __ge__ method expression.

        Parameters
        ----------
        result : Boolean
            Result boolean value.
        other : VariableNameMixIn
            Other value to compare.
        """
        from apysc._expression import expression_data_util

        expression: str = (
            f"{result.variable_name} = "
            f"{self.variable_name} >= {other.variable_name};"
        )
        expression_data_util.append_js_expression(expression=expression)

    def __int__(self) -> int:
        """
        Method for integer conversion.

        Returns
        -------
        result : int
            Converted integer value.
        """
        result: int = int(self._value)
        return result

    def __float__(self) -> float:
        """
        Method for float conversion.

        Returns
        -------
        result : float
            Converted float value.
        """
        result: float = float(self._value)
        return result

    def __repr__(self) -> str:
        """
        Get a representation string of this instance.

        Returns
        -------
        repr_str : str
            Representation string of this instance.
        """
        if not hasattr(self, "_value"):
            repr_str: str = 'String("")'
        else:
            repr_str = f'String("{self._value}")'
        return repr_str

    _value_snapshots: Optional[Dict[str, str]] = None

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

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
        Revert a value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._value = self._get_snapshot_val_if_exists(
            current_value=self._value,
            snapshot_dict=self._value_snapshots,
            snapshot_name=snapshot_name,
        )

    @classmethod
    @final
    def _initialize_with_base_value(cls) -> "String":
        """
        Initialize this class with a base value(s).

        Returns
        -------
        str_value : String
            An initialized string value.
        """
        return String("")

    @final
    def __hash__(self) -> int:
        """
        Get a hashed value.

        Returns
        -------
        hashed_value : int
            A hashed value.
        """
        return hash(self._value)


def _escape_str_value(*, value: Union[str, "String"]) -> Union[str, "String"]:
    """
    Escape a specified string value.

    Notes
    -----
    This function only applies to escape only when a specified value type
    is `str`.

    Parameters
    ----------
    value : Union[str, "String"]
        A specified string value.

    Returns
    -------
    value : Unjion[str, "String"]
        An escaped string value.
    """
    from apysc._string import string_util

    if isinstance(value, str):
        value = string_util.escape_str(string=value)
        return value

    return value

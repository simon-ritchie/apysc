"""Class implementation of the floating-point number value.
"""

from typing import Any
from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._loop.initialize_with_base_value_interface import (
    InitializeWithBaseValueInterface,
)
from apysc._type.hashable_interface import HashableInterface
from apysc._type.number_value_mixin import NumberValueMixIn
from apysc._type.to_fixed_mixin import ToFixedMixIn
from apysc._type.to_hex_mixin import ToHexMixIn
from apysc._type.to_string_mixin import ToStringMixIn
from apysc._validation import arg_validation_decos


class Number(
    NumberValueMixIn[float, "Number"],
    InitializeWithBaseValueInterface,
    ToStringMixIn,
    ToFixedMixIn,
    HashableInterface,
    ToHexMixIn,
):
    """
    Floating point number class for the apysc library.

    Notes
    -----
    The `Float` class is the alias of the Number,
    and it behaves the same as the Number class.

    References
    ----------
    - Int and Number
        - https://simon-ritchie.github.io/apysc/en/int_and_number.html
    - Int and Number common arithmetic operations
        - https://simon-ritchie.github.io/apysc/en/int_and_number_arithmetic_operations.html  # noqa
    - Int and Number common comparison operations
        - https://simon-ritchie.github.io/apysc/en/int_and_number_comparison_operations.html  # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> _ = ap.Stage()
    >>> number: ap.Number = ap.Number(10.5)
    >>> number
    Number(10.5)

    >>> number == 10.5
    Boolean(True)

    >>> number == ap.Number(10.5)
    Boolean(True)

    >>> number >= 10.5
    Boolean(True)

    >>> number += 10.3
    >>> number
    Number(20.8)
    """

    @arg_validation_decos.is_num(arg_position_index=1, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        value: Union[int, float, NumberValueMixIn],
        *,
        variable_name_suffix: str = "",
        skip_init_substitution_expression_appending: bool = False,
    ) -> None:
        """
        Floating point number class for apysc library.

        Parameters
        ----------
        value : int or float or Int or Number
            Initial floating point number value. This class
            casts it to float if you specify int or Int value.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        skip_init_substitution_expression_appending : bool, default False
            A boolean indicates whether to skip an initial substitution
            expression or not. This class uses this option internally.

        Notes
        -----
        The `Float` class is the alias of the Number, and it behaves
        the same as the Number class.

        References
        ----------
        - Int and Number
            - https://simon-ritchie.github.io/apysc/en/int_and_number.html
        - Int and Number common arithmetic operations
            - https://simon-ritchie.github.io/apysc/en/int_and_number_arithmetic_operations.html  # noqa
        - Int and Number common comparison operations
            - https://simon-ritchie.github.io/apysc/en/int_and_number_comparison_operations.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> number: ap.Number = ap.Number(10.5)
        >>> number
        Number(10.5)

        >>> number == 10.5
        Boolean(True)

        >>> number == ap.Number(10.5)
        Boolean(True)

        >>> number >= 10.5
        Boolean(True)

        >>> number += 10.3
        >>> number
        Number(20.8)
        """
        from apysc._converter import cast
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        from apysc._expression.event_handler_scope import TemporaryNotHandlerScope

        with TemporaryNotHandlerScope():
            TYPE_NAME: str = var_names.NUMBER
            self.variable_name = expression_variables_util.get_next_variable_name(
                type_name=TYPE_NAME
            )
            super(Number, self).__init__(
                value=value,
                type_name=TYPE_NAME,
                variable_name_suffix=variable_name_suffix,
            )
            self._value = cast.to_float_from_int(int_or_float=self.value)
            self._append_constructor_expression()

        self._append_initial_substitution_expression_if_in_handler_scope(
            skip_appending=skip_init_substitution_expression_appending,
        )

    @final
    @arg_validation_decos.is_num(arg_position_index=1, optional=False)
    def _set_value_and_skip_expression_appending(
        self, *, value: Union[int, float, Any]
    ) -> None:
        """
        Update value attribute and skip expression appending.

        Parameters
        ----------
        value : int or float or Int or Number
            Any number value to set. If a float or Number
            value is specified, this interface casts its
            value to an integer.
        """
        from apysc._converter import cast

        if isinstance(value, NumberValueMixIn):
            value._value = cast.to_float_from_int(int_or_float=value._value)
            value_ = value._value
        else:
            value = cast.to_float_from_int(int_or_float=value)
            value_ = value
        self._value = value_

    def __repr__(self) -> str:
        """
        Get a representation string of this instance.

        Returns
        -------
        repr_str : str
            Representation string of this instance.
        """
        if not hasattr(self, "_value"):
            repr_str: str = "Number(0)"
        else:
            repr_str = f"Number({self._value})"
        return repr_str

    @classmethod
    @final
    def _initialize_with_base_value(cls) -> "Number":
        """
        Initialize this class with a base value(s).

        Returns
        -------
        num_value : Number
            An initialized number value.
        """
        return Number(0)

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

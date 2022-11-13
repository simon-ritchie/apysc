"""Class implementation for the dictionary value.
"""

from typing import Any
from typing import Dict
from typing import Generic
from typing import TypeVar
from typing import Union

from typing_extensions import final

from apysc._event.custom_event_mixin import CustomEventMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.any_value import AnyValue
from apysc._type.boolean import Boolean
from apysc._type.copy_mixin import CopyMixIn
from apysc._type.dictionary_structure import DictionaryStructure
from apysc._type.expression_string import ExpressionString
from apysc._type.initial_substitution_exp_mixin import InitialSubstitutionExpMixIn
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.string import String
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos

DefaultType = TypeVar("DefaultType")

_BuiltinKeys = Union[str, int, float]
_K = TypeVar("_K")
_V = TypeVar("_V")


class Dictionary(
    CustomEventMixIn,
    Generic[_K, _V],
    CopyMixIn,
    RevertMixIn,
    DictionaryStructure,
    VariableNameSuffixMixIn,
    InitialSubstitutionExpMixIn,
):
    """
    Dictionary class for the apysc library.

    References
    ----------
    - Dictionary
        - https://simon-ritchie.github.io/apysc/en/dictionary.html
    - Dictionary class generic type settings
        - https://simon-ritchie.github.io/apysc/en/dictionary_generic.html  # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> dictionary: ap.Dictionary = ap.Dictionary({"a": 10})
    >>> dictionary
    Dictionary({'a': 10})

    >>> dictionary["a"]
    10

    >>> dictionary["b"] = 20
    >>> dictionary["b"]
    20

    >>> dictionary.length
    Int(2)

    >>> value_1: int = dictionary.get("c", default=0)
    >>> value_1
    0
    """

    _initial_value: Union[Dict[_K, _V], "Dictionary"]
    _value: Dict[_K, _V]

    @arg_validation_decos.is_acceptable_dictionary_value(arg_position_index=1)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        value: Union[Dict[_K, _V], "Dictionary"],
        *,
        variable_name_suffix: str = "",
        skip_init_substitution_expression_appending: bool = False,
    ) -> None:
        """
        Dictionary class for the apysc library.

        Parameters
        ----------
        value : dict or Dictionary
            Initial dictionary value.
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript's debugging.
        skip_init_substitution_expression_appending : bool, default False
            A boolean indicates whether to skip an initial substitution
            expression or not. This class uses this option internally.

        References
        ----------
        - Dictionary
            - https://simon-ritchie.github.io/apysc/en/dictionary.html
        - Dictionary class generic type settings
            - https://simon-ritchie.github.io/apysc/en/dictionary_generic.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> dictionary: ap.Dictionary = ap.Dictionary({"a": 10})
        >>> dictionary
        Dictionary({'a': 10})

        >>> dictionary["a"]
        10

        >>> dictionary["b"] = 20
        >>> dictionary["b"]
        20
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        from apysc._expression.event_handler_scope import TemporaryNotHandlerScope

        with TemporaryNotHandlerScope():
            self._variable_name_suffix = variable_name_suffix
            TYPE_NAME: str = var_names.DICTIONARY
            self._initial_value = value
            self._type_name = TYPE_NAME
            self._value = self._get_dict_value(value=value)
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
        from apysc._type import value_util

        value_str: str = value_util.get_value_str_for_expression(
            value=self._initial_value
        )
        expression: str = f"{self.variable_name} = {value_str};"
        return expression

    @final
    def _get_dict_value(
        self, *, value: Union[Dict[_K, _V], "Dictionary"]
    ) -> Dict[_K, _V]:
        """
        Get a dict value from a specified value.

        Parameters
        ----------
        value : dict or Dictionary
            Specified dictionary value.

        Returns
        -------
        dict_val : dict
            Converted dict value.
        """
        if isinstance(value, Dictionary):
            return value._value
        return value  # type: ignore

    @property
    @add_debug_info_setting(module_name=__name__)
    def value(self) -> Union[Dict[_K, _V], "Dictionary"]:
        """
        Get a current dict value.

        Returns
        -------
        value : dict
            Current dict value.

        References
        ----------
        - apysc fundamental data classes value interface
            - https://simon-ritchie.github.io/apysc/en/fundamental_data_classes_value_interface.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> dictionary: ap.Dictionary = ap.Dictionary({})
        >>> dictionary.value = {"a": 10}
        >>> dictionary.value
        {'a': 10}
        """
        return self._value

    @value.setter
    @arg_validation_decos.is_acceptable_dictionary_value(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def value(self, value: Union[Dict[_K, _V], "Dictionary"]) -> None:
        """
        Set dictionary value.

        Parameters
        ----------
        value : dict or Dictionary.
            Dictionary value to set.

        References
        ----------
        - apysc fundamental data classes value interface
            - https://simon-ritchie.github.io/apysc/en/fundamental_data_classes_value_interface.html  # noqa
        """
        self._value = self._get_dict_value(value=value)
        self._append_value_setter_expression(value=value)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_value_setter_expression(
        self, *, value: Union[Dict[_K, _V], "Dictionary"]
    ) -> None:
        """
        Append value's setter expression.

        Parameters
        ----------
        value : dict or Dictionary.
            Dictionary value to set.
        """
        import apysc as ap
        from apysc._type import value_util

        value_str: str = value_util.get_value_str_for_expression(value=value)
        expression: str = f"{self.variable_name} = {value_str};"
        ap.append_js_expression(expression=expression)

    _value_snapshot: Dict[str, Dict[_K, _V]]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make values' snapthot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._set_single_snapshot_val_to_dict(
            dict_name="_value_snapshot",
            value={**self._value},
            snapshot_name=snapshot_name,
        )

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert values if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._value = self._value_snapshot[snapshot_name]

    def __str__(self) -> str:
        """
        String conversion method.

        Returns
        -------
        string : str
            Converted value string.
        """
        if not hasattr(self, "_value"):
            return "{}"
        return str(self._value)

    def __repr__(self) -> str:
        """
        Get a representation string of this instance.

        Returns
        -------
        repr_str : str
            Representation string of this instance.
        """
        if not hasattr(self, "_value"):
            repr_str: str = "Dictionary({})"
        else:
            repr_str = f"Dictionary({self._value})"
        return repr_str

    @property
    @add_debug_info_setting(module_name=__name__)
    def length(self) -> Int:
        """
        Get length of this dictionary values.

        Returns
        -------
        length : Int
            This dictionary value's length.

        References
        ----------
        - Dictionary length interface
            - https://simon-ritchie.github.io/apysc/en/dictionary_length.html

        Examples
        --------
        >>> import apysc as ap
        >>> dictionary: ap.Dictionary = ap.Dictionary({"a": 1, "b": 2})
        >>> dictionary.length
        Int(2)
        """
        import apysc as ap

        length: ap.Int = ap.Int(len(self._value))
        self._append_length_expression(length=length)
        return length

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_length_expression(self, *, length: Int) -> None:
        """
        Append length method expression.

        Parameters
        ----------
        length : Int
            Created length Int variable.
        """
        import apysc as ap

        expression: str = (
            f"{length.variable_name} = " f"Object.keys({self.variable_name}).length;"
        )
        ap.append_js_expression(expression=expression)

    @final
    def __len__(self) -> None:
        """
        This method is disabled and can't use from a
        Dictionary instance.
        """
        raise Exception(
            "Dictionary instance can't apply len function."
            " Please use length property instead."
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def __getitem__(self, key: Union[_K, ExpressionString]) -> _V:
        """
        Get a specified key's single value.

        Parameters
        ----------
        key : _K
            Dictionary key.

        Returns
        -------
        value : *
            Specified key's value.
        """
        import apysc as ap

        self._validate_key_type_is_str_or_numeric(key=key)
        key_: _BuiltinKeys = self._get_builtin_type_key(key=key)
        has_key: bool = key_ in self._value
        if has_key:
            value: Any = self._value[key_]  # type: ignore
        else:
            value = ap.AnyValue(None)
        self._append_getitem_expression(key=key, value=value)
        return value

    @final
    def _get_builtin_type_key(
        self, *, key: Union[_K, ExpressionString]
    ) -> _BuiltinKeys:
        """
        Get a built-in type's key (str, int, or float) from
        a specified key.

        Parameters
        ----------
        key : _K
            Target key value (including String, Int, and Number).

        Returns
        -------
        key : str or int or float
            Built-in type's key.
        """
        if isinstance(key, ExpressionString):
            return key.value
        if isinstance(key, (String, Int, Number)):
            return key._value
        key_: _BuiltinKeys = key  # type: ignore
        return key_

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_getitem_expression(
        self, *, key: Union[_K, ExpressionString], value: Any
    ) -> None:
        """
        Append __getitem__ expression.

        Parameters
        ----------
        key : _K
            Dictionary key.
        value : *
            Specified key's value.
        """
        import apysc as ap
        from apysc._type import value_util

        if not isinstance(value, VariableNameMixIn):
            value = ap.AnyValue(None)
        key_str: str = value_util.get_value_str_for_expression(value=key)
        expression: str = (
            f"var {value.variable_name} = " f"{self.variable_name}[{key_str}];"
        )
        ap.append_js_expression(expression=expression)

    @final
    def _validate_key_type_is_str_or_numeric(
        self, *, key: Union[_K, ExpressionString]
    ) -> None:
        """
        Validate whether a key's value type is acceptable
        (str or int or float) or not.

        Parameters
        ----------
        key : _K
            Dictionary key to check.

        Raises
        ------
        ValueError
            If a key's type is not String, Int, Number, str, int,
            or float.
        """
        if isinstance(key, (str, String, int, Int, float, Number, ExpressionString)):
            return
        raise ValueError(
            f"Unsupported key type is specified: {type(key)}, {key}"
            f"\nSuppoting types are: str, String, int, Int"
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def __setitem__(self, key: Union[_K, ExpressionString], value: _V) -> None:
        """
        Set value to a specified key position.

        Parameters
        ----------
        key : _K
            Dictionary key to set value.
        value : *
            Any value to set.
        """
        key_: _BuiltinKeys = self._get_builtin_type_key(key=key)
        self._value[key_] = value  # type: ignore
        self._append_setitem_expression(key=key, value=value)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_setitem_expression(
        self, *, key: Union[_K, ExpressionString], value: _V
    ) -> None:
        """
        Append __setitem__ method expression.

        Parameters
        ----------
        key : _K
            Dictionary key to check.
        value : *
            Any value to set.
        """
        import apysc as ap
        from apysc._type import value_util

        key_str: str = value_util.get_value_str_for_expression(value=key)
        value_str: str = value_util.get_value_str_for_expression(value=value)
        expression: str = f"{self.variable_name}[{key_str}] = {value_str};"
        ap.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def __delitem__(self, key: Union[_K, ExpressionString]) -> None:
        """
        Delete specified key's value from a dictionary.

        Parameters
        ----------
        key : _K
            Dictionary key to delete.
        """
        key_: _BuiltinKeys = self._get_builtin_type_key(key=key)
        if key_ in self._value:
            del self._value[key_]  # type: ignore
        self._append_delitem_expression(key=key)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_delitem_expression(self, *, key: Union[_K, ExpressionString]) -> None:
        """
        Append __delitem__ method expression.

        Parameters
        ----------
        key : _K
            Dictionary key to delete.
        """
        import apysc as ap
        from apysc._type import value_util

        key_str: str = value_util.get_value_str_for_expression(value=key)
        expression: str = f"delete {self.variable_name}[{key_str}];"
        ap.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def __eq__(self, other: Any) -> Any:
        """
        Equal comparison method.

        Parameters
        ----------
        other : *
            The other value to compare. dict or Dictionary
            types are acceptable.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        import apysc as ap

        if isinstance(other, Dictionary):
            result: ap.Boolean = ap.Boolean(self._value == other._value)
        else:
            result = ap.Boolean(self._value == other)
            if isinstance(other, dict):
                other = Dictionary(other)
        if isinstance(other, VariableNameMixIn):
            self._append_eq_expression(result=result, other=other)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_eq_expression(
        self, *, result: Boolean, other: VariableNameMixIn
    ) -> None:
        """
        Append an __eq__ expression.

        Parameters
        ----------
        result : Boolean
            A result boolean value.
        other : Dictionary
            The Dictionary's other value to compare.
        """
        import apysc as ap

        expression: str = (
            f"{result.variable_name} = "
            f"_.isEqual({self.variable_name}, {other.variable_name});"
        )
        ap.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def __ne__(self, other: Any) -> Any:
        """
        Noe equal comparison method.

        Parameters
        ----------
        other : *
            The other value to compare. dict or Dictionary types
            are acceptable.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        import apysc as ap

        if isinstance(other, dict):
            other = Dictionary(other)
        result: ap.Boolean = self == other
        result = result.not_
        if isinstance(other, VariableNameMixIn):
            self._append_ne_expression(result=result, other=other)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_ne_expression(
        self, *, result: Boolean, other: VariableNameMixIn
    ) -> None:
        """
        Append a __ne__ expression.

        Parameters
        ----------
        result : Boolean
            A result boolean value.
        other : Dictionary
            The Dictionary's other value to compare.
        """
        import apysc as ap

        expression: str = (
            f"{result.variable_name} = "
            f"!_.isEqual({self.variable_name}, {other.variable_name});"
        )
        ap.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def get(
        self, key: Union[_K, ExpressionString], *, default: DefaultType = None
    ) -> DefaultType:
        """
        Get a specified key dictionary value. If this
        dictionary hasn't a specified key, this interface
        returns a default value.

        Parameters
        ----------
        key : _K
            Target key.
        default : DefaultType or None, optional
            Any default value.

        Returns
        -------
        result_value : Any
            Extracted value or a default value.

        References
        ----------
        - Dictionary get interface
            - https://simon-ritchie.github.io/apysc/en/dictionary_get.html

        Examples
        --------
        >>> from typing import Optional
        >>> import apysc as ap
        >>> dictionary: ap.Dictionary = ap.Dictionary({"a": 10})
        >>> value_1: Optional[int] = dictionary.get("a")
        >>> value_1
        10

        >>> value_2: Optional[int] = dictionary.get("b")
        >>> print(value_2)
        None

        >>> value_3: int = dictionary.get("c", default=0)
        >>> value_3
        0
        """
        key_: _BuiltinKeys = self._get_builtin_type_key(key=key)
        if key_ in self._value:
            result_value: Any = self._value[key_]  # type: ignore
        else:
            result_value = default
        self._append_get_expression(key=key, result_value=result_value, default=default)
        return result_value

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_get_expression(
        self, *, key: Union[_K, ExpressionString], result_value: Any, default: Any
    ) -> None:
        """
        Append the `get` method expression.

        Parameters
        ----------
        key : _K
            Target key.
        result_value : Any
            Extracted value or a default value.
        default : Any
            Any default value. Basic apysc types (e.g.,
            Int, Number, String, and so on) are necessary.
        """
        import apysc as ap
        from apysc._type import value_util

        key_str: str = value_util.get_value_str_for_expression(value=key)
        if not isinstance(result_value, VariableNameMixIn):
            result_value = AnyValue(value=None)
        result_value_str: str = value_util.get_value_str_for_expression(
            value=result_value
        )
        default_value_str: str = value_util.get_value_str_for_expression(value=default)
        expression: str = (
            f"if ({key_str} in {self.variable_name}) {{"
            f"\n  {result_value_str} = {self.variable_name}[{key_str}];"
            "\n}else {"
            f"\n  {result_value_str} = {default_value_str};"
            "\n}"
        )
        ap.append_js_expression(expression=expression)

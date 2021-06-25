"""Class implementation for dictionary.
"""

from typing import Any
from typing import Dict
from typing import Union

from apysc import Int
from apysc import Number
from apysc import String
from apysc._type.copy_interface import CopyInterface
from apysc._type.dictionary_structure import DictionaryStructure
from apysc._type.revert_interface import RevertInterface

Key = Union[str, int, float, String, Int, Number]


class Dictionary(CopyInterface, RevertInterface, DictionaryStructure):

    _initial_value: Union[Dict[Key, Any], Any]
    _value: Dict[Key, Any]

    def __init__(self, value: Union[Dict[Key, Any], Any]) -> None:
        """
        Dictionary class for apysc library.

        Parameters
        ----------
        value : dict or Dictionary
            Initial dictionary value.
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        from apysc._expression.event_handler_scope import \
            TemporaryNotHandlerScope
        with TemporaryNotHandlerScope():
            TYPE_NAME: str = var_names.DICTIONARY
            self._validate_acceptable_value_type(value=value)
            self._initial_value = value
            self._type_name = TYPE_NAME
            self._value = self._get_dict_value(value=value)
            self.variable_name = expression_variables_util.\
                get_next_variable_name(type_name=TYPE_NAME)
            self._append_constructor_expression()

    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression to file.
        """
        from apysc import append_js_expression
        from apysc._type import value_util
        value_str: str = value_util.get_value_str_for_expression(
            value=self._initial_value)
        expression: str = f'var {self.variable_name} = {value_str};'
        append_js_expression(expression=expression)

    def _get_dict_value(
            self, value: Union[Dict[Key, Any], Any]) -> Dict[Any, Any]:
        """
        Get a dict value from specified value.

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
        return value

    def _validate_acceptable_value_type(
            self, value: Union[Dict[Key, Any], Any]) -> None:
        """
        Validate that specified value is acceptable type or not.

        Parameters
        ----------
        value : dict or Dictionary
            Dictionary value to check.

        Raises
        ------
        TypeError
            If specified value's type is not dict or Dictionary.
        """
        if isinstance(value, (dict, Dictionary)):
            return
        raise TypeError(
            'Not acceptable value type is specified.'
            f'\nSpecified valkue type is: {type(value)}'
            '\nAcceptable types are: dict and Dictionary'
        )

    @property
    def value(self) -> Union[Dict[Key, Any], Any]:
        """
        Get a current dict value.

        Returns
        -------
        value : dict
            Current dict value.
        """
        return self._value

    @value.setter
    def value(self, value: Union[Dict[Key, Any], Any]) -> None:
        """
        Set dictionary value.

        Parameters
        ----------
        value : dict or Dictionary.
            Dictionary value to set.
        """
        self._validate_acceptable_value_type(value=value)
        self._value = self._get_dict_value(value=value)
        self._append_value_setter_expression(value=value)

    def _append_value_setter_expression(
            self, value: Union[Dict[Key, Any], Any]) -> None:
        """
        Append value's setter expression to file.

        Parameters
        ----------
        value : dict or Dictionary.
            Dictionary value to set.
        """
        from apysc import append_js_expression
        from apysc._type import value_util
        value_str: str = value_util.get_value_str_for_expression(value=value)
        expression: str = f'{self.variable_name} = {value_str};'
        append_js_expression(expression=expression)

    _value_snapshot: Dict[str, Dict[Key, Any]]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make values' snapthot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_value_snapshot'):
            self._value_snapshot = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._value_snapshot[snapshot_name] = {**self._value}

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert values if snapshot exists.

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
        return str(self._value)

    def __repr__(self) -> str:
        """
        Get a representation string of this instance.

        Returns
        -------
        repr_str : str
            Representation string of this instance.
        """
        repr_str: str = (
            f'Dictionary({self._value})'
        )
        return repr_str

    @property
    def length(self) -> Int:
        """
        Get length of this dictionary values.

        Returns
        -------
        length : Int
            This dictionary value's length.
        """
        length: Int = Int(len(self._value))
        self._append_length_expression(length=length)
        return length

    def _append_length_expression(self, length: Int) -> None:
        """
        Append length method expression to file.

        Parameters
        ----------
        length : Int
            Created length Int variable.
        """
        from apysc import append_js_expression
        expression: str = (
            f'{length.variable_name} = '
            f'Object.keys({self.variable_name}).length;'
        )
        append_js_expression(expression=expression)

    def __len__(self) -> None:
        """
        This method is disabled and can't use from Dictionary instance.
        """
        raise Exception(
            'Dictionary instance can\'t apply len function.'
            ' Please use length property instead.')

    def __getitem__(self, key: Key) -> Any:
        """
        Get a specified key's single value.

        Parameters
        ----------
        key : Key
            Dictionary key.

        Returns
        -------
        value : *
            Specified key's value.
        """
        from apysc import AnyValue
        self._validate_key_type_is_str_or_numeric(key=key)
        key_: Key = self._get_builtin_type_key(key=key)
        has_key: bool = key_ in self._value
        if has_key:
            value: Any = self._value[key_]
        else:
            value = AnyValue(None)
        self._append_getitem_expression(key=key, value=value)
        return value

    def _get_builtin_type_key(self, key: Key) -> Key:
        """
        Get a built-in type's key (str, int, or float) from
        a specified key.

        Parameters
        ----------
        key : Key
            Target key value (including String, Int, and Number).

        Returns
        -------
        key : str or int or float
            Built-in type's key.
        """
        if isinstance(key, (String, Int, Number)):
            return key._value
        return key

    def _append_getitem_expression(self, key: Key, value: Any) -> None:
        """
        Append __getitem__ expression to file.

        Parameters
        ----------
        key : Key
            Dictionary key.
        value : *
            Specified key's value.
        """
        from apysc import AnyValue
        from apysc import append_js_expression
        from apysc._type import value_util
        from apysc._type.variable_name_interface import VariableNameInterface
        if not isinstance(value, VariableNameInterface):
            value = AnyValue(None)
        key_str: str = value_util.get_value_str_for_expression(value=key)
        expression: str = (
            f'var {value.variable_name} = '
            f'{self.variable_name}[{key_str}];'
        )
        append_js_expression(expression=expression)

    def _validate_key_type_is_str_or_numeric(self, key: Key) -> None:
        """
        Validate whether key value type is acceptable (str or int or
        flaot) or not.

        Parameters
        ----------
        key : Key
            Dictionary key to check.

        Raises
        ------
        ValueError
            If key type is not str, String, int, Int, float, or Number.
        """
        if isinstance(key, (str, String, int, Int, float, Number)):
            return
        raise ValueError(
            f'Unsupported key type is specified: {type(key)}, {key}'
            f'\nSuppoting types are: str, String, int, Int')

    def __setitem__(self, key: Key, value: Any) -> None:
        """
        Set value to a specified key position.

        Parameters
        ----------
        key : Key
            Dictionary key to set value.
        value : *
            Any value to set.
        """
        key_: Key = self._get_builtin_type_key(key=key)
        self._value[key_] = value
        self._append_setitem_expression(key=key, value=value)

    def _append_setitem_expression(self, key: Key, value: Any) -> None:
        """
        Append __setitem__ method expression to file.

        Parameters
        ----------
        key : Key
            Dictionary key to check.
        value : *
            Any value to set.
        """
        from apysc import append_js_expression
        from apysc._type import value_util
        key_str: str = value_util.get_value_str_for_expression(value=key)
        value_str: str = value_util.get_value_str_for_expression(value=value)
        expression: str = (
            f'{self.variable_name}[{key_str}] = {value_str};'
        )
        append_js_expression(expression=expression)

    def __delitem__(self, key: Key) -> None:
        """
        Delete specified key's value from dictionary.

        Parameters
        ----------
        key : Key
            Dictionary key to delete.
        """
        key_: Key = self._get_builtin_type_key(key=key)
        if key_ in self._value:
            del self._value[key_]
        self._append_delitem_expression(key=key)

    def _append_delitem_expression(self, key: Key) -> None:
        """
        Append __delitem__ method expression to file.

        Parameters
        ----------
        key : Key
            Dictionary key to delete.
        """
        from apysc import append_js_expression
        from apysc._type import value_util
        key_str: str = value_util.get_value_str_for_expression(value=key)
        expression: str = (
            f'delete {self.variable_name}[{key_str}];'
        )
        append_js_expression(expression=expression)

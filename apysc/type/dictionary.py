"""Class implementation for dictionary.
"""

from typing import Any, Dict, Union

from apysc.type.copy_interface import CopyInterface
from apysc.type.revert_interface import RevertInterface
from apysc import Int, String

Key = Union[str, int, String, Int]


class Dictionary(CopyInterface, RevertInterface):

    _initial_value: Union[Dict[Key, Any], Any]
    _value: Dict[Key, Any]

    def __init__(self, value: Union[Dict[Key, Any], Any]) -> None:
        """
        Dictionary class for apysc library.

        Parameters
        ----------
        value : dict or Dictionary
            Initial dictionary value.

        Notes
        -----
        - Dictionary keys will be converted from int to str.
        - Only str or int keys are acceptable.
        """
        from apysc.expression import expression_variables_util
        from apysc.expression import var_names
        TYPE_NAME: str = var_names.DICTIONARY
        self._validate_acceptable_value_type(value=value)
        self._validate_all_keys_type_are_str_or_int(value=value)
        value = self._convert_values_key_from_int_to_str(value=value)
        self._initial_value = value
        self._type_name = TYPE_NAME
        self._value = self._get_dict_value(value=value)
        self.variable_name = expression_variables_util.get_next_variable_name(
            type_name=TYPE_NAME)
        self._append_constructor_expression()

    def _convert_values_key_from_int_to_str(
            self, value: Union[Dict[Key, Any], Any]):
        """
        Convert dict keys from int to str.

        Parameters
        ----------
        value : dict or Dictionary
            Dictionary value.
        """
        if isinstance(value, Dictionary):
            return value
        new_dict: Dict[Key, Any] = {}
        for key, value in value.items():
            if isinstance(key, (int, Int)):
                key = str(key)
            new_dict[key] = value
        return new_dict

    def _validate_all_keys_type_are_str_or_int(
            self, value: Union[Dict[Key, Any], Any]) -> None:
        """
        Validate whether all keys type are acceptable (str or int)
        or not.

        Parameters
        ----------
        value : dict or Dictionary
            Dictionary value.
        """
        if isinstance(value, Dictionary):
            return
        for key in value.keys():
            self._validate_key_type_is_str_or_int(key=key)

    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression to file.
        """
        from apysc.expression import expression_file_util
        from apysc.type import value_util
        value_str: str = value_util.get_value_str_for_expression(
            value=self._initial_value)
        expression: str = f'var {self.variable_name} = {value_str};'
        expression_file_util.append_js_expression(expression=expression)

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
        from apysc.expression import expression_file_util
        from apysc.type import value_util
        value_str: str = value_util.get_value_str_for_expression(value=value)
        expression: str = f'{self.variable_name} = {value_str};'
        expression_file_util.append_js_expression(expression=expression)

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

        Parameters
        ----------
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

        Parameters
        ----------
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
        from apysc.expression import expression_file_util
        expression: str = (
            f'{length.variable_name} = '
            f'Object.keys({self.variable_name}).length;'
        )
        expression_file_util.append_js_expression(expression=expression)

    def __len__(self) -> None:
        """
        This method is disabled and can't use from Dictionary instance.
        """
        raise Exception(
            'Dictionary instance can\'t apply len function.'
            ' Please use length property instead.')

    def __getitem__(self, key: Key) -> Any:
        """
        Get a specified key's sinble value.

        Parameters
        ----------
        key : Key
            Dictionary key. If int is specified, that will be
            converted to str.

        Returns
        -------
        value : *
            Specified key's value.
        """
        from apysc import AnyValue
        self._validate_key_type_is_str_or_int(key=key)
        pass

    def _validate_key_type_is_str_or_int(self, key: Key) -> None:
        """
        Validate whether key value type is acceptable (str or int)
        or not.

        Parameters
        ----------
        key : Key
            Dictionary key to check.

        Raises
        ------
        ValueError
            If key type is not str, String, int, and Int.
        """
        if isinstance(key, (str, String, int, Int)):
            return
        raise ValueError(
            f'Unsupported key type is specified: {type(key)}, {key}'
            f'\nSuppoting types are: str, String, int, Int')

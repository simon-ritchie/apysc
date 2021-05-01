"""Class implementation for dictionary.
"""

from typing import Any, Dict, Union

from apysc.type.copy_interface import CopyInterface
from apysc.type.revert_interface import RevertInterface
from apysc import Int


class Dictionary(CopyInterface, RevertInterface):

    _initial_value: Union[Dict[Any, Any], Any]
    _value: Dict[Any, Any]

    def __init__(self, value: Union[Dict[Any, Any], Any]) -> None:
        """
        Dictionary class for apysc library.

        Parameters
        ----------
        value : dict or Dictionary
            Initial dictionary value.
        """
        from apysc.expression import expression_variables_util
        from apysc.expression import var_names
        TYPE_NAME: str = var_names.DICTIONARY
        self._validate_acceptable_value_type(value=value)
        self._initial_value = value
        self._type_name = TYPE_NAME
        self._value = self._get_dict_value(value=value)
        self.variable_name = expression_variables_util.get_next_variable_name(
            type_name=TYPE_NAME)
        self._append_constructor_expression()

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
            self, value: Union[Dict[Any, Any], Any]) -> Dict[Any, Any]:
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
            self, value: Union[Dict[Any, Any], Any]) -> None:
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
    def value(self) -> Union[Dict[Any, Any], Any]:
        """
        Get a current dict value.

        Returns
        -------
        value : dict
            Current dict value.
        """
        return self._value

    @value.setter
    def value(self, value: Union[Dict[Any, Any], Any]) -> None:
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
            self, value: Union[Dict[Any, Any], Any]) -> None:
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

    _value_snapshot: Dict[str, Dict[Any, Any]]

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
        return length

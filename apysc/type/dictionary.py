"""Class implementation for dictionary.
"""

from typing import Any, Dict, Union
from apysc.type.copy_interface import CopyInterface
from apysc.type.revert_interface import RevertInterface


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
        ValueError
            If specified value's type is not dict or Dictionary.
        """
        if isinstance(value, (dict, Dictionary)):
            return
        raise ValueError(
            'Not acceptable value type is specified.'
            f'\nSpecified valkue type: {type(value)}'
            '\nAcceptable types: dict and Dictionary'
        )

    def _make_snapshot(self, snapshot_name: str) -> None:
        pass

    def _revert(self, snapshot_name: str) -> None:
        pass

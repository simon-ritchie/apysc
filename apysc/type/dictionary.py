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
        self._validate_acceptable_value_type(value=value)
        pass

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

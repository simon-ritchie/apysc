"""Validation interfaces for the handler's options argument.
"""

import inspect
from inspect import Signature
from typing import Any
from typing import Dict
from typing import List

from typing_extensions import TypedDict

from apysc._event.handler import Handler


def validate_options(handler: Handler, options: Any) -> None:
    """
    Validate handler's optional argument dictionary type.

    Parameters
    ----------
    handler : Handler
        Target handler.
    options : dict or None
        Optional argument dictionary.
    """
    if options is None:
        return
    _validate_dict_type(options=options)
    handler_arg_data_list: List[_ArgData] = _get_handler_arg_data_list(
        handler=handler)
    _validate_arg_names(handler_arg_data_list=handler_arg_data_list)
    _validate_typed_dict(
        handler_arg_data_list=handler_arg_data_list, options=options)


class _ArgData(TypedDict):
    arg_name: str
    annotation: Any


class _HandlerArgumentsLengthError(Exception):
    pass


class _HandlerFirstArgumentNameError(Exception):
    pass


class _HandlerSecondArgumentNameError(Exception):
    pass


class _TypedDictOptionsTypeMismatchError(Exception):
    pass


def _validate_typed_dict(
        handler_arg_data_list: List[_ArgData],
        options: Dict[Any, Any]) -> None:
    """
    Validate a TypedDict options values.

    Notes
    -----
    If the handler's annotation is not the type of the TypedDict,
    then validation will be skipped.

    Parameters
    ----------
    handler_arg_data_list : list of _ArgData
        Target handler's arguments data list.
    options : dict
        Optional arguments dictionary.
    """
    if not _is_typed_dict_options_arg(
            handler_arg_data_list=handler_arg_data_list):
        return
    typed_dict_annotation: Any = \
        _get_options_annotation_from_handler_arg_data_list(
            handler_arg_data_list=handler_arg_data_list)
    annotations_dict: Dict[str, Any] = typed_dict_annotation.__annotations__
    for key, annotation in annotations_dict.items():
        if key not in options:
            raise _TypedDictOptionsTypeMismatchError(
                f'There is no options dictionary key: {key}'
                "\nPlease check a handler's options argument type "
                'annotations and an actual options value.'
                f"\nHandler's options annotation: {annotations_dict}"
                f'\nActual options value: {options}')
        if not inspect.isclass(annotation):
            continue
        if not isinstance(options[key], annotation):
            raise _TypedDictOptionsTypeMismatchError(
                f'There is a options value type mismatch.'
                f'\nOptions key name: {key}'
                "\nExpected type (based on handler's annotation): "
                f'{annotation}'
                f'\nActual value type: {type(options[key])}'
                f'\nActual options value: {options}')


def _get_options_annotation_from_handler_arg_data_list(
        handler_arg_data_list: List[_ArgData]) -> Any:
    """
    Get a options' annotation value from a specified handler's
    argument data list.

    Parameters
    ----------
    handler_arg_data_list : list of _ArgData
        Target handler's arguments data list.

    Returns
    -------
    annotation : Any
        Options' annotation value.
    """
    annotation: Any = handler_arg_data_list[1]['annotation']
    return annotation


def _is_typed_dict_options_arg(
        handler_arg_data_list: List[_ArgData]) -> bool:
    """
    Get a boolean value whether the options argument is the
    TypedDict or not.

    Parameters
    ----------
    handler_arg_data_list : list of _ArgData
        Target handler's arguments data list.

    Returns
    -------
    result : bool
        If the options argument is the TypedDict, then True will
        be returned.
    """
    annotation: Any = _get_options_annotation_from_handler_arg_data_list(
        handler_arg_data_list=handler_arg_data_list)
    annotation_str: str = str(annotation)
    annotation_str = annotation_str.lower()
    if 'typeddict' in annotation_str:
        return True
    return False


def _validate_arg_names(handler_arg_data_list: List[_ArgData]) -> None:
    """
    Validate handler's argument names and order of arguments.

    Parameters
    ----------
    handler_arg_data_list : list of _ArgData
        Target handler's arguments data list.

    Raises
    ------
    _HandlerArgumentsLengthError
        If a specified arguments length is invalid.
    _HandlerFirstArgumentNameError
        If a specified first argument name is not 'e'.
    _HandlerSecondArgumentNameError
        If a specified second argument name is not 'options'.
    """
    expected_length: int = 2
    actual_length: int = len(handler_arg_data_list)
    if actual_length != expected_length:
        raise _HandlerArgumentsLengthError(
            'Passed handler arguments length is invalid.'
            f'\nExpected length: {expected_length}, passed: {actual_length}')

    first_arg_name: str = handler_arg_data_list[0]['arg_name']
    expected_name: str = 'e'
    if first_arg_name != expected_name:
        raise _HandlerFirstArgumentNameError(
            "Passed handler's first argument name is invalid."
            f'\nExpected argument name: {expected_name}, '
            f'actual: {first_arg_name}')

    second_arg_name: str = handler_arg_data_list[1]['arg_name']
    expected_name = 'options'
    if second_arg_name != expected_name:
        raise _HandlerSecondArgumentNameError(
            "Passed handler's second argument name is invalid."
            f'\nExpected argument name: {expected_name}, '
            f'actual: {second_arg_name}')


def _get_handler_arg_data_list(handler: Handler) -> List[_ArgData]:
    """
    Get a handler's argument(s) data list.

    Parameters
    ----------
    handler : Handler
        Target handler.

    Returns
    -------
    handler_arg_data_list : list of _ArgData
        Argument(s) data list.
    """
    signature: Signature = inspect.signature(handler)
    handler_arg_data_list: List[_ArgData] = []
    for arg_name, parameter in signature.parameters.items():
        handler_arg_data_list.append({
            'arg_name': arg_name,
            'annotation': parameter.annotation,
        })
    return handler_arg_data_list


def _validate_dict_type(options: Any) -> None:
    """
    Validate whether a specified value is dictionary type or not.

    Parameters
    ----------
    options : dict
        Optional argument dictionary.

    Raises
    ------
    TypeError
        If a specified value is not a dictionary type one.
    """
    if isinstance(options, dict):
        return
    raise TypeError(
        'Specified options argument is not dict type or None: '
        f'{type(options)}, {options}')

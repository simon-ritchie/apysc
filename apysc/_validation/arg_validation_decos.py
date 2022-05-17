"""This module is for the argument validations' decorators.
"""

import functools
from typing import Any, Dict, List, Type
from typing import Callable
from typing import Optional
from typing import TypeVar
from typing import Union
from inspect import Signature
import inspect

# pyright: reportInvalidTypeVarUse=false
_F = TypeVar('_F', bound=Callable)


def _extract_arg_value(
        *, args: Any, kwargs: Dict[str, Any],
        arg_position_index: int, arg_name: str) -> Any:
    """
    Extract an argument value from a specified arguments' dictionary
    or list.

    Parameters
    ----------
    args : List[Any]
        A specified positional arguments' list.
    kwargs : Dict[str, Any]
        A specified keyword arguments' dictionary.'
    arg_position_index : int
        A target argument position index.
    arg_name : str
        A target argument name to check.

    Returns
    -------
    value : Any
        An extracted any value.
    """
    value: Any = None
    if arg_name in kwargs:
        value = kwargs[arg_name]
    elif len(args) - 1 >= arg_position_index:
        value = args[arg_position_index]
    return value


def _get_arg_name_by_index(
        *, func: Callable, arg_position_index: int) -> str:
    """
    Get an argument name from a specified argument position index.

    Parameters
    ----------
    func : Callable
        A target function (or method).
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    arg_name : str
        A target argument name.
    """
    signature: Signature = inspect.signature(func)
    if len(signature.parameters) -1 < arg_position_index:
        raise IndexError(
            'A specified function has no argument parameter '
            f'at the index of {arg_position_index}'
            f'\nActual argument length: {len(signature.parameters)}')
    arg_name: str = ''
    for i, (arg_name_, _) in enumerate(signature.parameters.items()):
        if i == arg_position_index:
            arg_name = arg_name_
    return arg_name


def not_empty_string(
        *, arg_position_index: int, arg_name: str) -> _F:
    """
    Set the validation to check that a specified argument's string
    is not empty.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.
    arg_name : str
        A target argument name to check.

    Returns
    -------
    _wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(func: _F) -> _F:
        """
        Wrapping function for a decorator setting.

        Parameters
        ----------
        func : Callable
            A target function or method to wrap.

        Returns
        -------
        inner_wrapped : Callable
            Wrapped callable object.
        """

        @functools.wraps(func)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            """
            Wrapping function for a decorator setting.

            Parameters
            ----------
            *args : list
                Target positional arguments.
            **kwargs : dict
                Target keyword arguments.

            Returns
            -------
            result : Any
                A return value(s) of a callable execution result.
            """
            from apysc._type.string import String
            from apysc._validation.string_validation import \
                validate_not_empty_string
            string: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, arg_name=arg_name)

            if string is not None:
                validate_not_empty_string(
                    string=string,
                    additional_err_msg=(
                        'An argument\'s string value must not be empty.'
                        f'\nTarget callable name: {func.__name__}'
                        f'\nTarget argument name: {arg_name}'
                    ))
            result: Any = func(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def handler_args_num(
        *, arg_position_index: int, arg_name: str) -> _F:
    """
    Set the validation to check specified handler argument's
    number.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.
    arg_name : str
        A target argument name to validate.

    Returns
    -------
    _wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(func: _F) -> _F:
        """
        Wrapping function for a decorator setting.

        Parameters
        ----------
        func : Callable
            A target function or method to wrap.

        Returns
        -------
        inner_wrapped : Callable
            Wrapped callable object.
        """

        @functools.wraps(func)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            """
            Wrapping function for a decorator setting.

            Parameters
            ----------
            *args : list
                Target positional arguments.
            **kwargs : dict
                Target keyword arguments.

            Returns
            -------
            result : Any
                A return value(s) of a callable execution result.
            """
            from apysc._validation.handler_validation import \
                validate_handler_args_num
            handler: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index,
                arg_name=arg_name)
            if handler is not None:
                validate_handler_args_num(
                    handler=handler,
                    additional_err_msg=(
                        f'Target callable name: {func.__name__}'
                        f'\nTarget argument name: {arg_name}'
                    ))
            result: Any = func(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def handler_options_type(
        *, arg_position_index: int, arg_name: str) -> _F:
    """
    Set the validation to check a specified handler-options
    argument's type.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.
    arg_name : str
        A target argument name to validate.

    Returns
    -------
    _wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(func: _F) -> _F:
        """
        Wrapping function for a decorator setting.

        Parameters
        ----------
        func : Callable
            A target function or method to wrap.

        Returns
        -------
        inner_wrapped : Callable
            Wrapped callable object.
        """

        @functools.wraps(func)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            """
            Wrapping function for a decorator setting.

            Parameters
            ----------
            *args : list
                Target positional arguments.
            **kwargs : dict
                Target keyword arguments.

            Returns
            -------
            result : Any
                A return value(s) of a callable execution result.
            """
            from apysc._validation.handler_validation import \
                validate_options_type
            options: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, arg_name=arg_name)
            validate_options_type(
                options=options,
                additional_err_msg=(
                    f'\nTarget callable name: {func.__name__}'
                    f'\nTarget argument name: {arg_name}'
                ))

            result: Any = func(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore

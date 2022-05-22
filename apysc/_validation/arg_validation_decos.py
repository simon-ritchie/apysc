"""This module is for the argument validations' decorators.

Mainly the following decorators exist.

- not_empty_string
    - Set the validation to check that a specified argument's string
        is not empty.
- handler_args_num
    - Set the validation to check a specified handler argument's
        number.
- handler_options_type
    - Set the validation to check a specified handler-options
        argument's type.
- is_num
    - Set the validation to check a specified argument's type
        is the number-related type.
- is_integer
    - Set the validation to check a specified argument's type
        is the `int` or `ap.Int`.
- num_is_gt_zero
    - Set the validation to check that a specified argument's value
        is greater than zero.
- num_is_gte_zero
    - Set the validation to check that a specified argument's value
        is greater than or equal to zero.
- num_is_0_to_1_range
    - Set the validation to check that a specified argument's value
        is 0.0 to 1.0 range.
- is_easing
    - Set the validation to check a specified argument's type
        is the `ap.Easing`.
- is_hex_color_code_format
    - Set the validation to check a specified argument's value
        is a hexadecimal color code format.
"""

import functools
import inspect
from inspect import Signature
from typing import Any
from typing import Callable
from typing import Dict
from typing import TypeVar

# pyright: reportInvalidTypeVarUse=false
_F = TypeVar('_F', bound=Callable)


def _extract_arg_value(
        *, args: Any, kwargs: Dict[str, Any],
        arg_position_index: int,
        callable_: Callable) -> Any:
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
    callable_ : Callable
        A target function or method.

    Returns
    -------
    value : Any
        An extracted any value.
    """
    value: Any = None
    arg_name: str = _get_arg_name_by_index(
        callable_=callable_, arg_position_index=arg_position_index)
    default_val: Any = _get_default_val_by_arg_name(
        callable_=callable_, arg_name=arg_name)
    if arg_name in kwargs:
        value = kwargs[arg_name]
    elif len(args) - 1 >= arg_position_index:
        value = args[arg_position_index]
    if value is None and default_val is not None:
        return default_val
    return value


def _get_arg_name_by_index(
        *, callable_: Callable, arg_position_index: int) -> str:
    """
    Get an argument name from a specified argument position index.

    Parameters
    ----------
    callable_ : Callable
        A target function or method.
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    arg_name : str
        A target argument name.
    """
    signature: Signature = inspect.signature(callable_)
    if len(signature.parameters) - 1 < arg_position_index:
        raise IndexError(
            'A specified function has no argument parameter '
            f'at the index of {arg_position_index}'
            f'\nActual argument length: {len(signature.parameters)}')
    arg_name: str = ''
    for i, (arg_name_, _) in enumerate(signature.parameters.items()):
        if i == arg_position_index:
            arg_name = arg_name_
    return arg_name


def _get_callable_and_arg_names_msg(
        *, callable_: Callable, arg_position_index: int) -> str:
    """
    Get a function or method and argument names' message
    for an additional error message.

    Parameters
    ----------
    callable_ : Callable
        A target function or method.
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    callable_and_arg_names_msg : str
        A function or method and argument names' message.
    """
    arg_name: str = _get_arg_name_by_index(
        callable_=callable_, arg_position_index=arg_position_index)
    callable_and_arg_names_msg: str = (
        f'Target callable name: {callable_.__name__}'
        f'\nTarget argument name: {arg_name}'
    )
    return callable_and_arg_names_msg


def _get_default_val_by_arg_name(
        *, callable_: Callable, arg_name: str) -> Any:
    """
    Get a default value of a given name's argument.

    Parameters
    ----------
    callable_ : Callable
        A target function or method.
    arg_name : str
        A target argument name.

    Returns
    -------
    default_val : Any
        A default value of a given name's argument.
    """
    default_val: Any = None
    signature: Signature = inspect.signature(callable_)
    for target_arg_name, parameter in signature.parameters.items():
        if target_arg_name != arg_name:
            continue
        default_val = parameter.default
        break
    if default_val == inspect.Signature.empty:
        return None
    return default_val


def not_empty_string(*, arg_position_index: int) -> _F:
    """
    Set the validation to check that a specified argument's string
    is not empty.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _F) -> _F:
        """
        Wrapping function for a decorator setting.

        Parameters
        ----------
        callable_ : Callable
            A target function or method to wrap.

        Returns
        -------
        inner_wrapped : Callable
            Wrapped callable object.
        """

        @functools.wraps(callable_)
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
            from apysc._validation.string_validation import \
                validate_not_empty_string
            string: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_not_empty_string(
                string=string,
                additional_err_msg=(
                    'An argument\'s string value must not be empty.'
                    f'\n{callable_and_arg_names_msg}'
                ))
            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def handler_args_num(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified handler argument's
    number.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _F) -> _F:
        """
        Wrapping function for a decorator setting.

        Parameters
        ----------
        callable_ : Callable
            A target function or method to wrap.

        Returns
        -------
        inner_wrapped : Callable
            Wrapped callable object.
        """

        @functools.wraps(callable_)
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
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_handler_args_num(
                handler=handler,
                additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def handler_options_type(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified handler-options
    argument's type.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _F) -> _F:
        """
        Wrapping function for a decorator setting.

        Parameters
        ----------
        callable_ : Callable
            A target function or method to wrap.

        Returns
        -------
        inner_wrapped : Callable
            Wrapped callable object.
        """

        @functools.wraps(callable_)
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
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_options_type(
                options=options,
                additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_num(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified argument's type
    is the number-related type.

    Parameters
    ----------
    arg_position_index : int
        _description_

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _F) -> _F:
        """
        Wrapping function for a decorator setting.

        Parameters
        ----------
        callable_ : Callable
            A target function or method to wrap.

        Returns
        -------
        inner_wrapped : Callable
            Wrapped callable object.
        """

        @functools.wraps(callable_)
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
            from apysc._validation.number_validation import validate_num
            num: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_num(
                num=num,
                additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_integer(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified argument's type
    is the `int` or `ap.Int`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _F) -> _F:
        """
        Wrapping function for a decorator setting.

        Parameters
        ----------
        callable_ : Callable
            A target function or method to wrap.

        Returns
        -------
        inner_wrapped : Callable
            Wrapped callable object.
        """

        @functools.wraps(callable_)
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
            from apysc._validation.number_validation import validate_integer
            integer: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_integer(
                integer=integer,
                additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def num_is_gt_zero(*, arg_position_index: int) -> _F:
    """
    Set the validation to check that a specified argument's value
    is greater than zero.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _F) -> _F:
        """
        Wrapping function for a decorator setting.

        Parameters
        ----------
        callable_ : Callable
            A target function or method to wrap.

        Returns
        -------
        inner_wrapped : Callable
            Wrapped callable object.
        """

        @functools.wraps(callable_)
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
            from apysc._validation.number_validation import \
                validate_num_is_gt_zero
            num: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_num_is_gt_zero(
                num=num, additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def num_is_gte_zero(*, arg_position_index: int) -> _F:
    """
    Set the validation to check that a specified argument's value
    is greater than or equal to zero.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _F) -> _F:
        """
        Wrapping function for a decorator setting.

        Parameters
        ----------
        callable_ : Callable
            A target function or method to wrap.

        Returns
        -------
        inner_wrapped : Callable
            Wrapped callable object.
        """

        @functools.wraps(callable_)
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
            from apysc._validation.number_validation import \
                validate_num_is_gte_zero
            num: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_num_is_gte_zero(
                num=num, additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def num_is_0_to_1_range(*, arg_position_index: int) -> _F:
    """
    Set the validation to check that a specified argument's value
    is 0.0 to 1.0 range.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _F) -> _F:
        """
        Wrapping function for a decorator setting.

        Parameters
        ----------
        callable_ : Callable
            A target function or method to wrap.

        Returns
        -------
        inner_wrapped : Callable
            Wrapped callable object.
        """

        @functools.wraps(callable_)
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
            from apysc._validation.number_validation import \
                validate_num_is_0_to_1_range
            num: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_num_is_0_to_1_range(
                num=num, additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_easing(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified argument's type
    is the `ap.Easing`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _F) -> _F:
        """
        Wrapping function for a decorator setting.

        Parameters
        ----------
        callable_ : Callable
            A target function or method to wrap.

        Returns
        -------
        inner_wrapped : Callable
            Wrapped callable object.
        """

        @functools.wraps(callable_)
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
            import apysc as ap
            easing: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            if not isinstance(easing, ap.Easing):
                raise TypeError(
                    'A specified easing argument\'s type is not the '
                    f'ap.Easing: {type(easing)}'
                    f'\n{callable_and_arg_names_msg}')

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_hex_color_code_format(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified argument's value
    in a hexadecimal color code format.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _F) -> _F:
        """
        Wrapping function for a decorator setting.

        Parameters
        ----------
        callable_ : Callable
            A target function or method to wrap.

        Returns
        -------
        inner_wrapped : Callable
            Wrapped callable object.
        """

        @functools.wraps(callable_)
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
            from apysc._color import color_util
            from apysc._validation.color_validation import \
                validate_hex_color_code_format
            hex_color_code: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            hex_color_code = color_util.remove_color_code_sharp_symbol(
                hex_color_code=hex_color_code)
            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_hex_color_code_format(
                hex_color_code=hex_color_code,
                additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore

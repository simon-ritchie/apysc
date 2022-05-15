"""This module is for the argument validations' decorators.
"""

import functools
from typing import Any
from typing import Callable
from typing import TypeVar
from typing import Union

# pyright: reportInvalidTypeVarUse=false
_F = TypeVar('_F', bound=Callable)


def not_empty_string(*, arg_name: str) -> _F:
    """
    Set the validation to check a specified argument's string
    is not empty.

    Notes
    -----
    This decorator function checks when a code passes an argument
    as a keyword argument.


    Parameters
    ----------
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
            if arg_name in kwargs:
                string: Union[str, String] = kwargs.get(arg_name, '')
                validate_not_empty_string(string=string)
            result: Any = func(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore

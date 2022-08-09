"""This module is for the handler interfaces'
validation implementations.
"""

import inspect
from inspect import Signature
import re
from typing import Any, Optional
from typing import Callable
from typing import List


def validate_options_type(*, options: Any, additional_err_msg: str = "") -> None:
    """
    Validate a specified options type.

    Parameters
    ----------
    options : Any
        Target options value.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    TypeError
        If a specified options type is not the dictionary or None.
    """
    if options is None:
        return
    if isinstance(options, dict):
        return
    if additional_err_msg != "":
        additional_err_msg = f"\n{additional_err_msg}"
    raise TypeError(
        f"Handler's options argument must be a dictionary: {type(options)}"
        f"\n{options}{additional_err_msg}"
    )


def validate_handler_args_num(
    *, handler: Callable, additional_err_msg: str = ""
) -> None:
    """
    Validate specified handler's arguments number.

    Parameters
    ----------
    handler : Callable
        A target handler to validate.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        - If handler's arguments number is not 2.
    TypeError
        - If a specified handler is not callable.
    """
    if not callable(handler):
        raise TypeError(
            "A specified handler's argument is not callable: " f"{type(handler)}"
        )
    signature: Signature = inspect.signature(obj=handler)
    args_num: int = 0
    skipping_arg_names: List[str] = ["*", "**", "self", "cls"]
    arg_names: List[str] = []
    for parameter in signature.parameters:
        if parameter in skipping_arg_names:
            continue
        args_num += 1
        arg_names.append(parameter)
    if args_num != 2:
        if additional_err_msg != "":
            additional_err_msg = f"\n{additional_err_msg}"
        raise ValueError(
            "A specified handler's arguments number must be 2 "
            f"(actual: {args_num})"
            f"\nTarget argument names: {arg_names}"
            "\n\nThe first argument becomes event instance and the second "
            "one becomes the handler's option parameters."
            f"{additional_err_msg}"
        )


def validate_in_handler_substitution(*, handler: Callable) -> None:
    """
    Validate whether there isn't substitution of the basic type values
    (e.g., ap.Int, ap.String) in a specified handler's source.

    Parameters
    ----------
    handler : Callable
        A target handler's callable object.
    """
    source: str = inspect.getsource(handler)
    source = _remove_handlers_name_and_args_from_source(
        source=source)
    source = _remove_docstring_from_source(docstring=handler.__doc__, source=source)
    pass


def _remove_docstring_from_source(*, docstring: Optional[str], source: str) -> str:
    """
    Remove a docstring from a specified source code string.

    Parameters
    ----------
    docstring : Optional[str]
        A handler's docstring.
    source : str
        A handler's source code string.

    Returns
    -------
    source : str
        A result source code string.
    """
    if docstring is None:
        return source
    source = source.replace(docstring, "", 1)
    while source.lstrip().startswith('"""'):
        source = source.replace('"""', "", 1)
    while source.lstrip().startswith("'''"):
        source = source.replace("'''", "", 1)
    source = re.sub(
        pattern=r'^ *?\n', repl='', string=source, count=1,
        flags=re.DOTALL)
    source = source.rstrip()
    return source


def _remove_handlers_name_and_args_from_source(*, source: str) -> str:
    """
    Remove a handler's keyword, name, arguments, and return values
    type annotations from a specified source string.

    Parameters
    ----------
    source : str
        A source string.

    Returns
    -------
    source : str
        A result source string.
    """
    source = re.sub(
        pattern=r"def .+?\(.*?\).*?\:\n",
        repl='', string=source, count=1,
        flags=re.MULTILINE | re.DOTALL)
    return source

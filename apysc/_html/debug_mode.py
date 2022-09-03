"""This module is for the HTML and JavaScript debugging-mode
setting interface implementations.
"""

import functools
import inspect
from inspect import Signature
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union

from typing_extensions import final

from apysc._expression.indent_num import Indent


def set_debug_mode() -> None:
    """
    Set the debug mode for the HTML and JavaScript debugging.
    If calling this function, this interface applies
    the following setting:
    - Disabling HTML minify setting.
    - Changing to append per each interface JavaScript divider string.

    References
    ----------
    - set_debug_mode interface
        - https://simon-ritchie.github.io/apysc/en/set_debug_mode.html

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> ap.set_debug_mode()
    >>> int_val: ap.Int = ap.Int(10)
    """
    from apysc._expression import expression_data_util

    table_name: str = expression_data_util.TableName.DEBUG_MODE_SETTING.value
    query: str = f"DELETE FROM {table_name};"
    expression_data_util.exec_query(sql=query, commit=False)
    query = f"INSERT INTO {table_name}(is_debug_mode) VALUES(1);"
    expression_data_util.exec_query(sql=query)


def unset_debug_mode() -> None:
    """
    Unset the debug mode for the HTML and JavaScript debugging.

    References
    ----------
    - unset_debug_mode interface
        - https://simon-ritchie.github.io/apysc/en/unset_debug_mode.html

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> ap.set_debug_mode()
    >>> int_val: ap.Int = ap.Int(10)
    >>> ap.unset_debug_mode()
    """
    from apysc._expression import expression_data_util

    table_name: str = expression_data_util.TableName.DEBUG_MODE_SETTING.value
    query: str = f"DELETE FROM {table_name};"
    expression_data_util.exec_query(sql=query)


def is_debug_mode() -> bool:
    """
    Get a boolean value whether the current debug mode is enabled or not.

    Returns
    -------
    result : bool
        If the current debug mode is enabled, this interface
        returns True.

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> ap.set_debug_mode()
    >>> ap.is_debug_mode()
    True

    >>> int_val: ap.Int = ap.Int(10)
    >>> ap.unset_debug_mode()
    >>> ap.is_debug_mode()
    False
    """
    from apysc._expression import expression_data_util

    table_name: str = expression_data_util.TableName.DEBUG_MODE_SETTING.value
    query: str = f"SELECT is_debug_mode FROM {table_name} LIMIT 1;"
    expression_data_util.exec_query(sql=query)
    result_: Optional[Tuple[int]] = expression_data_util.cursor.fetchone()
    if result_ is None:
        return False
    result: bool = bool(result_[0])
    return result


def _get_callable_str(*, callable_: Union[Callable, str]) -> str:
    """
    Get a callable string (label).

    Parameters
    ----------
    callable_ : Callable or str
        Target function or method or property or dunder method name.

    Returns
    -------
    callable_str : str
        A callable string (label).
    """
    if isinstance(callable_, str):
        callable_str: str = callable_
    else:
        callable_str = callable_.__name__
    return callable_str


def _get_callable_path_name(
    *,
    callable_: Union[Callable, str],
    module_name: str,
    class_: Optional[Union[Type, str]] = None,
) -> str:
    """
    Get a specified callable count data path name.

    Parameters
    ----------
    callable_ : Callable or str
        Target function or method or property or dunder method name.
    module_name : str
        Module name. This value needs to set the `__name__` value.
    class_ : Type or str or None, optional
        Target class type or type name. If the target callable_
        variable is not a method, this interface ignores this argument.

    Returns
    -------
    path_name : str
        Target path name.
    """
    module_path: str = module_name.replace(".", "_")
    if class_ is None:
        class_name: str = ""
    elif inspect.isclass(class_):
        class_name_: str = getattr(class_, "__name__")
        class_name = f"_{class_name_}"
    else:
        class_name = f"_{class_}"
    callable_str: str = _get_callable_str(callable_=callable_)
    path_name: str = f"{module_path}{class_name}_{callable_str}"
    return path_name


def _get_callable_count(
    *,
    callable_: Union[Callable, str],
    module_name: str,
    class_: Optional[Union[Type, str]] = None,
) -> int:
    """
    Get a specified callable count number.

    Parameters
    ----------
    callable_ : Callable or str
        Target function or method or property or dunder method name.
    module_name : str
        Module name. This value needs to set the `__name__` value.
    class_ : Type or str or None, optional
        Target class type or type name. If the target callable_
        variable is not a method, this interface ignores this argument.

    Returns
    -------
    callable_count : int
        Target count number.
    """
    from apysc._expression import expression_data_util

    path_name: str = _get_callable_path_name(
        callable_=callable_, module_name=module_name, class_=class_
    )
    table_name: str = expression_data_util.TableName.DEBUG_MODE_CALLABLE_COUNT.value
    query: str = (
        f"SELECT count FROM {table_name} " f"WHERE name = '{path_name}' LIMIT 1;"
    )
    expression_data_util.exec_query(sql=query)
    result: Optional[Tuple[int]] = expression_data_util.cursor.fetchone()
    if result is None:
        return 0
    return result[0]


def _increment_callable_count(
    *,
    callable_: Union[Callable, str],
    module_name: str,
    class_: Optional[Union[Type, str]] = None,
) -> None:
    """
    Increment a specified callable count number.

    Parameters
    ----------
    callable_ : Callable or str
        Target function or method or property or dunder method name.
    module_name : str
        Module name. This value needs to set the `__name__` value.
    class_ : Type or str or None, optional
        Target class type or type name. If the target callable_
        variable is not a method, this interface ignores this argument.
    """
    from apysc._expression import expression_data_util

    callable_count: int = _get_callable_count(
        callable_=callable_, module_name=module_name, class_=class_
    )
    callable_count += 1
    path_name: str = _get_callable_path_name(
        callable_=callable_, module_name=module_name, class_=class_
    )
    table_name: str = expression_data_util.TableName.DEBUG_MODE_CALLABLE_COUNT.value
    query: str = f"DELETE FROM {table_name} " f"WHERE name = '{path_name}';"
    expression_data_util.exec_query(sql=query, commit=False)
    query = (
        f"INSERT INTO {table_name}(name, count) "
        f"VALUES ('{path_name}', {callable_count});"
    )
    expression_data_util.exec_query(sql=query)


class DebugInfo:
    """
    Save debugging information (append callable interface
    name comment and arguments information) to the
    JavaScript expression file. The apysc uses this
    class at the `with` statement.

    Notes
    -----
    If the debug mode setting is not enabled, the apysc
    skips the saving.
    """

    _callable: Union[Callable, str]
    _module_name: str
    _args: List[Any]
    _kwargs: Dict[str, Any]
    _class_name: Optional[str]
    _DIVIDER: str = "/" * 70
    _callable_count: int
    _indent: Indent

    @final
    def __init__(
        self,
        *,
        callable_: Union[Callable, str],
        args: List[Any],
        kwargs: Dict[str, Any],
        module_name: str,
        class_name: Optional[str] = None,
    ) -> None:
        """
        Save debug information (append callable interface
        name comment and arguments information) to the
        JavaScript expression file. This class needs
        to use the `with` statement when instantiating.

        Notes
        -----
        If the debug mode setting is not enabled,
        this interface skips the saving.

        Parameters
        ----------
        callable_ : Callable or str
            Target function or method or property or dunder method name.
        args : list
            Function positional arguments.
        kwargs : dict
            Function keyword arguments.
        module_name : str
            Module name. This value requires the `__name__` value.
        class_name : str or None, optional
            Target class type name. If the target
            callable_ variable is not a method, this
            interface ignores this argument.
        """
        self._callable = callable_
        self._args = args
        self._kwargs = kwargs
        self._module_name = module_name
        self._class_name = class_name
        _increment_callable_count(
            callable_=callable_, module_name=module_name, class_=class_name
        )
        self._callable_count = _get_callable_count(
            callable_=callable_, module_name=module_name, class_=class_name
        )
        self._indent = Indent()

    @final
    def _get_class_info(self) -> str:
        """
        Get a class information string.

        Returns
        -------
        class_info : str
            Target class information string.
        """
        if self._class_name is None:
            class_info: str = ""
        else:
            class_info = f"\n// class: {self._class_name}"
        return class_info

    @final
    def __enter__(self) -> None:
        """
        This class uses this method at the start of the
        with-block.
        """
        import apysc as ap

        if not ap.is_debug_mode():
            return
        class_info: str = self._get_class_info()
        arguments_info: str = ""
        if self._args:
            arguments_info += f"\n// Positional arguments: {self._args}"
        if self._kwargs:
            arguments_info += f"\n// Keyword arguments: {self._kwargs}"
        callable_str: str = _get_callable_str(callable_=self._callable)
        expression: str = (
            f"{self._DIVIDER}"
            f"\n// [{callable_str} {self._callable_count}] "
            "started."
            f"\n// module name: {self._module_name}"
            f"{class_info}"
            f"{arguments_info}"
        )
        ap.append_js_expression(expression=expression)
        self._indent.__enter__()

    @final
    def __exit__(self, *args: Any) -> None:
        """
        This class uses this method at the end of the with-block.

        Parameters
        ----------
        *args : list
            Positional arguments.
        """
        import apysc as ap

        if not ap.is_debug_mode():
            return
        class_info: str = self._get_class_info()
        callable_str: str = _get_callable_str(callable_=self._callable)
        expression: str = (
            f"// [{callable_str} {self._callable_count}] ended."
            f"\n// module name: {self._module_name}"
            f"{class_info}"
            f"\n{self._DIVIDER}"
        )
        self._indent.__exit__()
        ap.append_js_expression(expression=expression)


# pyright: reportInvalidTypeVarUse=false
_F = TypeVar("_F", bound=Callable)


def add_debug_info_setting(*, module_name: str) -> _F:
    """
    Set a debug information setting to a target
    callable object (decorator function).

    Parameters
    ----------
    module_name : str
        A target module name.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.

    Notes
    -----
    Currently, this interface raises a mypy error under
    some mypy settings. Please set `type: ignore[misc]` comment
    or `--disable-error-code misc` mypy's command argument
    if encountered its mypy error.

    Examples
    --------
    >>> import apysc as ap
    >>> @ap.add_debug_info_setting(module_name=__name__)  # type: ignore[misc]
    ... def sample_method(a: int) -> None:
    ...     ...
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
            class_name: Optional[str] = None
            signature: Signature = inspect.signature(func)
            if len(signature.parameters) != 0:
                first_arg_name: str = list(signature.parameters.keys())[0]
                if first_arg_name == "self":
                    first_arg_value: Any = args[0]
                    class_name = type(first_arg_value).__name__
                elif first_arg_name == "cls":
                    first_arg_value = args[0]
                    class_name = first_arg_value.__name__

            with DebugInfo(
                callable_=func,
                args=list(args),
                kwargs=kwargs,
                module_name=module_name,
                class_name=class_name,
            ):
                result: Any = func(*args, **kwargs)
                return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore

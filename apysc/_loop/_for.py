"""This module is for the `For` loop class implementation.
"""

from typing import Any
from typing import Dict
from typing import Generic
from typing import Optional
from typing import TypeVar
from typing import Union

from typing_extensions import final

from apysc._expression.indent_num import Indent
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.array import Array
from apysc._type.dictionary import Dictionary
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String

_Target = TypeVar("_Target", Int, String, Number)


class For(Generic[_Target]):
    """
    A class to append for the (loop) expression.

    References
    ----------
    - For
        - https://simon-ritchie.github.io/apysc/en/for.html

    Examples
    --------
    >>> import apysc as ap
    >>> arr: ap.Array = ap.Array(range(3))
    >>> with ap.For(arr) as i:
    ...     ap.trace("Loop index is:", i)
    ...
    """

    _arr_or_dict: Union[Array, Dictionary]
    _locals: Dict[str, Any]
    _globals: Dict[str, Any]
    _snapshot_name: str
    _indent: Indent

    @final
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        arr_or_dict: Union[Array, Dictionary],
        *,
        locals_: Optional[Dict[str, Any]] = None,
        globals_: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        A class to append for the (loop) expression.

        Parameters
        ----------
        arr_or_dict : Array or Dictionary
            Array or Dictionary instance to iterate.
        locals_ : dict or None, default None
            Current scope's local variables. Set locals()
            value to this argument. If specified, this interface
            reverts all local scope VariableNameMixIn
            variables (like Int, Sprite) at the end of a `For`
            scope. This setting is useful when you don't want to
            update each variable by implementing the `For` scope.
        globals_ : dict or None, default None
            Current scope's global variables. Set globals()
            value to this argument. This setting works
            the same way as the locals_ argument.

        References
        ----------
        - For
            - https://simon-ritchie.github.io/apysc/en/for.html

        Examples
        --------
        >>> import apysc as ap
        >>> arr: ap.Array = ap.Array(range(3))
        >>> with ap.For(arr) as i:
        ...     ap.trace("Loop index is:", i)
        ...
        """
        self._validate_arr_or_dict_val_type(arr_or_dict=arr_or_dict)
        if locals_ is None:
            locals_ = {}
        if globals_ is None:
            globals_ = {}
        self._arr_or_dict = arr_or_dict
        self._locals = locals_
        self._globals = globals_
        self._indent = Indent()

    @final
    def _validate_arr_or_dict_val_type(
        self, *, arr_or_dict: Union[Array, Dictionary]
    ) -> None:
        """
        Validate loop value type is Array of Dictionary.

        Parameters
        ----------
        arr_or_dict : Array or Dictionary
            Value to be checked.

        Raises
        ------
        TypeError
            If a value type is neither Array nor Dictionary.
        """
        if isinstance(arr_or_dict, (Array, Dictionary)):
            return
        raise TypeError(
            "Specified value type is neither Array nor Dictionary: "
            f"{type(arr_or_dict)}"
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def __enter__(self) -> _Target:
        """
        This class calls this method at the with-statement.

        Returns
        -------
        i_or_key : Int or String
            Loop index or dictionary key.
        """
        import apysc as ap
        from apysc._loop import loop_count
        from apysc._type import revert_mixin

        loop_count.increment_current_loop_count()
        self._snapshot_name = revert_mixin.make_snapshots_of_each_scope_vars(
            locals_=self._locals, globals_=self._globals
        )
        i_or_key: Union[ap.Int, ap.String]
        if isinstance(self._arr_or_dict, ap.Array):
            i_or_key = ap.Int(0)
            self._append_arr_enter_expression(i=i_or_key)
        elif isinstance(self._arr_or_dict, ap.Dictionary):
            if self._arr_or_dict._value:
                key: str = str(list(self._arr_or_dict._value.keys())[0])
            else:
                key = ""
            i_or_key = ap.String(key)
            self._append_dict_enter_expression(key=i_or_key)
        self._indent.__enter__()
        return i_or_key  # type: ignore

    @final
    @add_debug_info_setting(module_name=__name__)
    def __exit__(self, *args: Any) -> None:
        """
        This class calls this method at the with-statement.
        """
        import apysc as ap
        from apysc._expression import last_scope
        from apysc._expression.last_scope import LastScope
        from apysc._loop import loop_count
        from apysc._type import revert_mixin

        loop_count.decrement_current_loop_count()
        revert_mixin.revert_each_scope_vars(
            snapshot_name=self._snapshot_name,
            locals_=self._locals,
            globals_=self._globals,
        )
        self._indent.__exit__()
        ap.append_js_expression(expression="}")
        last_scope.set_last_scope(value=LastScope.FOR)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_arr_enter_expression(self, *, i: Int) -> None:
        """
        Append for loop start expression (for Array value).

        Parameters
        ----------
        i : Int
            Loop index value.
        """
        import apysc as ap

        i_name: str = i.variable_name
        expression: str = (
            f"var length = {self._arr_or_dict.variable_name}.length;\n"
            f"for ({i_name} = 0; {i_name} < length; {i_name}++) {{"
        )
        ap.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_dict_enter_expression(self, *, key: String) -> None:
        """
        Append for loop start expression (for Dictionary value).

        Parameters
        ----------
        key : String
            Loop (dictionary) key value.
        """
        import apysc as ap

        key_name: str = key.variable_name
        expression: str = (
            f"for (var {key_name} in " f"{self._arr_or_dict.variable_name}) {{"
        )
        ap.append_js_expression(expression=expression)

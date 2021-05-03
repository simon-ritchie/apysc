"""For loop class implementation.
"""

from typing import Any
from typing import Dict
from typing import Generic
from typing import Optional
from typing import Type
from typing import TypeVar
from typing import Union

from apysc import Array
from apysc import Dictionary
from apysc import Int
from apysc import Number
from apysc import String
from apysc.expression.indent_num import Indent

T = TypeVar('T', Int, String, Number)


class For(Generic[T]):

    _arr_or_dict: Union[Array, Dictionary]
    _locals: Dict[str, Any]
    _globals: Dict[str, Any]
    _snapshot_name: str
    _indent: Indent

    def __init__(
            self, arr_or_dict: Union[Array, Dictionary],
            locals_: Optional[Dict[str, Any]] = None,
            globals_: Optional[Dict[str, Any]] = None) -> None:
        """
        A class to append for (loop) expression.

        Parameters
        ----------
        arr_or_dict : Array or Dictionary
            Array or Dictionary instance to iterate.
        locals_ : dict or None, default None
            Current scope's local variables. Set locals() value to
            this argument. If specified, all local scope
            VariableNameInterface variables (like Int, Sprite) will be
            reverted ad the end of For scope. This setting is useful
            when you don't want to update each variable by the
            implementation of the For scope.
        globals_ : dict or None, default None
            Current scope's golobal variables. Set golobals() value
            to this argument. If specified, all local scope
            VariableNameInterface variables (like Int, Sprite) will be
            reverted ad the end of For scope. This setting is useful
            when you don't want to update each variable by the
            implementation of the For scope.
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

    def _validate_arr_or_dict_val_type(
            self, arr_or_dict: Union[Array, Dictionary]) -> None:
        """
        Validate loop value type is Array of Dictionary.

        Parameters
        ----------
        arr_or_dict : Array or Dictionary
            Value to be checked.

        Raises
        ------
        TypeError
            If value type is neither Array nor Dictionary.
        """
        if isinstance(arr_or_dict, (Array, Dictionary)):
            return
        raise TypeError(
            'Specified value type is neither Array nor Dictionary: '
            f'{type(arr_or_dict)}')

    def __enter__(self) -> T:
        """
        Method to be called when begining of with statement.

        Returns
        -------
        i_or_key : Int or String
            Loop index or dictionary key.
        """
        from apysc.type import revert_interface
        self._snapshot_name = \
            revert_interface.make_snapshots_of_each_scope_vars(
                locals_=self._locals, globals_=self._globals)
        i_or_key: Union[Int, String]
        if isinstance(self._arr_or_dict, Array):
            i_or_key = Int(0)
            self._append_arr_enter_expression(i=i_or_key)
        else:
            i_or_key = String('')
            self._append_dict_enter_expression(key=i_or_key)
        self._indent.__enter__()
        return i_or_key  # type: ignore

    def __exit__(
            self, exc_type: Type,
            exc_value: Any,
            traceback: Any) -> None:
        """
        Method to be called when end of with statement.

        Parameters
        ----------
        exc_type : Type
            Exception type.
        exc_value : *
            Exception value.
        traceback : *
            Traceback value.
        """
        from apysc.expression import expression_file_util
        from apysc.expression import last_scope
        from apysc.expression.last_scope import LastScope
        from apysc.type import revert_interface
        revert_interface.revert_each_scope_vars(
            snapshot_name=self._snapshot_name,
            locals_=self._locals, globals_=self._globals)
        self._indent.__exit__()
        expression_file_util.append_js_expression(expression='}')
        last_scope.set_last_scope(value=LastScope.FOR)

    def _append_arr_enter_expression(self, i: Int) -> None:
        """
        Append for loop start expression (for Array value) to file.

        Parameters
        ----------
        i : Int
            Loop index value.
        """
        from apysc.expression import expression_file_util
        i_name: str = i.variable_name
        expression: str = (
            f'var length = {self._arr_or_dict.variable_name}.length;\n'
            f'for ({i_name} = 0; {i_name} < length; {i_name}++) {{'
        )
        expression_file_util.append_js_expression(expression=expression)

    def _append_dict_enter_expression(self, key: String) -> None:
        """
        Append for loop start expression (for Dictionary value) to file.

        Parameters
        ----------
        key : String
            Loop (dictionary) key value.
        """
        from apysc.expression import expression_file_util
        key_name: str = key.variable_name
        expression: str = (
            f'for (var {key_name} in {self._arr_or_dict.variable_name}) {{'
        )
        expression_file_util.append_js_expression(expression=expression)

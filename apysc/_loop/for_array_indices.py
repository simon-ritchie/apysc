"""The loop implementation class for the `ap.Array` indices.
"""

from typing import Any
from typing import Dict
from typing import Generic
from typing import Optional
from typing import TypeVar
from typing import Union
from typing import Generic
from typing import TypeVar

from typing_extensions import final
from apysc._expression.indent_num import Indent
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.array import Array
from apysc._type.int import Int
from apysc._validation import arg_validation_decos

_ArrValue = TypeVar("_ArrValue")


class ForArrayIndices(Generic[_ArrValue]):
    """
    The loop implementation class for the `ap.Array` indices.
    """

    _arr: Array[_ArrValue]
    _locals: Dict[str, Any]
    _globals: Dict[str, Any]
    _variable_name_suffix: str
    _snapshot_name: str
    _indent: Indent

    @final
    @arg_validation_decos.is_apysc_array(arg_position_index=1)
    @arg_validation_decos.is_builtin_string(arg_position_index=4, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        arr: Array[_ArrValue],
        *,
        locals_: Optional[Dict[str, Any]] = None,
        globals_: Optional[Dict[str, Any]] = None,
        variable_name_suffix: str = "",
    ) -> None:
        """
        The loop implementation class for the `ap.Array` indices.

        Parameters
        ----------
        arr : Array[_ArrValue]
            An array to iterate.
        locals_ : Optional[Dict[str, Any]], optional
            Current scope's local variables. Set locals()
            value to this argument. If specified, this interface
            reverts all local scope VariableNameMixIn
            variables (like Int, Sprite) at the end of a `For`
            scope. This setting is useful when you don't want to
            update each variable by implementing the `For` scope.
        globals_ : Optional[Dict[str, Any]], optional
            Current scope's global variables. Set globals()
            value to this argument. This setting works
            the same way as the locals_ argument.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if locals_ is None:
            locals_ = {}
        if globals_ is None:
            globals_ = {}
        self._arr = arr
        self._locals = locals_
        self._globals = globals_
        self._variable_name_suffix = variable_name_suffix
        self._indent = Indent()

    @final
    @add_debug_info_setting(module_name=__name__)
    def __enter__(self) -> Int:
        """
        The entering method for the with-statement.

        Returns
        -------
        i : Int
            An index of iteration.
        """
        import apysc as ap
        from apysc._loop import loop_count
        from apysc._type import revert_mixin

        loop_count.increment_current_loop_count()
        self._snapshot_name = revert_mixin.make_snapshots_of_each_scope_vars(
            locals_=self._locals, globals_=self._globals
        )
        i: Int = ap.Int(0, variable_name_suffix=self._variable_name_suffix)
        self._append_enter_expression(i=i)
        pass

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_enter_expression(self, *, i: Int) -> None:
        """
        Append a for-loop start expression.

        Parameters
        ----------
        i : Int
            Loop index value.
        """
        import apysc as ap

        arr_name: str = self._arr.variable_name
        i_name: str = i.variable_name
        expression: str = (
            f"for ({i_name} = 0; {i_name} < {arr_name}.length; {i_name}++) {{"
        )
        ap.append_js_expression(expression=expression)

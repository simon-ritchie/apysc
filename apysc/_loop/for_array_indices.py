"""The loop implementation class for the `ap.Array` indices.
"""

from typing import Any
from typing import Dict
from typing import Optional

from typing_extensions import final

from apysc._expression.get_last_scope_interface import GetLastScopeInterface
from apysc._expression.indent_num import Indent
from apysc._expression.last_scope import LastScope
from apysc._html.debug_mode import add_debug_info_setting
from apysc._loop.for_loop_exit_mixin import ForLoopExitMixIn
from apysc._type.array import Array
from apysc._type.initialize_locals_and_globals_mixin import (
    InitializeLocalsAndGlobalsMixIn,
)
from apysc._type.int import Int
from apysc._validation import arg_validation_decos


class ForArrayIndices(
    ForLoopExitMixIn,
    GetLastScopeInterface,
    InitializeLocalsAndGlobalsMixIn,
):
    """
    The loop implementation class for the `ap.Array` indices.

    References
    ----------
    - ForArrayIndices class
        - https://simon-ritchie.github.io/apysc/en/for_array_indices.html
    - Why the apysc library doesn’t use the Python built-in data type
        - https://simon-ritchie.github.io/apysc/en/why_apysc_doesnt_use_python_builtin_data_type.html  # noqa
    - Each branch instruction class’s scope variable reverting setting
        - https://simon-ritchie.github.io/apysc/en/branch_instruction_variables_reverting_setting.html  # noqa

    Examples
    --------
    >>> import apysc as ap

    >>> arr: ap.Array[ap.Number] = ap.Array(
    ...     [ap.Number(50), ap.Number(150), ap.Number(250)]
    ... )
    >>> indices: ap.Array[ap.Int] = ap.Array([])
    >>> with ap.ForArrayIndices(arr=arr) as i:
    ...     indices.append(i)
    ...

    >>> _ = ap.assert_arrays_equal(indices, [0, 1, 2])
    """

    _arr: Array
    _variable_name_suffix: str

    @final
    @arg_validation_decos.is_apysc_array(arg_position_index=1)
    @arg_validation_decos.is_builtin_string(arg_position_index=4, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        arr: Array,
        *,
        locals_: Optional[Dict[str, Any]] = None,
        globals_: Optional[Dict[str, Any]] = None,
        variable_name_suffix: str = "",
    ) -> None:
        """
        The loop implementation class for the `ap.Array` indices.

        Parameters
        ----------
        arr : Array
            An array to iterate.
        locals_ : Optional[Dict[str, Any]], optional
            Current scope's local variables. Set locals()
            value to this argument. If specified, this interface
            reverts all local scope VariableNameMixIn
            variables (like Int, Sprite) at the end of a with-statement
            scope. This setting is useful when you don't want to
            update each variable.
        globals_ : Optional[Dict[str, Any]], optional
            Current scope's global variables. Set globals()
            value to this argument. This setting works
            the same way as the locals_ argument.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        References
        ----------
        - ForArrayIndices class
            - https://simon-ritchie.github.io/apysc/en/for_array_indices.html
        - Why the apysc library doesn’t use the Python built-in data type
            - https://simon-ritchie.github.io/apysc/en/why_apysc_doesnt_use_python_builtin_data_type.html  # noqa
        - Each branch instruction class’s scope variable reverting setting
            - https://simon-ritchie.github.io/apysc/en/branch_instruction_variables_reverting_setting.html  # noqa

        Examples
        --------
        >>> import apysc as ap

        >>> arr: ap.Array[ap.Number] = ap.Array(
        ...     [ap.Number(50), ap.Number(150), ap.Number(250)]
        ... )
        >>> indices: ap.Array[ap.Int] = ap.Array([])
        >>> with ap.ForArrayIndices(arr=arr) as i:
        ...     indices.append(i)
        ...

        >>> _ = ap.assert_arrays_equal(indices, [0, 1, 2])
        """
        self._initialize_locals_and_globals(locals_=locals_, globals_=globals_)
        self._arr = arr
        self._variable_name_suffix = variable_name_suffix
        self._indent = Indent()

    @final
    @add_debug_info_setting(module_name=__name__)
    def __enter__(self) -> Int:
        """
        The entering method for the beginning of with-statement.

        Returns
        -------
        i : Int
            An index of iteration.
        """
        from apysc._loop import loop_count
        from apysc._type import revert_mixin

        loop_count.increment_current_loop_count()
        self._snapshot_name = revert_mixin.make_snapshots_of_each_scope_vars(
            locals_=self._locals, globals_=self._globals
        )
        i: Int = Int(0, variable_name_suffix=self._variable_name_suffix)
        self._append_enter_expression(i=i)
        self._indent.__enter__()
        return i

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
        from apysc._expression import expression_data_util

        arr_name: str = self._arr.variable_name
        i_name: str = i.variable_name
        expression: str = (
            f"for ({i_name} = 0; {i_name} < {arr_name}.length; {i_name}++) {{"
        )
        expression_data_util.append_js_expression(expression=expression)

    @final
    def _get_last_scope(self) -> LastScope:
        """
        Get a target last scope value.

        Returns
        -------
        last_scope : LastScope
            A target last scope.
        """
        return LastScope.FOR_ARRAY_INDICES

"""The loop implementation class for the `ap.Array` indices and values.
"""

from typing import Any
from typing import Dict
from typing import Generic
from typing import Optional
from typing import Tuple
from typing import Type
from typing import TypeVar

from typing_extensions import final

from apysc._expression.get_last_scope_interface import GetLastScopeInterface
from apysc._expression.indent_num import Indent
from apysc._expression.last_scope import LastScope
from apysc._html.debug_mode import add_debug_info_setting
from apysc._loop.for_loop_exit_mixin import ForLoopExitMixIn
from apysc._loop.initialize_with_base_value_interface import (
    InitializeWithBaseValueInterface,
)
from apysc._type.array import Array
from apysc._type.initialize_locals_and_globals_mixin import (
    InitializeLocalsAndGlobalsMixIn,
)
from apysc._type.int import Int
from apysc._validation import arg_validation_decos

_ArrayValue = TypeVar("_ArrayValue", bound=InitializeWithBaseValueInterface)


class ForArrayIndicesAndValues(
    ForLoopExitMixIn,
    GetLastScopeInterface,
    InitializeLocalsAndGlobalsMixIn,
    Generic[_ArrayValue],
):
    """
    The loop implementation class for the `ap.Array` indices and values.

    References
    ----------
    - ForArrayIndicesAndValues
        - https://simon-ritchie.github.io/apysc/en/for_array_indices_and_values.html

    Examples
    --------
    >>> import apysc as ap

    >>> _ = ap.Stage(
    ...     stage_width=350, stage_height=225, background_color=ap.Color("#333")
    ... )

    >>> x_arr: ap.Array[ap.Number] = ap.Array(
    ...     [ap.Number(75), ap.Number(175), ap.Number(275)]
    ... )
    >>> with ap.ForArrayIndicesAndValues(arr=x_arr, arr_value_type=ap.Number) as (i, x):
    ...     circle: ap.Circle = ap.Circle(
    ...         x=x,
    ...         y=(i + 1) * 50,
    ...         radius=25,
    ...         fill_color=ap.Color("#0af"),
    ...     )
    ...
    """

    _arr: Array[_ArrayValue]
    _arr_value_type: Type[_ArrayValue]
    _variable_name_suffix: str

    @final
    @arg_validation_decos.is_apysc_array(arg_position_index=1)
    @arg_validation_decos.is_initialize_with_base_value_interface_subclass(
        arg_position_index=2,
    )
    @arg_validation_decos.is_builtin_string(arg_position_index=5, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        arr: Array[_ArrayValue],
        arr_value_type: Type[_ArrayValue],
        *,
        locals_: Optional[Dict[str, Any]] = None,
        globals_: Optional[Dict[str, Any]] = None,
        variable_name_suffix: str = "",
    ) -> None:
        """
        The loop implementation class for the `ap.Array` indices and values.

        Parameters
        ----------
        arr : Array[_ArrayValue]
            An array to iterate.
        arr_value_type : Type[_ArrayValue]
            An array value type. This interface accepts apysc
            types, such as the `Int`, `String`, `Rectangle`.
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
        - ForArrayIndicesAndValues
            - https://simon-ritchie.github.io/apysc/en/for_array_indices_and_values.html

        Examples
        --------
        >>> import apysc as ap

        >>> _ = ap.Stage(
        ...     stage_width=350, stage_height=225, background_color=ap.Color("#333")
        ... )

        >>> x_arr: ap.Array[ap.Number] = ap.Array(
        ...     [ap.Number(75), ap.Number(175), ap.Number(275)]
        ... )
        >>> with ap.ForArrayIndicesAndValues(arr=x_arr, arr_value_type=ap.Number) as (
        ...     i,
        ...     x,
        ... ):
        ...     circle: ap.Circle = ap.Circle(
        ...         x=x,
        ...         y=(i + 1) * 50,
        ...         radius=25,
        ...         fill_color=ap.Color("#0af"),
        ...     )
        """
        self._initialize_locals_and_globals(locals_=locals_, globals_=globals_)
        self._arr = arr
        self._arr_value_type = arr_value_type
        self._variable_name_suffix = variable_name_suffix
        self._indent = Indent()

    @final
    def _get_last_scope(self) -> LastScope:
        """
        Get a target last scope value.

        Returns
        -------
        last_scope : LastScope
            A target last scope.
        """
        return LastScope.FOR_ARRAY_INDICES_AND_VALUES

    @final
    @add_debug_info_setting(module_name=__name__)
    def __enter__(self) -> Tuple[Int, _ArrayValue]:
        """
        The entering method for the beginning of with-statement.

        Returns
        -------
        i : Int
            An index of iteration.
        _ArrayValue
            A value of iteration.
        """
        from apysc._expression import expression_data_util
        from apysc._loop import loop_count
        from apysc._type import revert_mixin
        from apysc._validation.variable_name_validation import (
            validate_variable_name_mixin_type,
        )

        loop_count.increment_current_loop_count()
        self._snapshot_name = revert_mixin.make_snapshots_of_each_scope_vars(
            locals_=self._locals, globals_=self._globals
        )
        arr_value: _ArrayValue = self._arr_value_type._initialize_with_base_value()
        arr_value_variable_name: str = validate_variable_name_mixin_type(
            instance=arr_value
        ).variable_name

        i: Int = Int(0, variable_name_suffix=self._variable_name_suffix)
        arr_name: str = self._arr.variable_name
        i_name: str = i.variable_name
        expression: str = (
            f"for ({i_name} = 0; {i_name} < {arr_name}.length; {i_name}++) {{"
        )
        expression_data_util.append_js_expression(expression=expression)

        self._indent.__enter__()
        expression = f"{arr_value_variable_name} = {arr_name}[{i_name}];"
        expression_data_util.append_js_expression(expression=expression)

        return i, arr_value

"""The mix-in class implementation for the `ColorCopyMixIn` class.
"""

from copy import deepcopy
from typing import TYPE_CHECKING
from typing import Generic
from typing import TypeVar
from typing import cast

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.copy_interface import CopyInterface

if TYPE_CHECKING:
    from apysc._color.color import Color

_SelfType = TypeVar("_SelfType", bound="Color")


class ColorCopyMixIn(
    CopyInterface,
    Generic[_SelfType],
):
    @final
    @add_debug_info_setting(module_name=__name__)
    def _copy(self) -> _SelfType:
        """
        Make a deep copy of this instance.

        Returns
        -------
        result : _SelfType
            Copied instance.
        """
        from apysc._expression import event_handler_scope
        from apysc._expression import expression_data_util
        from apysc._expression import expression_variables_util
        from apysc._expression.event_handler_scope import TemporaryNotHandlerScope

        result: _SelfType = cast(_SelfType, deepcopy(self))
        result._value.variable_name = expression_variables_util.get_next_variable_name(
            type_name=result._value.type_name,
        )
        with TemporaryNotHandlerScope():
            expression: str = self._get_copy_expression(result=result)
            expression_data_util.append_js_expression(expression=expression)

        if event_handler_scope.current_scope_is_in_event_handler():
            expression_data_util.append_js_expression(expression=expression)

        result._variable_name = result._value.variable_name
        return result

    def _get_copy_expression(self, *, result: _SelfType) -> str:
        """
        Get a copy expression.

        Parameters
        ----------
        result : _SelfType
            A copied instance.

        Returns
        -------
        expression : str
            A target expression.
        """
        from apysc._validation import variable_name_validation

        self_value_variable_name: str = (
            variable_name_validation.validate_variable_name_mixin_type(
                instance=getattr(self, "_value"),
            ).variable_name
        )
        expression: str = (
            f"var {result._value.variable_name} = {self_value_variable_name};"
        )
        return expression

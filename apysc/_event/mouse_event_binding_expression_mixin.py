"""Class implementation for the event binding expression-related mix-in.
"""

from typing_extensions import final

from apysc._event.mouse_event_type import MouseEventType
from apysc._html.debug_mode import add_debug_info_setting


class MouseEventBindingExpressionMixin:
    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_mouse_event_binding_expression(
        self, *, name: str, mouse_event_type: MouseEventType
    ) -> None:
        """
        Append a mouse event binding expression.

        Parameters
        ----------
        name : str
            Handler's name.
        mouse_event_type : MouseEventType
            Event type to bind.
        """
        import apysc as ap
        from apysc._type.variable_name_mixin import VariableNameMixIn
        from apysc._validation.variable_name_validation import (
            validate_variable_name_interface_type,
        )

        self_instance: VariableNameMixIn = validate_variable_name_interface_type(
            instance=self
        )
        expression: str = (
            f"{self_instance.variable_name}.{mouse_event_type.value}({name});"
        )
        ap.append_js_expression(expression=expression)

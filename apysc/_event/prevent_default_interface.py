"""Class implementation for the prevent_default interface.
"""

from apysc._type.variable_name_interface import VariableNameInterface


class PreventDefaultInterface(VariableNameInterface):

    def prevent_default(self) -> None:
        """
        Prevent event's default behavior.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.prevent_default, locals_=locals(),
                module_name=__name__, class_=PreventDefaultInterface):
            expression: str = (
                f'{self.variable_name}.preventDefault();'
            )
            ap.append_js_expression(expression=expression)

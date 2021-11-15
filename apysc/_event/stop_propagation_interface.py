"""Class implementation for the stop_propagation interface.
"""

from apysc._type.variable_name_interface import VariableNameInterface


class StopPropagationInterface(VariableNameInterface):

    def stop_propagation(self) -> None:
        """
        Stop event propagation.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.stop_propagation, locals_=locals(),
                module_name=__name__, class_=StopPropagationInterface):
            expression: str = (
                f'{self.variable_name}.stopPropagation();'
            )
            ap.append_js_expression(expression=expression)

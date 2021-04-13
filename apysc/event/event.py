"""Class Implementation for basic event.
"""

from typing import Optional

from apysc.type.variable_name_interface import VariableNameInterface


class Event(VariableNameInterface):

    _this: VariableNameInterface

    def __init__(
            self, this: VariableNameInterface,
            type_name: Optional[str] = None) -> None:
        """
        Basic event class.

        Parameters
        ----------
        this : VariableNameInterface
            Instance that listening event (e.g., Sprite).
        type_name : str or None, default None
            Type name to set. Only specify when inherit this class.
        """
        from apysc.expression import expression_variables_util
        from apysc.expression import var_names
        self._this = this
        if type_name is None:
            type_name = var_names.EVENT
        self.variable_name = expression_variables_util.get_next_variable_name(
            type_name=type_name)

    def stop_propagation(self) -> None:
        """
        Stop event propagation.
        """
        from apysc.expression import expression_file_util
        expression: str = (
            f'{self.variable_name}.stopPropagation();'
        )
        expression_file_util.append_js_expression(expression=expression)

    def prevent_default(self) -> None:
        """
        Prevent event's default behavior.
        """
        from apysc.expression import expression_file_util
        expression: str = (
            f'{self.variable_name}.preventDefault();'
        )
        expression_file_util.append_js_expression(expression=expression)

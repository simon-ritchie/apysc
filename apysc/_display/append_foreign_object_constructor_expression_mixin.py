"""The mix-in class for the `_append_foreign_object_constructor_expression`
method.
"""

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int


class AppendForeignObjectConstructorExpressionMixIn:
    _width: Int

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_foreign_object_constructor_expression(self) -> None:
        """
        Append a `foreignObject`'s constructor expression.
        """
        from apysc._display.stage import Stage
        from apysc._display.stage import get_stage
        from apysc._expression import expression_data_util
        from apysc._validation.variable_name_validation import (
            validate_variable_name_mixin_type,
        )

        self_variable_name: str = validate_variable_name_mixin_type(
            instance=self
        ).variable_name
        stage: Stage = get_stage()
        expression: str = (
            f"var {self_variable_name} = {stage.variable_name}"
            ".foreignObject("
            f"{self._width.variable_name}, 0);"
        )
        expression_data_util.append_js_expression(expression=expression)

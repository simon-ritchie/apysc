"""The mix-in class for the `_add_foreign_object_child` method.
"""

from typing_extensions import final

from apysc._display.svg_foreign_object_child import SvgForeignObjectChild
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos


class AddForeignObjectChildMixIn:
    @final
    @arg_validation_decos.is_svg_foreign_object_child(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def _add_foreign_object_child(self, *, child: SvgForeignObjectChild) -> None:
        """
        Add a foreignObject's child object.

        Parameters
        ----------
        child : SvgForeignObjectChild
            A foreignObject's child object.
        """
        from apysc._expression import expression_data_util
        from apysc._validation.variable_name_validation import (
            validate_variable_name_mixin_type,
        )

        self_variable_name: str = validate_variable_name_mixin_type(
            instance=self
        ).variable_name
        expression: str = f"{self_variable_name}.add({child.variable_name});"
        expression_data_util.append_js_expression(expression=expression)

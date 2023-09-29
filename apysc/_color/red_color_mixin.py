"""The mix-in class implementation for the `red_color` property.
"""

from apysc._type.int import Int
from apysc._html.debug_mode import add_debug_info_setting


class RedColorMixIn:
    @property
    def red_color(self) -> Int:
        """
        Get a red color integer value (0 to 255).

        Returns
        -------
        red_color : Int
            Red color integer value (0 to 255).
        """
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix
        )
        from apysc._validation import variable_name_validation
        from apysc._expression import expression_data_util

        suffix: str = get_attr_or_variable_name_suffix(
            instance=self, value_identifier="red_color"
        )
        red_color: Int = Int(0, variable_name_suffix=suffix)
        variable_name: str = variable_name_validation.validate_variable_name_mixin_type(
            instance=self,
        ).variable_name

        expression: str = (
            f"{red_color.variable_name} = "
            f"parseInt({variable_name}.substring(1, 3), 16);"
        )
        expression_data_util.append_js_expression(expression=expression)
        return red_color

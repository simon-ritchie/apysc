"""The mix-in class implementation for the `to_string` method.
"""

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.string import String
from apysc._type.variable_name_mixin import VariableNameMixIn


class ToStringMixIn(VariableNameMixIn):
    @final
    @add_debug_info_setting(module_name=__name__)
    def to_string(self) -> String:
        """
        Convert this instance to a string.

        Returns
        -------
        string : String
            A converted string.

        References
        ----------
        - to_string interface
            - https://simon-ritchie.github.io/apysc/en/to_string.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage(
        ...     background_color=ap.Color("#333"), stage_width=200, stage_height=200
        ... )
        >>> int_value: ap.Int = ap.Int(value=100)
        >>> string: ap.String = int_value.to_string()
        >>> ap.assert_equal(string, "100")
        """
        from apysc._expression import expression_data_util
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        suffix: str = get_attr_or_variable_name_suffix(
            instance=self, value_identifier="string"
        )
        string: String = String("", variable_name_suffix=suffix)
        expression: str = f"{string.variable_name} = String({self.variable_name});"
        expression_data_util.append_js_expression(expression=expression)
        return string

"""The mix-in class implementation for the `String`'s `lower` method.
"""

from typing import TYPE_CHECKING

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting

if TYPE_CHECKING:
    from apysc._type.string import String


class StringLowerMixIn:
    @final
    @add_debug_info_setting(module_name=__name__)
    def lower(self) -> "String":
        """
        Get a copied lower case string.

        Returns
        -------
        string : String
            A copied lower case string.

        References
        ----------
        - String class lower method
            - https://simon-ritchie.github.io/apysc/en/string_lower.html

        Examples
        --------
        >>> import apysc as ap
        >>> string: ap.String = ap.String("HELLO")
        >>> string = string.lower()
        >>> string
        String("hello")
        """
        from apysc._expression import expression_data_util
        from apysc._type.string import String
        from apysc._validation import string_validation

        self_string: String = string_validation.validate_apysc_string_type(string=self)
        string = self_string._copy()
        string._value = string._value.lower()
        expression: str = (
            f"{string.variable_name} = {self_string.variable_name}.toLowerCase();"
        )
        expression_data_util.append_js_expression(expression=expression)
        return string

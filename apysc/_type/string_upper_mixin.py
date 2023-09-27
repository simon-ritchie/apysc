"""The mix-in class implementation for the `String`'s `upper` method.
"""

from typing import TYPE_CHECKING

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting

if TYPE_CHECKING:
    from apysc._type.string import String


class StringUpperMixIn:
    @final
    @add_debug_info_setting(module_name=__name__)
    def upper(self) -> "String":
        """
        Get a copied upper case string.

        Returns
        -------
        string : String
            A copied upper case string.

        References
        ----------
        - String class upper method
            - https://simon-ritchie.github.io/apysc/en/string_upper.html

        Examples
        --------
        >>> import apysc as ap
        >>> string: ap.String = ap.String("Hello")
        >>> string = string.upper()
        >>> string
        String("HELLO")
        """
        from apysc._expression import expression_data_util
        from apysc._type.string import String
        from apysc._validation import string_validation

        self_string: String = string_validation.validate_apysc_string_type(string=self)
        string: String = self_string._copy()
        string._value = string._value.upper()
        expression: str = (
            f"{string.variable_name} = {self_string.variable_name}.toUpperCase();"
        )
        expression_data_util.append_js_expression(expression=expression)
        return string

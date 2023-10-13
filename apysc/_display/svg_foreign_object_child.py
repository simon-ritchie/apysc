"""The module for the `SVGForeignObjectChild` class.
"""


from typing import Union
from apysc._display.css_mixin import CssMixIn
from apysc._display.display_object import DisplayObject
from apysc._loop.initialize_with_base_value_interface import InitializeWithBaseValueInterface
from apysc._type.string import String
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class SVGForeignObjectChild(
    CssMixIn,
    DisplayObject,
    VariableNameSuffixMixIn,
    InitializeWithBaseValueInterface,
):
    _html_str: String

    def __init__(
        self,
        *,
        html_str: Union[str, String],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Class implementation for the SVG's foreignObject child.

        Parameters
        ----------
        html_str : Union[str, String]
            A HTML string.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        from apysc._converter import to_apysc_val_from_builtin

        self._variable_name_suffix = variable_name_suffix
        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.SVG_FOREIGN_OBJECT_CHILD,
        )
        super(SVGForeignObjectChild, self).__init__(variable_name=variable_name)

        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="html_str"
        )
        self._html_str = to_apysc_val_from_builtin.get_copied_string_from_builtin_val(
            string=html_str,
            variable_name_suffix=suffix,
        )
        self._append_constructor_expression()

    def _append_constructor_expression(self) -> None:
        """
        Append a constructor expression of the SVG's foreignObject child.
        """
        from apysc._expression import expression_data_util

        expression: str = (
            f"var {self.variable_name} = SVG({self._html_str.variable_name});"
        )
        expression_data_util.append_js_expression(expression=expression)

    @classmethod
    def _initialize_with_base_value(cls) -> "SVGForeignObjectChild":
        """
        Initialize this class with a base value(s).

        Returns
        -------
        SVGForeignObjectChild
            An initialized instance.
        """
        foreign_object_child: SVGForeignObjectChild = SVGForeignObjectChild(html_str="")
        return foreign_object_child

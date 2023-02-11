"""Class implementation for a SVG text.
"""

from typing import Union

from apysc._type.string import String
from apysc._display.svg_text_text_mixin import SVGTextTextMixIn
from apysc._display.display_object import DisplayObject
from apysc._display.x_mixin import XMixIn
from apysc._display.y_mixin import YMixIn


class SVGText(
    DisplayObject,
    SVGTextTextMixIn,
    XMixIn,
    YMixIn,
):

    def __init__(
        self,
        *,
        text: Union[str, String],
        variable_name_suffix: str = "",
    ) -> None:
        """
        The class for a SVG text.

        Parameters
        ----------
        text : Union[str, String]
            A text to use in this class.
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.SVG_TEXT,
        )
        self.variable_name = variable_name
        self._variable_name_suffix = variable_name_suffix
        super(SVGText, self).__init__(
            variable_name=variable_name,
        )

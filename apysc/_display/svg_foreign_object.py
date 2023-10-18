"""The class implementation for the SVG's `foreignObject`.
"""

from typing import Union
from apysc._display.css_mixin import CssMixIn
from apysc._display.height_mixin import HeightMixIn
from apysc._display.set_overflow_visible_setting_mixin import (
    SetOverflowVisibleSettingMixIn
)
from apysc._display.width_mixin import WidthMixIn
from apysc._type.int import Int
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._display.display_object import DisplayObject
from apysc._loop.initialize_with_base_value_interface import (
    InitializeWithBaseValueInterface,
)
from apysc._display.add_foreign_object_child_mixin import (
    AddForeignObjectChildMixIn
)
from apysc._display.append_foreign_object_constructor_expression_mixin import (
    AppendForeignObjectConstructorExpressionMixIn
)
from apysc._display.svg_foreign_object_initialize_width_mixin import (
    SVGForeignObjectInitializeWidthMixIn
)
from apysc._display.add_to_stage_mixin import AddToStageMixIn


class SVGForeignObject(
    DisplayObject,
    WidthMixIn,
    HeightMixIn,
    VariableNameSuffixMixIn,
    CssMixIn,
    SetOverflowVisibleSettingMixIn,
    InitializeWithBaseValueInterface,
    AddForeignObjectChildMixIn,
    AppendForeignObjectConstructorExpressionMixIn,
    SVGForeignObjectInitializeWidthMixIn,
    AddToStageMixIn,
):
    def __init__(
        self,
        *,
        width: Union[int, Int],
        height: Union[int, Int],
        variable_name_suffix: str = "",
    ) -> None:
        """
        The class implementation for the SVG's `foreignObject` element.

        Parameters
        ----------
        width : Union[int, Int]
            Width of the foreignObject element.
        height : Union[int, Int]
            Height of the foreignObject element.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        self._variable_name_suffix = variable_name_suffix
        self._initialize_width(width=width)
        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.SVG_FOREIGN_OBJECT,
        )
        super(SVGForeignObject, self).__init__(variable_name=variable_name)
        self._append_foreign_object_constructor_expression()
        self._add_to_stage()
        self._set_overflow_visible_setting()

    @classmethod
    def _initialize_with_base_value(cls) -> "SVGForeignObject":
        """
        Initialize this class with a base value(s).

        Returns
        -------
        foreign_object : SVGForeignObject
            An initialized instance.
        """
        foreign_object: SVGForeignObject = SVGForeignObject(width=0, height=0)
        return foreign_object

"""The class implementation for the SVG's `foreignObject`.
"""

from typing import Union
from apysc._display.css_mixin import CssMixIn
from apysc._display.height_mixin import HeightMixIn
from apysc._display.set_overflow_visible_setting_mixin import (
    SetOverflowVisibleSettingMixIn
)
from apysc._display.width_mixin import WidthMixIn
from apysc._expression import expression_data_util
from apysc._type.int import Int
from typing_extensions import final
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._display.display_object import DisplayObject
from apysc._loop.initialize_with_base_value_interface import (
    InitializeWithBaseValueInterface,
)
from apysc._display.add_foreign_object_child_mixin import (
    AddForeignObjectChildMixIn
)


class SVGForeignObject(
    DisplayObject,
    WidthMixIn,
    HeightMixIn,
    VariableNameSuffixMixIn,
    CssMixIn,
    SetOverflowVisibleSettingMixIn,
    InitializeWithBaseValueInterface,
    AddForeignObjectChildMixIn,
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
        from apysc._display.stage import Stage
        from apysc._display.stage import get_stage
        from apysc._converter import to_apysc_val_from_builtin
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        self._variable_name_suffix = variable_name_suffix
        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="width"
        )
        width_: Int = to_apysc_val_from_builtin.get_copied_int_from_builtin_val(
            integer=width,
            variable_name_suffix=suffix,
        )
        suffix = self._get_attr_or_variable_name_suffix(value_identifier="height")
        height_: Int = to_apysc_val_from_builtin.get_copied_int_from_builtin_val(
            integer=height,
            variable_name_suffix=suffix,
        )
        self._width = width_
        self._height = height_
        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.SVG_FOREIGN_OBJECT,
        )
        super(SVGForeignObject, self).__init__(variable_name=variable_name)
        self._append_constructor_expression()

        stage: Stage = get_stage()
        stage.add_child(child=self)
        self._set_overflow_visible_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_constructor_expression(self) -> None:
        """
        Append a constructor expression of the SVG's foreignObject.
        """
        from apysc._display.stage import Stage
        from apysc._display.stage import get_stage

        stage: Stage = get_stage()
        expression: str = (
            f"var {self.variable_name} = {stage.variable_name}"
            ".foreignObject("
            f"{self._width.variable_name}, {self._height.variable_name});"
        )
        expression_data_util.append_js_expression(expression=expression)

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

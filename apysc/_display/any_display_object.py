"""This module is for the `DisplayObject` subclass implementation
to avoid an abstract method error.
"""

from typing_extensions import final

from apysc._display.css_mixin import CssMixIn
from apysc._display.display_object import DisplayObject
from apysc._display.set_overflow_visible_setting_mixin import (
    SetOverflowVisibleSettingMixIn,
)
from apysc._display.x_mixin import XMixIn
from apysc._display.y_mixin import YMixIn
from apysc._expression import var_names
from apysc._html.debug_mode import add_debug_info_setting
from apysc._loop.initialize_with_base_value_interface import (
    InitializeWithBaseValueInterface,
)


class AnyDisplayObject(
    SetOverflowVisibleSettingMixIn,
    CssMixIn,
    DisplayObject,
    XMixIn,
    YMixIn,
    InitializeWithBaseValueInterface,
):
    """
    This class is for the `DisplayObject` subclass
    implementation to avoid an abstract method error.
    """

    @add_debug_info_setting(module_name=__name__)
    def __init__(self) -> None:
        """
        This class is for the `DisplayObject` subclass
        implementation to avoid an abstract method error.
        """
        from apysc._expression import expression_data_util
        from apysc._expression.expression_variables_util import get_next_variable_name

        variable_name: str = get_next_variable_name(
            type_name=var_names.ANY_DISPLAY_OBJECT
        )
        super(AnyDisplayObject, self).__init__(variable_name=variable_name)
        expression: str = f"var {variable_name};"
        expression_data_util.append_js_expression(expression=expression)

    @classmethod
    @final
    def _initialize_with_base_value(cls) -> "AnyDisplayObject":
        """
        Initialize this class with a base value(s).

        Returns
        -------
        any_display_object : AnyDisplayObject
            An initialized object.
        """
        from apysc._type.boolean import Boolean

        any_display_object: AnyDisplayObject = AnyDisplayObject()
        any_display_object.visible = Boolean(False)
        return any_display_object

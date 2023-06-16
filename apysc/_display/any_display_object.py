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
from apysc._loop.initialize_for_loop_key_or_value_interface import (
    InitializeForLoopKeyOrValueInterface,
)


class AnyDisplayObject(
    SetOverflowVisibleSettingMixIn,
    CssMixIn,
    DisplayObject,
    XMixIn,
    YMixIn,
    InitializeForLoopKeyOrValueInterface,
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
        import apysc as ap
        from apysc._expression.expression_variables_util import get_next_variable_name

        variable_name: str = get_next_variable_name(
            type_name=var_names.ANY_DISPLAY_OBJECT
        )
        super(AnyDisplayObject, self).__init__(variable_name=variable_name)
        expression: str = f"var {variable_name};"
        ap.append_js_expression(expression=expression)

    @classmethod
    @final
    def _initialize_for_loop_value(cls) -> "AnyDisplayObject":
        """
        Initialize this instance for a loop value.

        Returns
        -------
        any_display_object : AnyDisplayObject
            An initialized object.
        """
        import apysc as ap

        any_display_object: AnyDisplayObject = AnyDisplayObject()
        any_display_object.visible = ap.Boolean(False)
        return any_display_object

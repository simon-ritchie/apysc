"""The mix-in class implementation for the `set_overflow_visible_setting_mixin`.
"""

from typing_extensions import final

from apysc._display.css_interface import CssInterface
from apysc._html.debug_mode import add_debug_info_setting


class SetOverflowVisibleSettingMixIn(CssInterface):
    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_overflow_visible_setting(self) -> None:
        """
        Set the `visible` value to the `overflow` CSS property.
        """
        self.set_css(name="overflow", value="visible")

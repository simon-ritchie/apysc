from apysc._material_design.icon.material_mark_chat_unread_icon import (
    MaterialMarkChatUnreadIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMarkChatUnreadIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMarkChatUnreadIcon = MaterialMarkChatUnreadIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

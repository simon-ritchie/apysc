from apysc._material_design.icon.material_mark_chat_unread_outlined_icon import (
    MaterialMarkChatUnreadOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMarkChatUnreadOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMarkChatUnreadOutlinedIcon = MaterialMarkChatUnreadOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

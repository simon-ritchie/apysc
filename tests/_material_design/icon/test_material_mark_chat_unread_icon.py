from apysc._material_design.icon.material_mark_chat_unread_icon import (
    MaterialmarkChatUnreadIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialmarkChatUnreadIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialmarkChatUnreadIcon = MaterialmarkChatUnreadIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

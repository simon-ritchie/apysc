from apysc._material_design.icon.material_mark_chat_read_outlined_icon import (
    MaterialmarkChatReadOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialmarkChatReadOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialmarkChatReadOutlinedIcon = MaterialmarkChatReadOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

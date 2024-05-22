from apysc._material_design.icon.material_mark_chat_read_icon import (
    MaterialMarkChatReadIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMarkChatReadIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMarkChatReadIcon = MaterialMarkChatReadIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

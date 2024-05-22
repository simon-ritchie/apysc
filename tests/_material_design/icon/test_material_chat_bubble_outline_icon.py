from apysc._material_design.icon.material_chat_bubble_outline_icon import (
    MaterialChatBubbleOutlineIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialChatBubbleOutlineIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialChatBubbleOutlineIcon = MaterialChatBubbleOutlineIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

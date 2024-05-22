from apysc._material_design.icon.material_chat_bubble_outlined_icon import (
    MaterialChatBubbleOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialChatBubbleOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialChatBubbleOutlinedIcon = MaterialChatBubbleOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

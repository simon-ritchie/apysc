from apysc._material_design.icon.material_chat_bubble_outline_outlined_icon import (
    MaterialChatBubbleOutlineOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialChatBubbleOutlineOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialChatBubbleOutlineOutlinedIcon = (
            MaterialChatBubbleOutlineOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

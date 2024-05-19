from apysc._material_design.icon.material_chat_bubble_outline_outlined_icon import (
    MaterialchatBubbleOutlineOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialchatBubbleOutlineOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialchatBubbleOutlineOutlinedIcon = (
            MaterialchatBubbleOutlineOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

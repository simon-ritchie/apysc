from apysc._material_design.icon.material_chat_outlined_icon import (
    MaterialChatOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialChatOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialChatOutlinedIcon = MaterialChatOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

from apysc._material_design.icon.material_chat_icon import MaterialChatIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialChatIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialChatIcon = MaterialChatIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

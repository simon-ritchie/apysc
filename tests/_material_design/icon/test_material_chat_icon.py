from apysc._material_design.icon.material_chat_icon import MaterialchatIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialchatIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialchatIcon = MaterialchatIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

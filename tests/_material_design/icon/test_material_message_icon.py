from apysc._material_design.icon.material_message_icon import MaterialMessageIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMessageIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMessageIcon = MaterialMessageIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

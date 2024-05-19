from apysc._material_design.icon.material_language_icon import MateriallanguageIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallanguageIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallanguageIcon = MateriallanguageIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

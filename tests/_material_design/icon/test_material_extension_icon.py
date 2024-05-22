from apysc._material_design.icon.material_extension_icon import MaterialExtensionIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialExtensionIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialExtensionIcon = MaterialExtensionIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

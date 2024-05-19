from apysc._material_design.icon.material_accessibility_new_icon import MaterialaccessibilityNewIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialaccessibilityNewIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialaccessibilityNewIcon = MaterialaccessibilityNewIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

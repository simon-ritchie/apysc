from apysc._material_design.icon.material_accessibility_icon import (
    MaterialaccessibilityIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialaccessibilityIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialaccessibilityIcon = MaterialaccessibilityIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

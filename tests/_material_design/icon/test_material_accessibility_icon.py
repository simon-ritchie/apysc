from apysc._material_design.icon.material_accessibility_icon import (
    MaterialAccessibilityIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAccessibilityIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAccessibilityIcon = MaterialAccessibilityIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

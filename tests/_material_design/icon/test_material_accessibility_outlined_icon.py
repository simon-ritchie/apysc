from apysc._material_design.icon.material_accessibility_outlined_icon import (
    MaterialAccessibilityOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAccessibilityOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAccessibilityOutlinedIcon = MaterialAccessibilityOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

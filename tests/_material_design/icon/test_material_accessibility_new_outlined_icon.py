from apysc._material_design.icon.material_accessibility_new_outlined_icon import (
    MaterialaccessibilityNewOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialaccessibilityNewOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialaccessibilityNewOutlinedIcon = (
            MaterialaccessibilityNewOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

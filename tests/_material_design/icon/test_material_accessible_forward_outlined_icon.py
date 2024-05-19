from apysc._material_design.icon.material_accessible_forward_outlined_icon import (
    MaterialaccessibleForwardOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialaccessibleForwardOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialaccessibleForwardOutlinedIcon = (
            MaterialaccessibleForwardOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

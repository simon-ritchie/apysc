from apysc._material_design.icon.material_wifi_protected_setup_icon import (
    MaterialwifiProtectedSetupIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialwifiProtectedSetupIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialwifiProtectedSetupIcon = MaterialwifiProtectedSetupIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

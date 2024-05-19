from apysc._material_design.icon.material_wifi_protected_setup_outlined_icon import MaterialwifiProtectedSetupOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialwifiProtectedSetupOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialwifiProtectedSetupOutlinedIcon = MaterialwifiProtectedSetupOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

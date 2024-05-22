from apysc._material_design.icon.material_admin_panel_settings_icon import (
    MaterialAdminPanelSettingsIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAdminPanelSettingsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAdminPanelSettingsIcon = MaterialAdminPanelSettingsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

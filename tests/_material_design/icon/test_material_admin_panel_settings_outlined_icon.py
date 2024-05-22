from apysc._material_design.icon.material_admin_panel_settings_outlined_icon import (
    MaterialAdminPanelSettingsOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAdminPanelSettingsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAdminPanelSettingsOutlinedIcon = (
            MaterialAdminPanelSettingsOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

from apysc._material_design.icon.material_admin_panel_settings_icon import (
    MaterialadminPanelSettingsIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialadminPanelSettingsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialadminPanelSettingsIcon = MaterialadminPanelSettingsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

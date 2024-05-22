from apysc._material_design.icon.material_settings_ethernet_outlined_icon import (
    MaterialSettingsEthernetOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSettingsEthernetOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSettingsEthernetOutlinedIcon = (
            MaterialSettingsEthernetOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

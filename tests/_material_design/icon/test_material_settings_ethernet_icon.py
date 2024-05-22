from apysc._material_design.icon.material_settings_ethernet_icon import (
    MaterialSettingsEthernetIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSettingsEthernetIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSettingsEthernetIcon = MaterialSettingsEthernetIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

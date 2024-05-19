from apysc._material_design.icon.material_settings_ethernet_icon import (
    MaterialsettingsEthernetIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsettingsEthernetIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsettingsEthernetIcon = MaterialsettingsEthernetIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

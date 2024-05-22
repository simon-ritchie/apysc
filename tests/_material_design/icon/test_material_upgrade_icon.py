from apysc._material_design.icon.material_upgrade_icon import MaterialUpgradeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialUpgradeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialUpgradeIcon = MaterialUpgradeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

from apysc._material_design.icon.material_upgrade_outlined_icon import (
    MaterialUpgradeOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialUpgradeOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialUpgradeOutlinedIcon = MaterialUpgradeOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

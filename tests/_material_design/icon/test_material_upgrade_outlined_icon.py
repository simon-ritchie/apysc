from apysc._material_design.icon.material_upgrade_outlined_icon import (
    MaterialupgradeOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialupgradeOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialupgradeOutlinedIcon = MaterialupgradeOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

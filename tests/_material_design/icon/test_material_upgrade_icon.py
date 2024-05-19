from apysc._material_design.icon.material_upgrade_icon import MaterialupgradeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialupgradeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialupgradeIcon = MaterialupgradeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

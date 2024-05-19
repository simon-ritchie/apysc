from apysc._material_design.icon.material_inventory_icon import MaterialinventoryIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialinventoryIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialinventoryIcon = MaterialinventoryIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

from apysc._material_design.icon.material_inbox_icon import MaterialinboxIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialinboxIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialinboxIcon = MaterialinboxIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

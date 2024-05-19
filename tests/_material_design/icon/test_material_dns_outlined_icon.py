from apysc._material_design.icon.material_dns_outlined_icon import MaterialdnsOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdnsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdnsOutlinedIcon = MaterialdnsOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

from apysc._material_design.icon.material_dns_icon import MaterialdnsIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdnsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdnsIcon = MaterialdnsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

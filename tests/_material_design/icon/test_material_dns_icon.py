from apysc._material_design.icon.material_dns_icon import MaterialDnsIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDnsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDnsIcon = MaterialDnsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

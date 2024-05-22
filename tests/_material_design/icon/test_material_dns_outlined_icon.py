from apysc._material_design.icon.material_dns_outlined_icon import (
    MaterialDnsOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDnsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDnsOutlinedIcon = MaterialDnsOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

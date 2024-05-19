from apysc._material_design.icon.material_domain_disabled_outlined_icon import (
    MaterialdomainDisabledOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdomainDisabledOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdomainDisabledOutlinedIcon = MaterialdomainDisabledOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

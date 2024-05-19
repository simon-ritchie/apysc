from apysc._material_design.icon.material_domain_disabled_icon import (
    MaterialdomainDisabledIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdomainDisabledIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdomainDisabledIcon = MaterialdomainDisabledIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

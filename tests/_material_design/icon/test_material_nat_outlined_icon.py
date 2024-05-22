from apysc._material_design.icon.material_nat_outlined_icon import (
    MaterialNatOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialNatOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialNatOutlinedIcon = MaterialNatOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

from apysc._material_design.icon.material_nat_outlined_icon import (
    MaterialnatOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialnatOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialnatOutlinedIcon = MaterialnatOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

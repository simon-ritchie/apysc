from apysc._material_design.icon.material_rounded_corner_outlined_icon import (
    MaterialRoundedCornerOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRoundedCornerOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRoundedCornerOutlinedIcon = MaterialRoundedCornerOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

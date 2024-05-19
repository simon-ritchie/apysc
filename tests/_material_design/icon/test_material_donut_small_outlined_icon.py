from apysc._material_design.icon.material_donut_small_outlined_icon import (
    MaterialdonutSmallOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdonutSmallOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdonutSmallOutlinedIcon = MaterialdonutSmallOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

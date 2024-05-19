from apysc._material_design.icon.material_donut_large_outlined_icon import (
    MaterialdonutLargeOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdonutLargeOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdonutLargeOutlinedIcon = MaterialdonutLargeOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

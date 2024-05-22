from apysc._material_design.icon.material_donut_large_outlined_icon import (
    MaterialDonutLargeOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDonutLargeOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDonutLargeOutlinedIcon = MaterialDonutLargeOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

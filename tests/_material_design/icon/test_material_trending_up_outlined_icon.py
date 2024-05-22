from apysc._material_design.icon.material_trending_up_outlined_icon import (
    MaterialTrendingUpOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTrendingUpOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTrendingUpOutlinedIcon = MaterialTrendingUpOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

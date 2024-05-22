from apysc._material_design.icon.material_trending_down_outlined_icon import (
    MaterialTrendingDownOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTrendingDownOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTrendingDownOutlinedIcon = MaterialTrendingDownOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

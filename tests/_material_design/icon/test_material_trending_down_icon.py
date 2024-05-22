from apysc._material_design.icon.material_trending_down_icon import (
    MaterialTrendingDownIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTrendingDownIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTrendingDownIcon = MaterialTrendingDownIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

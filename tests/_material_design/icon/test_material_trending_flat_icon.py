from apysc._material_design.icon.material_trending_flat_icon import (
    MaterialTrendingFlatIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTrendingFlatIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTrendingFlatIcon = MaterialTrendingFlatIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

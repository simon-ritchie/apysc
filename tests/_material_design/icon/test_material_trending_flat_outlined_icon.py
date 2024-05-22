from apysc._material_design.icon.material_trending_flat_outlined_icon import (
    MaterialTrendingFlatOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTrendingFlatOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTrendingFlatOutlinedIcon = MaterialTrendingFlatOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

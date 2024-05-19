from apysc._material_design.icon.material_trending_flat_outlined_icon import (
    MaterialtrendingFlatOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtrendingFlatOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtrendingFlatOutlinedIcon = MaterialtrendingFlatOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

from apysc._material_design.icon.material_trending_down_icon import MaterialtrendingDownIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtrendingDownIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtrendingDownIcon = MaterialtrendingDownIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

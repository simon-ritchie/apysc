from apysc._material_design.icon.material_trending_up_icon import MaterialTrendingUpIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTrendingUpIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTrendingUpIcon = MaterialTrendingUpIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

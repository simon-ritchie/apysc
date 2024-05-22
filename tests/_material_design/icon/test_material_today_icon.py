from apysc._material_design.icon.material_today_icon import MaterialTodayIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTodayIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTodayIcon = MaterialTodayIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

from apysc._material_design.icon.material_today_icon import MaterialtodayIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtodayIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtodayIcon = MaterialtodayIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

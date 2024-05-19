from apysc._material_design.icon.material_calendar_today_icon import MaterialcalendarTodayIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcalendarTodayIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcalendarTodayIcon = MaterialcalendarTodayIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

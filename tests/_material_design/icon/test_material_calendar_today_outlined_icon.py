from apysc._material_design.icon.material_calendar_today_outlined_icon import MaterialcalendarTodayOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcalendarTodayOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcalendarTodayOutlinedIcon = MaterialcalendarTodayOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

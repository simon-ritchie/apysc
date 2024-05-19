from apysc._material_design.icon.material_calendar_view_day_icon import MaterialcalendarViewDayIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcalendarViewDayIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcalendarViewDayIcon = MaterialcalendarViewDayIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

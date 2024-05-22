from apysc._material_design.icon.material_calendar_view_day_icon import (
    MaterialCalendarViewDayIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCalendarViewDayIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCalendarViewDayIcon = MaterialCalendarViewDayIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

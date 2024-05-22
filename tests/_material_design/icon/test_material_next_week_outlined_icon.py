from apysc._material_design.icon.material_next_week_outlined_icon import (
    MaterialNextWeekOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialNextWeekOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialNextWeekOutlinedIcon = MaterialNextWeekOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

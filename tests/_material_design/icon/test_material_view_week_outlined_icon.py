from apysc._material_design.icon.material_view_week_outlined_icon import (
    MaterialviewWeekOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialviewWeekOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialviewWeekOutlinedIcon = MaterialviewWeekOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

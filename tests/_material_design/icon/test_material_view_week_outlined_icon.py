from apysc._material_design.icon.material_view_week_outlined_icon import (
    MaterialViewWeekOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialViewWeekOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialViewWeekOutlinedIcon = MaterialViewWeekOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

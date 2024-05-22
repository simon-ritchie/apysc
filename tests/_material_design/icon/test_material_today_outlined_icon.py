from apysc._material_design.icon.material_today_outlined_icon import (
    MaterialTodayOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTodayOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTodayOutlinedIcon = MaterialTodayOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

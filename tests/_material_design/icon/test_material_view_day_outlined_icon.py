from apysc._material_design.icon.material_view_day_outlined_icon import (
    MaterialViewDayOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialViewDayOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialViewDayOutlinedIcon = MaterialViewDayOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

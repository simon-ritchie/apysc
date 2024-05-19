from apysc._material_design.icon.material_schedule_outlined_icon import (
    MaterialscheduleOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialscheduleOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialscheduleOutlinedIcon = MaterialscheduleOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

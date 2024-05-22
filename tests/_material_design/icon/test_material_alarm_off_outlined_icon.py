from apysc._material_design.icon.material_alarm_off_outlined_icon import (
    MaterialAlarmOffOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAlarmOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAlarmOffOutlinedIcon = MaterialAlarmOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

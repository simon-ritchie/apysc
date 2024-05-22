from apysc._material_design.icon.material_alarm_on_outlined_icon import (
    MaterialAlarmOnOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAlarmOnOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAlarmOnOutlinedIcon = MaterialAlarmOnOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

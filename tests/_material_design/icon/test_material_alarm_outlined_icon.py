from apysc._material_design.icon.material_alarm_outlined_icon import (
    MaterialAlarmOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAlarmOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAlarmOutlinedIcon = MaterialAlarmOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

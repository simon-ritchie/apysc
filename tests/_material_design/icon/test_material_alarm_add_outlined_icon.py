from apysc._material_design.icon.material_alarm_add_outlined_icon import (
    MaterialAlarmAddOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAlarmAddOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAlarmAddOutlinedIcon = MaterialAlarmAddOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

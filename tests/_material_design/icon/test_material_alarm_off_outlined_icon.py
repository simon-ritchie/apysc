from apysc._material_design.icon.material_alarm_off_outlined_icon import (
    MaterialalarmOffOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialalarmOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialalarmOffOutlinedIcon = MaterialalarmOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

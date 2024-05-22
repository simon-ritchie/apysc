from apysc._material_design.icon.material_av_timer_outlined_icon import (
    MaterialAvTimerOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAvTimerOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAvTimerOutlinedIcon = MaterialAvTimerOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

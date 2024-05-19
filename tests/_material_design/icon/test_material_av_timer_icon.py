from apysc._material_design.icon.material_av_timer_icon import MaterialavTimerIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialavTimerIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialavTimerIcon = MaterialavTimerIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

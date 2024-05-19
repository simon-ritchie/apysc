from apysc._material_design.icon.material_stop_screen_share_outlined_icon import MaterialstopScreenShareOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialstopScreenShareOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialstopScreenShareOutlinedIcon = MaterialstopScreenShareOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

from apysc._material_design.icon.material_stop_screen_share_icon import MaterialstopScreenShareIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialstopScreenShareIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialstopScreenShareIcon = MaterialstopScreenShareIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

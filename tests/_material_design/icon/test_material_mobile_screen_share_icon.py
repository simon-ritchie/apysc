from apysc._material_design.icon.material_mobile_screen_share_icon import MaterialmobileScreenShareIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialmobileScreenShareIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialmobileScreenShareIcon = MaterialmobileScreenShareIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

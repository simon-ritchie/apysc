from apysc._material_design.icon.material_mobile_screen_share_outlined_icon import MaterialmobileScreenShareOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialmobileScreenShareOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialmobileScreenShareOutlinedIcon = MaterialmobileScreenShareOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

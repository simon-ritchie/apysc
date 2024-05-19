from apysc._material_design.icon.material_video_settings_outlined_icon import MaterialvideoSettingsOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialvideoSettingsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialvideoSettingsOutlinedIcon = MaterialvideoSettingsOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

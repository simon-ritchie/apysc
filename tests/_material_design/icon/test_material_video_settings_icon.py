from apysc._material_design.icon.material_video_settings_icon import MaterialvideoSettingsIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialvideoSettingsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialvideoSettingsIcon = MaterialvideoSettingsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

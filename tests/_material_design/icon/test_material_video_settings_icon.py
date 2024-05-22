from apysc._material_design.icon.material_video_settings_icon import (
    MaterialVideoSettingsIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialVideoSettingsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialVideoSettingsIcon = MaterialVideoSettingsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

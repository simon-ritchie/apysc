from apysc._material_design.icon.material_settings_voice_icon import (
    MaterialSettingsVoiceIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSettingsVoiceIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSettingsVoiceIcon = MaterialSettingsVoiceIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

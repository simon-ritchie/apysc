from apysc._material_design.icon.material_settings_voice_icon import (
    MaterialsettingsVoiceIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsettingsVoiceIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsettingsVoiceIcon = MaterialsettingsVoiceIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

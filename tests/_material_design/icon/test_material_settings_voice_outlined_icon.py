from apysc._material_design.icon.material_settings_voice_outlined_icon import MaterialsettingsVoiceOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsettingsVoiceOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsettingsVoiceOutlinedIcon = MaterialsettingsVoiceOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

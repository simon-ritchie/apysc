from apysc._material_design.icon.material_record_voice_over_outlined_icon import MaterialrecordVoiceOverOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialrecordVoiceOverOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialrecordVoiceOverOutlinedIcon = MaterialrecordVoiceOverOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

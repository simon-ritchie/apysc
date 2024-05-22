from apysc._material_design.icon.material_record_voice_over_outlined_icon import (
    MaterialRecordVoiceOverOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRecordVoiceOverOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRecordVoiceOverOutlinedIcon = (
            MaterialRecordVoiceOverOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

from apysc._material_design.icon.material_record_voice_over_icon import (
    MaterialRecordVoiceOverIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRecordVoiceOverIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRecordVoiceOverIcon = MaterialRecordVoiceOverIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

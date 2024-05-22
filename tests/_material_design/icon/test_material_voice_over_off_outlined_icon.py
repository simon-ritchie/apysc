from apysc._material_design.icon.material_voice_over_off_outlined_icon import (
    MaterialVoiceOverOffOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialVoiceOverOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialVoiceOverOffOutlinedIcon = MaterialVoiceOverOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

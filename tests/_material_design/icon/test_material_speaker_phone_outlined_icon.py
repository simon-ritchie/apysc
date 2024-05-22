from apysc._material_design.icon.material_speaker_phone_outlined_icon import (
    MaterialSpeakerPhoneOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSpeakerPhoneOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSpeakerPhoneOutlinedIcon = MaterialSpeakerPhoneOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

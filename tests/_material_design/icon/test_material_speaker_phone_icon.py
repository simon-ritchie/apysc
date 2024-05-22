from apysc._material_design.icon.material_speaker_phone_icon import (
    MaterialSpeakerPhoneIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSpeakerPhoneIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSpeakerPhoneIcon = MaterialSpeakerPhoneIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

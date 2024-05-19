from apysc._material_design.icon.material_speaker_phone_outlined_icon import (
    MaterialspeakerPhoneOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialspeakerPhoneOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialspeakerPhoneOutlinedIcon = MaterialspeakerPhoneOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

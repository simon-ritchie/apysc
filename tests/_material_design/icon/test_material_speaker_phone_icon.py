from apysc._material_design.icon.material_speaker_phone_icon import MaterialspeakerPhoneIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialspeakerPhoneIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialspeakerPhoneIcon = MaterialspeakerPhoneIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

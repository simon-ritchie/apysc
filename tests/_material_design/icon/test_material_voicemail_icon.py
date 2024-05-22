from apysc._material_design.icon.material_voicemail_icon import MaterialVoicemailIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialVoicemailIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialVoicemailIcon = MaterialVoicemailIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

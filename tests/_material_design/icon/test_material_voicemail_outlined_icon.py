from apysc._material_design.icon.material_voicemail_outlined_icon import (
    MaterialVoicemailOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialVoicemailOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialVoicemailOutlinedIcon = MaterialVoicemailOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

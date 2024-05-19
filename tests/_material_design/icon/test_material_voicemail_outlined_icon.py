from apysc._material_design.icon.material_voicemail_outlined_icon import (
    MaterialvoicemailOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialvoicemailOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialvoicemailOutlinedIcon = MaterialvoicemailOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

from apysc._material_design.icon.material_voice_over_off_icon import MaterialvoiceOverOffIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialvoiceOverOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialvoiceOverOffIcon = MaterialvoiceOverOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

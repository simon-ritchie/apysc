from apysc._material_design.icon.material_fingerprint_icon import MaterialfingerprintIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfingerprintIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfingerprintIcon = MaterialfingerprintIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

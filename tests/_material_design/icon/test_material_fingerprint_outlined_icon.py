from apysc._material_design.icon.material_fingerprint_outlined_icon import MaterialfingerprintOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfingerprintOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfingerprintOutlinedIcon = MaterialfingerprintOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

from apysc._material_design.icon.material_dialer_sip_icon import MaterialdialerSipIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdialerSipIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdialerSipIcon = MaterialdialerSipIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

from apysc._material_design.icon.material_dialer_sip_icon import MaterialDialerSipIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDialerSipIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDialerSipIcon = MaterialDialerSipIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

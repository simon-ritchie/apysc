from apysc._material_design.icon.material_privacy_tip_icon import MaterialPrivacyTipIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPrivacyTipIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPrivacyTipIcon = MaterialPrivacyTipIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

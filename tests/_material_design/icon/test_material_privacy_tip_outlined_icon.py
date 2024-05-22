from apysc._material_design.icon.material_privacy_tip_outlined_icon import (
    MaterialPrivacyTipOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPrivacyTipOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPrivacyTipOutlinedIcon = MaterialPrivacyTipOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

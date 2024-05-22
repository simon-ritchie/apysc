from apysc._material_design.icon.material_domain_verification_outlined_icon import (
    MaterialDomainVerificationOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDomainVerificationOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDomainVerificationOutlinedIcon = (
            MaterialDomainVerificationOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

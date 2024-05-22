from apysc._material_design.icon.material_domain_verification_icon import (
    MaterialDomainVerificationIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDomainVerificationIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDomainVerificationIcon = MaterialDomainVerificationIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

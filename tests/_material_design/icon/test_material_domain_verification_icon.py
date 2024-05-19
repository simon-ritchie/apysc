from apysc._material_design.icon.material_domain_verification_icon import MaterialdomainVerificationIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdomainVerificationIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdomainVerificationIcon = MaterialdomainVerificationIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

from apysc._material_design.icon.material_app_registration_icon import (
    MaterialAppRegistrationIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAppRegistrationIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAppRegistrationIcon = MaterialAppRegistrationIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

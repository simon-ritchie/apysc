from apysc._material_design.icon.material_app_registration_icon import MaterialappRegistrationIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialappRegistrationIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialappRegistrationIcon = MaterialappRegistrationIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

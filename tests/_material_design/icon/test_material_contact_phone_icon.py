from apysc._material_design.icon.material_contact_phone_icon import MaterialcontactPhoneIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcontactPhoneIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcontactPhoneIcon = MaterialcontactPhoneIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

from apysc._material_design.icon.material_contact_support_icon import MaterialcontactSupportIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcontactSupportIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcontactSupportIcon = MaterialcontactSupportIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

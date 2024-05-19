from apysc._material_design.icon.material_contact_mail_icon import (
    MaterialcontactMailIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcontactMailIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcontactMailIcon = MaterialcontactMailIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

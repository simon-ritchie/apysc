from apysc._material_design.icon.material_contact_mail_outlined_icon import (
    MaterialcontactMailOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcontactMailOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcontactMailOutlinedIcon = MaterialcontactMailOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

from apysc._material_design.icon.material_contact_phone_outlined_icon import (
    MaterialcontactPhoneOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcontactPhoneOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcontactPhoneOutlinedIcon = MaterialcontactPhoneOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

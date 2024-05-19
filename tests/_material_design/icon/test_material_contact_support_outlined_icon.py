from apysc._material_design.icon.material_contact_support_outlined_icon import (
    MaterialcontactSupportOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcontactSupportOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcontactSupportOutlinedIcon = MaterialcontactSupportOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

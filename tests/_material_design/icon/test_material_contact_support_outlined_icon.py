from apysc._material_design.icon.material_contact_support_outlined_icon import (
    MaterialContactSupportOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialContactSupportOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialContactSupportOutlinedIcon = MaterialContactSupportOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

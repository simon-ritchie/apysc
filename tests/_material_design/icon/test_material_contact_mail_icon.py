from apysc._material_design.icon.material_contact_mail_icon import (
    MaterialContactMailIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialContactMailIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialContactMailIcon = MaterialContactMailIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

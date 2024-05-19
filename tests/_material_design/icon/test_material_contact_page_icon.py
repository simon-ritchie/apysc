from apysc._material_design.icon.material_contact_page_icon import (
    MaterialcontactPageIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcontactPageIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcontactPageIcon = MaterialcontactPageIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

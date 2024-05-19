from apysc._material_design.icon.material_contact_page_outlined_icon import (
    MaterialcontactPageOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcontactPageOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcontactPageOutlinedIcon = MaterialcontactPageOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

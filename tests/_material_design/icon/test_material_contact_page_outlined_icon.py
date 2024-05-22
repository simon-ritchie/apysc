from apysc._material_design.icon.material_contact_page_outlined_icon import (
    MaterialContactPageOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialContactPageOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialContactPageOutlinedIcon = MaterialContactPageOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

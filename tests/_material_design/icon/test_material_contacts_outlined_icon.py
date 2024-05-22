from apysc._material_design.icon.material_contacts_outlined_icon import (
    MaterialContactsOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialContactsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialContactsOutlinedIcon = MaterialContactsOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

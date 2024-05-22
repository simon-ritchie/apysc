from apysc._material_design.icon.material_contacts_icon import MaterialContactsIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialContactsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialContactsIcon = MaterialContactsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

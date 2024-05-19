from apysc._material_design.icon.material_import_contacts_icon import MaterialimportContactsIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialimportContactsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialimportContactsIcon = MaterialimportContactsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

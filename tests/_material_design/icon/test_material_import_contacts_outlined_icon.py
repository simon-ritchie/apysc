from apysc._material_design.icon.material_import_contacts_outlined_icon import (
    MaterialImportContactsOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialImportContactsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialImportContactsOutlinedIcon = MaterialImportContactsOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

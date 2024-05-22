from apysc._material_design.icon.material_import_export_icon import (
    MaterialImportExportIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialImportExportIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialImportExportIcon = MaterialImportExportIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

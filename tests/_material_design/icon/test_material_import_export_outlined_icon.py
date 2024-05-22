from apysc._material_design.icon.material_import_export_outlined_icon import (
    MaterialImportExportOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialImportExportOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialImportExportOutlinedIcon = MaterialImportExportOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

from apysc._material_design.icon.material_import_export_icon import (
    MaterialimportExportIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialimportExportIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialimportExportIcon = MaterialimportExportIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

from apysc._material_design.icon.material_restore_page_icon import (
    MaterialRestorePageIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRestorePageIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRestorePageIcon = MaterialRestorePageIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

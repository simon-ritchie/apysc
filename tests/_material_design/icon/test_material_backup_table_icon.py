from apysc._material_design.icon.material_backup_table_icon import (
    MaterialBackupTableIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialBackupTableIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialBackupTableIcon = MaterialBackupTableIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

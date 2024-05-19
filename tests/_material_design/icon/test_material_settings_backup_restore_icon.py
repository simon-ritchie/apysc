from apysc._material_design.icon.material_settings_backup_restore_icon import (
    MaterialsettingsBackupRestoreIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsettingsBackupRestoreIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsettingsBackupRestoreIcon = MaterialsettingsBackupRestoreIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

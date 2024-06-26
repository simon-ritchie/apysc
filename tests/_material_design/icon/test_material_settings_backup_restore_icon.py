from apysc._material_design.icon.material_settings_backup_restore_icon import (
    MaterialSettingsBackupRestoreIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSettingsBackupRestoreIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSettingsBackupRestoreIcon = MaterialSettingsBackupRestoreIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

from apysc._material_design.icon.material_settings_backup_restore_outlined_icon import MaterialsettingsBackupRestoreOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsettingsBackupRestoreOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsettingsBackupRestoreOutlinedIcon = MaterialsettingsBackupRestoreOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

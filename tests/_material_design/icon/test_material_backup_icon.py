from apysc._material_design.icon.material_backup_icon import MaterialbackupIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialbackupIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialbackupIcon = MaterialbackupIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

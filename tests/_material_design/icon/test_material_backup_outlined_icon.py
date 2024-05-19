from apysc._material_design.icon.material_backup_outlined_icon import MaterialbackupOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialbackupOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialbackupOutlinedIcon = MaterialbackupOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

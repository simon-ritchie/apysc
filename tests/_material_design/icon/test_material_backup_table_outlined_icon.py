from apysc._material_design.icon.material_backup_table_outlined_icon import MaterialbackupTableOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialbackupTableOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialbackupTableOutlinedIcon = MaterialbackupTableOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

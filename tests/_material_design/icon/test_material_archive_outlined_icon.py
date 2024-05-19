from apysc._material_design.icon.material_archive_outlined_icon import MaterialarchiveOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialarchiveOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialarchiveOutlinedIcon = MaterialarchiveOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

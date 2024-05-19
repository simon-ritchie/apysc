from apysc._material_design.icon.material_archive_icon import MaterialarchiveIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialarchiveIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialarchiveIcon = MaterialarchiveIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

from apysc._material_design.icon.material_table_view_icon import MaterialtableViewIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtableViewIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtableViewIcon = MaterialtableViewIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

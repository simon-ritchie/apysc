from apysc._material_design.icon.material_view_column_icon import MaterialviewColumnIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialviewColumnIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialviewColumnIcon = MaterialviewColumnIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

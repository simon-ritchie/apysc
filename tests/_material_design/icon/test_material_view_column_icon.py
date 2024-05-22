from apysc._material_design.icon.material_view_column_icon import MaterialViewColumnIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialViewColumnIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialViewColumnIcon = MaterialViewColumnIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

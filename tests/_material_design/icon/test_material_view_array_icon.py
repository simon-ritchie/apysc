from apysc._material_design.icon.material_view_array_icon import MaterialViewArrayIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialViewArrayIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialViewArrayIcon = MaterialViewArrayIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

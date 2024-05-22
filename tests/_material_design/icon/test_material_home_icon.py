from apysc._material_design.icon.material_home_icon import MaterialHomeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHomeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHomeIcon = MaterialHomeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

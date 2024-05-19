from apysc._material_design.icon.material_tour_icon import MaterialtourIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtourIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtourIcon = MaterialtourIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

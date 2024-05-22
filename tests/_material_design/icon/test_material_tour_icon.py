from apysc._material_design.icon.material_tour_icon import MaterialTourIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTourIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTourIcon = MaterialTourIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

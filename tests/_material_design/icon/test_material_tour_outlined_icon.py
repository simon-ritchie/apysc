from apysc._material_design.icon.material_tour_outlined_icon import MaterialtourOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtourOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtourOutlinedIcon = MaterialtourOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

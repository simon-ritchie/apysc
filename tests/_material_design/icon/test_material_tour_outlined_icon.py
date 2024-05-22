from apysc._material_design.icon.material_tour_outlined_icon import (
    MaterialTourOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTourOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTourOutlinedIcon = MaterialTourOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

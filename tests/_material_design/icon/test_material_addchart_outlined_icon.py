from apysc._material_design.icon.material_addchart_outlined_icon import (
    MaterialAddchartOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAddchartOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAddchartOutlinedIcon = MaterialAddchartOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

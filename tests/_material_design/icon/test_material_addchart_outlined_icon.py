from apysc._material_design.icon.material_addchart_outlined_icon import (
    MaterialaddchartOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialaddchartOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialaddchartOutlinedIcon = MaterialaddchartOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

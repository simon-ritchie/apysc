from apysc._material_design.icon.material_eco_outlined_icon import (
    MaterialecoOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialecoOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialecoOutlinedIcon = MaterialecoOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

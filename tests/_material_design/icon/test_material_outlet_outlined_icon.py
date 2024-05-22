from apysc._material_design.icon.material_outlet_outlined_icon import (
    MaterialOutletOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialOutletOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialOutletOutlinedIcon = MaterialOutletOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

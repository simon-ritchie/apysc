from apysc._material_design.icon.material_polymer_outlined_icon import (
    MaterialPolymerOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPolymerOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPolymerOutlinedIcon = MaterialPolymerOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

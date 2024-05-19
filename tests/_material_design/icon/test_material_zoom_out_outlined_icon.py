from apysc._material_design.icon.material_zoom_out_outlined_icon import (
    MaterialzoomOutOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialzoomOutOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialzoomOutOutlinedIcon = MaterialzoomOutOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

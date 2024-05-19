from apysc._material_design.icon.material_zoom_in_outlined_icon import (
    MaterialzoomInOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialzoomInOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialzoomInOutlinedIcon = MaterialzoomInOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

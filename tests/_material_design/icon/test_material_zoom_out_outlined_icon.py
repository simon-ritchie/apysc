from apysc._material_design.icon.material_zoom_out_outlined_icon import (
    MaterialZoomOutOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialZoomOutOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialZoomOutOutlinedIcon = MaterialZoomOutOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

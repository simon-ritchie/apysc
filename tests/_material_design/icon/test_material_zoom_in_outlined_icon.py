from apysc._material_design.icon.material_zoom_in_outlined_icon import (
    MaterialZoomInOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialZoomInOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialZoomInOutlinedIcon = MaterialZoomInOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

from apysc._material_design.icon.material_zoom_in_icon import MaterialZoomInIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialZoomInIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialZoomInIcon = MaterialZoomInIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()

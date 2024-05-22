from apysc._material_design.icon.material_zoom_out_icon import MaterialZoomOutIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialZoomOutIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialZoomOutIcon = MaterialZoomOutIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
